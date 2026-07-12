import asyncio
import sqlite3
from datetime import date, datetime, timedelta
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ==================== КОНФИГ ===================="
ADMIN_ID = 8684827145
TON_WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps"
TON_TO_TONIX = 1_000_000
BASE_CLICK = 10
DAILY_LIMIT = 1000
MIN_WITHDRAW = 0.5

PICKAXES = {
    "bronze": 50, "silver": 80, "gold": 120, "platinum": 180, "mythic": 300
}
PICKAXE_PRICES = {
    "bronze": 2.7, "silver": 4.0, "gold": 5.8, "platinum": 8.5, "mythic": 14.0
}

# ==================== БАЗА ДАННЫХ ====================
conn = sqlite3.connect("toniks.db")
c = conn.cursor()
c.executescript("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY, username TEXT,
    balance_tonix INTEGER DEFAULT 0, balance_ton REAL DEFAULT 0.0,
    clicks_today INTEGER DEFAULT 0, last_click_date TEXT,
    pickaxe TEXT, pickaxe_expire TEXT,
    energy_boost INTEGER DEFAULT 1000, energy_expire TEXT,
    multiplier REAL DEFAULT 1.0, multiplier_expire TEXT,
    bonus_day INTEGER DEFAULT 0, last_bonus_date TEXT,
    referer_id INTEGER
);
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT, creator_id INTEGER,
    channel_link TEXT, reward INTEGER, total_executions INTEGER DEFAULT 500,
    executions_done INTEGER DEFAULT 0, status TEXT DEFAULT 'pending'
);
CREATE TABLE IF NOT EXISTS task_done (task_id INTEGER, user_id INTEGER);
CREATE TABLE IF NOT EXISTS promo (code TEXT PRIMARY KEY, reward INTEGER, max_uses INTEGER, used INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS promo_used (code TEXT, user_id INTEGER);
CREATE TABLE IF NOT EXISTS admins (user_id INTEGER PRIMARY KEY, can_tasks INTEGER DEFAULT 0, can_promo INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS deposits (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, amount REAL, status TEXT DEFAULT 'pending');
CREATE TABLE IF NOT EXISTS withdraws (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, amount REAL, wallet TEXT, status TEXT DEFAULT 'pending');
""")
c.execute("INSERT OR IGNORE INTO admins (user_id, can_tasks, can_promo) VALUES (?, 1, 1)", (ADMIN_ID,))
conn.commit()

# ==================== БОТ ====================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# ==================== КЛАВИАТУРЫ ====================
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="⛏ Кликер")],
    [KeyboardButton(text="📋 Задания"), KeyboardButton(text="👥 Рефералы")],
    [KeyboardButton(text="🎁 Бонусы"), KeyboardButton(text="📊 Биржа")],
    [KeyboardButton(text="👤 Профиль")]
])

# ==================== /start ====================
@router.message(Command("start"))
async def start(msg: types.Message):
    uid = msg.from_user.id
    ref = msg.text.split()
    ref_id = int(ref[1]) if len(ref) > 1 and ref[1].isdigit() else None

    c.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (uid, msg.from_user.username))
    if ref_id and ref_id != uid:
        c.execute("SELECT user_id FROM users WHERE user_id=?", (ref_id,))
        if c.fetchone():
            c.execute("UPDATE users SET referer_id=? WHERE user_id=? AND referer_id IS NULL", (ref_id, uid))
            c.execute("UPDATE users SET balance_tonix=balance_tonix+1000 WHERE user_id=?", (ref_id,))
    conn.commit()
    await msg.answer(
        "⚡ Добро пожаловать в Тоникс!\n\n"
        "💎 Зарабатывай Тониксы в кликере\n"
        "📋 Выполняй задания\n"
        "👥 Приглашай друзей\n"
        "📊 Торгуй на бирже\n\n"
        "📍 Твой ID: `{}`\n"
        "📍 Для пополнения: отправь TON на `{}`\n"
        "📍 В комментарии к переводу укажи свой ID\n"
        "📍 Затем нажми кнопку «Я пополнил» в Профиле".format(uid, TON_WALLET),
        reply_markup=main_kb,
        parse_mode="Markdown"
    )

# ==================== КЛИКЕР ====================
@router.message(F.text == "⛏ Кликер")
async def clicker(msg: types.Message):
    await msg.answer("⛏ Жми на кнопку и зарабатывай Тониксы!",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💎 КЛИКНУТЬ (+10 T)", callback_data="cl")],
            [InlineKeyboardButton(text="🏪 Магазин", callback_data="shop")]
        ]))

@router.callback_query(F.data == "cl")
async def click(cb: types.CallbackQuery):
    uid = cb.from_user.id
    today = str(date.today())
    c.execute("SELECT * FROM users WHERE user_id=?", (uid,))
    u = c.fetchone()
    if not u:
        c.execute("INSERT INTO users (user_id) VALUES (?)", (uid,))
        conn.commit()
        u = (uid, None, 0, 0, 0, None, None, None, 1000, None, 1.0, None, 0, None, None)

    _, _, bal, ton, clicks, ld, pk, pk_exp, en, en_exp, mult, mult_exp, bonus, lb, ref = u

    if ld != today:
        clicks = 0
    if en_exp and datetime.now() > datetime.fromisoformat(en_exp):
        en = 1000
    if clicks >= en:
        await cb.answer("🔴 Лимит кликов на сегодня! Купи энергию в магазине.", show_alert=True)
        return

    per_click = BASE_CLICK
    if pk and pk_exp and datetime.now() < datetime.fromisoformat(pk_exp):
        per_click += PICKAXES.get(pk, 0)
    if mult_exp and datetime.now() > datetime.fromisoformat(mult_exp):
        mult = 1.0
    reward = int(per_click * mult)

    clicks += 1
    bal += reward
    c.execute("UPDATE users SET balance_tonix=?, clicks_today=?, last_click_date=? WHERE user_id=?",
              (bal, clicks, today, uid))
    conn.commit()

    await cb.message.edit_text(
        f"💎 +{reward} Тониксов!\n💰 Баланс: {bal:,} Т\n⚡ Осталось кликов: {en - clicks}/{en}",
        reply_markup=cb.message.reply_markup)
    await cb.answer(f"+{reward} Тониксов!")

@router.callback_query(F.data == "shop")
async def shop(cb: types.CallbackQuery):
    await cb.message.edit_text("🏪 Магазин:\n\nВыбери товар (оплата вручную админу):",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"🥉 Бронзовая +50/клик (60д) - {PICKAXE_PRICES['bronze']} TON", callback_data="buy_bronze")],
            [InlineKeyboardButton(text=f"🥈 Серебряная +80/клик (60д) - {PICKAXE_PRICES['silver']} TON", callback_data="buy_silver")],
            [InlineKeyboardButton(text=f"🥇 Золотая +120/клик (60д) - {PICKAXE_PRICES['gold']} TON", callback_data="buy_gold")],
            [InlineKeyboardButton(text=f"💠 Платиновая +180/клик (60д) - {PICKAXE_PRICES['platinum']} TON", callback_data="buy_platinum")],
            [InlineKeyboardButton(text=f"🔮 Мифическая +300/клик (60д) - {PICKAXE_PRICES['mythic']} TON", callback_data="buy_mythic")],
            [InlineKeyboardButton(text="⚡ +500 энергии (5д) - 1.5 TON", callback_data="buy_en500")],
            [InlineKeyboardButton(text="🔥 x2 доход (24ч) - 0.5 TON", callback_data="buy_x2")],
            [InlineKeyboardButton(text="💰 Мешок +100K - 0.1 TON", callback_data="buy_bag")],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="back_clicker")]
        ]))

@router.callback_query(F.data.startswith("buy_"))
async def buy(cb: types.CallbackQuery):
    item = cb.data[4:]
    uid = cb.from_user.id
    now = datetime.now()

    if item in PICKAXES:
        price = PICKAXE_PRICES[item]
        exp = (now + timedelta(days=60)).isoformat()
        txt = f"⛏ Кирка: {item}\n💰 Цена: {price} TON\n\nОтправь {price} TON на `{TON_WALLET}`\nВ комментарии укажи ID: `{uid}`\nЗатем нажми «Я пополнил» в Профиле.\nАдмин проверит и выдаст кирку."
    elif item == "en500":
        exp = (now + timedelta(days=5)).isoformat()
        txt = f"⚡ +500 энергии на 5 дней\n💰 Цена: 1.5 TON\n\nОтправь 1.5 TON на `{TON_WALLET}`\nКомментарий: `{uid}`"
    elif item == "x2":
        exp = (now + timedelta(days=1)).isoformat()
        txt = f"🔥 x2 доход на 24ч\n💰 Цена: 0.5 TON\n\nОтправь 0.5 TON на `{TON_WALLET}`\nКомментарий: `{uid}`"
    elif item == "bag":
        txt = f"💰 Мешок +100K Тониксов\n💰 Цена: 0.1 TON\n\nОтправь 0.1 TON на `{TON_WALLET}`\nКомментарий: `{uid}`"
    else:
        txt = "Товар не найден"

    c.execute("INSERT INTO deposits (user_id, amount) VALUES (?, ?)", (uid, 0))
    conn.commit()
    await cb.message.answer(txt, parse_mode="Markdown")
    await cb.answer("Проверь сообщение выше ⬆️", show_alert=True)

@router.callback_query(F.data == "back_clicker")
async def back_clicker(cb: types.CallbackQuery):
    await cb.message.edit_text("⛏ Жми на кнопку!",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💎 КЛИКНУТЬ (+10 T)", callback_data="cl")],
            [InlineKeyboardButton(text="🏪 Магазин", callback_data="shop")]
        ]))

# ==================== ЗАДАНИЯ ====================
@router.message(F.text == "📋 Задания")
async def tasks(msg: types.Message):
    c.execute("SELECT task_id, channel_link, reward, executions_done, total_executions FROM tasks WHERE status='approved'")
    all_tasks = c.fetchall()
    if not all_tasks:
        await msg.answer("📋 Нет активных заданий.\n\nСоздать задание: /create_task ссылка")
        return
    kb = []
    for t in all_tasks:
        tid, link, reward, done, total = t
        kb.append([InlineKeyboardButton(text=f"{link} (+{reward} Т) [{done}/{total}]", callback_data=f"do_{tid}")])
    await msg.answer("📋 Доступные задания:", reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))

@router.message(Command("create_task"))
async def create_task(msg: types.Message):
    uid = msg.from_user.id
    args = msg.text.split()
    if len(args) < 2:
        await msg.answer("Использование: /create_task ссылка_на_канал\nЦена: 1 TON (отправь админу)\nНаграда: 1500 Т за выполнение\nВыполнений: 500")
        return
    link = args[1]
    c.execute("INSERT INTO tasks (creator_id, channel_link, reward, total_executions, status) VALUES (?, ?, 1500, 500, 'pending')",
              (uid, link))
    conn.commit()
    c.execute("INSERT INTO deposits (user_id, amount) VALUES (?, 1.0)", (uid,))
    conn.commit()
    await msg.answer(f"📋 Задание создано и отправлено на проверку!\nКанал: {link}\nОплата: отправь 1 TON на `{TON_WALLET}` с комментарием `task_{uid}`", parse_mode="Markdown")

@router.callback_query(F.data.startswith("do_"))
async def do_task(cb: types.CallbackQuery):
    tid = int(cb.data[3:])
    uid = cb.from_user.id
    c.execute("SELECT * FROM task_done WHERE task_id=? AND user_id=?", (tid, uid))
    if c.fetchone():
        await cb.answer("❌ Уже выполнено!", show_alert=True)
        return
    c.execute("SELECT channel_link, reward, executions_done, total_executions FROM tasks WHERE task_id=?", (tid,))
    t = c.fetchone()
    if not t: return
    link, reward, done, total = t
    if done >= total:
        await cb.answer("Задание завершено!", show_alert=True)
        return

    # Проверка подписки
    try:
        ch = link.split("t.me/")[-1] if "t.me/" in link else link
        member = await bot.get_chat_member(chat_id=f"@{ch}", user_id=uid)
        if member.status in ["member", "administrator", "creator"]:
            c.execute("UPDATE users SET balance_tonix=balance_tonix+? WHERE user_id=?", (reward, uid))
            c.execute("UPDATE tasks SET executions_done=executions_done+1 WHERE task_id=?", (tid,))
            c.execute("INSERT INTO task_done (task_id, user_id) VALUES (?, ?)", (tid, uid))
            conn.commit()
            await cb.answer(f"✅ +{reward} Тониксов!", show_alert=True)
        else:
            await cb.answer(f"❌ Вы не подписаны на {link}!", show_alert=True)
    except Exception as e:
        await cb.answer(f"Ошибка: {e}", show_alert=True)

# ==================== РЕФЕРАЛЫ ====================
@router.message(F.text == "👥 Рефералы")
async def referal(msg: types.Message):
    uid = msg.from_user.id
    link = f"https://t.me/{(await bot.get_me()).username}?start={uid}"
    await msg.answer(f"👥 Твоя реферальная ссылка:\n`{link}`\n\nЗа каждого друга: +1000 Тониксов", parse_mode="Markdown")

# ==================== БОНУСЫ ====================
@router.message(F.text == "🎁 Бонусы")
async def bonus(msg: types.Message):
    uid = msg.from_user.id
    today = str(date.today())
    c.execute("SELECT bonus_day, last_bonus_date, balance_tonix FROM users WHERE user_id=?", (uid,))
    u = c.fetchone()
    if not u:
        await msg.answer("Сначала нажми /start")
        return
    day, ld, bal = u

    if ld == today:
        await msg.answer(f"🎁 Ты уже получил бонус сегодня! День {day}. Возвращайся завтра за +{((day % 7) + 1) * 1000} Т")
        return

    if ld and str(date.today()) != str((datetime.fromisoformat(ld) + timedelta(days=1)).date()):
        day = 0
    day = (day % 7) + 1
    reward = day * 1000
    bal += reward
    c.execute("UPDATE users SET bonus_day=?, last_bonus_date=?, balance_tonix=? WHERE user_id=?",
              (day, today, bal, uid))
    conn.commit()
    await msg.answer(f"🎁 День {day}: +{reward} Тониксов!\n💰 Баланс: {bal:,} Т\n\nВозвращайся завтра за +{((day % 7) + 1) * 1000} Т")

@router.message(Command("promo"))
async def promo(msg: types.Message):
    args = msg.text.split()
    if len(args) < 2:
        await msg.answer("Использование: /promo КОД")
        return
    code = args[1]
    uid = msg.from_user.id
    c.execute("SELECT * FROM promo WHERE code=?", (code,))
    p = c.fetchone()
    if not p:
        await msg.answer("❌ Промокод не найден")
        return
    c.execute("SELECT * FROM promo_used WHERE code=? AND user_id=?", (code, uid))
    if c.fetchone():
        await msg.answer("❌ Ты уже использовал этот промокод")
        return
    _, reward, max_uses, used = p
    if used >= max_uses:
        await msg.answer("❌ Промокод закончился")
        return
    c.execute("UPDATE promo SET used=used+1 WHERE code=?", (code,))
    c.execute("INSERT INTO promo_used (code, user_id) VALUES (?, ?)", (code, uid))
    c.execute("UPDATE users SET balance_tonix=balance_tonix+? WHERE user_id=?", (reward, uid))
    conn.commit()
    await msg.answer(f"✅ Промокод активирован! +{reward} Тониксов")

# ==================== БИРЖА (заглушка) ====================
@router.message(F.text == "📊 Биржа")
async def exchange(msg: types.Message):
    await msg.answer("📊 Биржа (упрощённая версия)\n\nКурс: 1 TON = 1,000,000 Тониксов\n\nКупить/продать через админа. Напиши в ЛС.")

# ==================== ПРОФИЛЬ ====================
@router.message(F.text == "👤 Профиль")
async def profile(msg: types.Message):
    uid = msg.from_user.id
    c.execute("SELECT * FROM users WHERE user_id=?", (uid,))
    u = c.fetchone()
    if not u:
        await msg.answer("Сначала /start")
        return
    _, _, bal_t, bal_ton, *_ = u
    await msg.answer(
        f"👤 Профиль\n\n"
        f"💰 Тониксы: {bal_t:,} Т\n"
        f"💎 TON: {bal_ton}\n\n"
        f"📥 Пополнение: отправь TON на `{TON_WALLET}`\n"
        f"📍 В комментарии укажи ID: `{uid}`\n"
        f"📍 Затем нажми /deposit сумма\n"
        f"📤 Вывод: /withdraw сумма адрес_кошелька (мин. {MIN_WITHDRAW} TON)",
        parse_mode="Markdown"
    )

@router.message(Command("deposit"))
async def deposit(msg: types.Message):
    uid = msg.from_user.id
    args = msg.text.split()
    if len(args) < 2:
        await msg.answer("/deposit сумма")
        return
    amount = float(args[1])
    c.execute("INSERT INTO deposits (user_id, amount, status) VALUES (?, ?, 'pending')", (uid, amount))
    conn.commit()
    await bot.send_message(ADMIN_ID, f"📥 Пополнение: {amount} TON от @{msg.from_user.username} (ID: {uid})\nПроверить и зачислить.")
    await msg.answer("✅ Заявка на пополнение отправлена админу. Ожидай.")

@router.message(Command("withdraw"))
async def withdraw(msg: types.Message):
    uid = msg.from_user.id
    args = msg.text.split()
    if len(args) < 3:
        await msg.answer(f"/withdraw сумма адрес\nМинимум: {MIN_WITHDRAW} TON")
        return
    amount = float(args[1])
    wallet = args[2]
    c.execute("SELECT balance_ton FROM users WHERE user_id=?", (uid,))
    bal = c.fetchone()
    if not bal or bal[0] < amount:
        await msg.answer("❌ Недостаточно TON")
        return
    c.execute("INSERT INTO withdraws (user_id, amount, wallet) VALUES (?, ?, ?)", (uid, amount, wallet))
    conn.commit()
    await bot.send_message(ADMIN_ID, f"📤 Вывод: {amount} TON на {wallet} от @{msg.from_user.username} (ID: {uid})")
    await msg.answer("✅ Заявка на вывод отправлена. Ожидай.")

# ==================== АДМИНКА ====================
@router.message(Command("admin"))
async def admin(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return
    await msg.answer("🔐 Админ-панель:\n/task_approve ID — одобрить задание\n/task_reject ID — отклонить\n/add_promo КОД СУММА ЛИМИТ — создать промокод\n/confirm_deposit ID_юзера СУММА — зачислить пополнение\n/confirm_withdraw ID_юзера — подтвердить вывод")

@router.message(Command("task_approve"))
async def task_approve(msg: types.Message):
    if msg.from_user.id != ADMIN_ID: return
    args = msg.text.split()
    if len(args) < 2: return
    tid = int(args[1])
    c.execute("UPDATE tasks SET status='approved' WHERE task_id=?", (tid,))
    conn.commit()
    await msg.answer(f"✅ Задание {tid} одобрено")

@router.message(Command("task_reject"))
async def task_reject(msg: types.Message):
    if msg.from_user.id != ADMIN_ID: return
    args = msg.text.split()
    if len(args) < 2: return
    tid = int(args[1])
    c.execute("UPDATE tasks SET status='rejected' WHERE task_id=?", (tid,))
    conn.commit()
    await msg.answer(f"❌ Задание {tid} отклонено")

@router.message(Command("add_promo"))
async def add_promo(msg: types.Message):
    if msg.from_user.id != ADMIN_ID: return
    args = msg.text.split()
    if len(args) < 4: return
    code, reward, limit = args[1], int(args[2]), int(args[3])
    c.execute("INSERT OR REPLACE INTO promo (code, reward, max_uses) VALUES (?, ?, ?)", (code, reward, limit))
    conn.commit()
    await msg.answer(f"✅ Промокод {code} создан: +{reward} Т, лимит {limit}")

@router.message(Command("confirm_deposit"))
async def confirm_deposit(msg: types.Message):
    if msg.from_user.id != ADMIN_ID: return
    args = msg.text.split()
    if len(args) < 3: return
    uid, amount = int(args[1]), float(args[2])
    c.execute("UPDATE users SET balance_ton=balance_ton+? WHERE user_id=?", (amount, uid))
    c.execute("UPDATE deposits SET status='done' WHERE user_id=? AND status='pending'", (uid,))
    conn.commit()
    await msg.answer(f"✅ Зачислено {amount} TON пользователю {uid}")

@router.message(Command("confirm_withdraw"))
async def confirm_withdraw(msg: types.Message):
    if msg.from_user.id != ADMIN_ID: return
    args = msg.text.split()
    if len(args) < 2: return
    uid = int(args[1])
    c.execute("SELECT amount FROM withdraws WHERE user_id=? AND status='pending'", (uid,))
    w = c.fetchone()
    if w:
        c.execute("UPDATE users SET balance_ton=balance_ton-? WHERE user_id=?", (w[0], uid))
        c.execute("UPDATE withdraws SET status='done' WHERE user_id=? AND status='pending'", (uid,))
        conn.commit()
        await msg.answer(f"✅ Вывод {w[0]} TON для {uid} подтверждён. Отправь вручную.")

# ==================== ЗАПУСК ====================
dp.include_router(router)

async def main():
    print("Тоникс запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
