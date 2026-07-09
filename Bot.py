import os
import sqlite3
import asyncio
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from flask import Flask, request

# ============================================
#  ⚙️ КОНФИГУРАЦИЯ (из .env)
# ============================================
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

if not BOT_TOKEN:
    raise ValueError("❌ Создай .env с BOT_TOKEN и ADMIN_ID")

COINS_TO_GRAM = 0.002
MIN_WITHDRAW_GRAM = 0.25
EXCHANGE_FEE = 0.03
MAX_CLICKS_PER_DAY = 1000
CLICK_REWARD = 0.02
BOOST_X2_PRICE = 0.1
BOOST_X5_PRICE = 0.5
AUTOCLICKER_PRICE = 1.0
UNLIMIT_PRICE = 0.5
REFERRAL_BONUS = 40
REFERRAL_PERCENT = 0.1

# ============================================
#  🗃️ БАЗА ДАННЫХ
# ============================================
db_conn = sqlite3.connect("bot.db", check_same_thread=False)
db = db_conn.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY, username TEXT, coins INTEGER DEFAULT 0,
    referred_by INTEGER DEFAULT 0, reg_date TEXT, clicks_today INTEGER DEFAULT 0,
    last_click_date TEXT, boost_x2_end TEXT, boost_x5_end TEXT,
    autoclicker INTEGER DEFAULT 0, unlimited_clicks INTEGER DEFAULT 0
)''')

db.execute('''CREATE TABLE IF NOT EXISTS referrals (
    id INTEGER PRIMARY KEY AUTOINCREMENT, referrer_id INTEGER, referred_id INTEGER, date TEXT
)''')

db.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT,
    reward INTEGER, task_type TEXT, link TEXT, is_active INTEGER DEFAULT 1
)''')

db.execute('''CREATE TABLE IF NOT EXISTS completed_tasks (
    user_id INTEGER, task_id INTEGER, date TEXT, PRIMARY KEY (user_id, task_id)
)''')

db.execute('''CREATE TABLE IF NOT EXISTS exchange_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, type TEXT,
    amount_coins INTEGER, amount_gram REAL, fee REAL, date TEXT
)''')
db_conn.commit()

def get_user(user_id):
    db.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    return db.fetchone()

def get_coins(user_id):
    db.execute('SELECT coins FROM users WHERE user_id = ?', (user_id,))
    row = db.fetchone()
    return row[0] if row else 0

def add_coins(user_id, amount):
    db.execute('UPDATE users SET coins = coins + ? WHERE user_id = ?', (amount, user_id))
    db_conn.commit()

def add_user(user_id, username, referred_by=0):
    db.execute('INSERT OR IGNORE INTO users (user_id, username, reg_date, referred_by) VALUES (?, ?, datetime("now"), ?)',
               (user_id, username, referred_by))
    db_conn.commit()

def get_clicks_today(user_id):
    db.execute('SELECT clicks_today, last_click_date FROM users WHERE user_id = ?', (user_id,))
    row = db.fetchone()
    if not row:
        return 0
    clicks, last_date = row
    if last_date and datetime.now().date() > datetime.fromisoformat(last_date).date():
        db.execute('UPDATE users SET clicks_today = 0, last_click_date = datetime("now") WHERE user_id = ?', (user_id,))
        db_conn.commit()
        return 0
    return clicks

def add_click(user_id):
    db.execute('UPDATE users SET clicks_today = clicks_today + 1 WHERE user_id = ?', (user_id,))
    db_conn.commit()

def get_boost(user_id, boost_type):
    db.execute(f'SELECT {boost_type} FROM users WHERE user_id = ?', (user_id,))
    row = db.fetchone()
    if row and row[0]:
        try:
            end_date = datetime.fromisoformat(row[0])
            if datetime.now() < end_date:
                return end_date
        except:
            pass
    return None

def set_boost(user_id, boost_type, hours):
    end_time = (datetime.now() + timedelta(hours=hours)).isoformat()
    db.execute(f'UPDATE users SET {boost_type} = ? WHERE user_id = ?', (end_time, user_id))
    db_conn.commit()

def add_referral(referrer_id, referred_id):
    db.execute('INSERT INTO referrals (referrer_id, referred_id, date) VALUES (?, ?, datetime("now"))', (referrer_id, referred_id))
    db_conn.commit()
    add_coins(referrer_id, REFERRAL_BONUS)

def get_referrals_count(user_id):
    db.execute('SELECT COUNT(*) FROM referrals WHERE referrer_id = ?', (user_id,))
    return db.fetchone()[0]

def get_referral_earnings(user_id):
    db.execute(f'SELECT SUM(coins) * {REFERRAL_PERCENT} FROM users WHERE user_id IN (SELECT referred_id FROM referrals WHERE referrer_id = ?)', (user_id,))
    row = db.fetchone()
    return row[0] if row and row[0] else 0

def get_tasks():
    db.execute('SELECT * FROM tasks WHERE is_active = 1')
    return db.fetchall()

def add_task(title, description, reward, task_type, link):
    db.execute('INSERT INTO tasks (title, description, reward, task_type, link) VALUES (?, ?, ?, ?, ?)',
               (title, description, reward, task_type, link))
    db_conn.commit()
    return db.lastrowid

def delete_task(task_id):
    db.execute('UPDATE tasks SET is_active = 0 WHERE id = ?', (task_id,))
    db_conn.commit()

def complete_task(user_id, task_id):
    db.execute('INSERT OR IGNORE INTO completed_tasks (user_id, task_id, date) VALUES (?, ?, datetime("now"))', (user_id, task_id))
    db_conn.commit()
    return db.rowcount > 0

def is_task_completed(user_id, task_id):
    db.execute('SELECT 1 FROM completed_tasks WHERE user_id = ? AND task_id = ?', (user_id, task_id))
    return db.fetchone() is not None

def add_exchange_history(user_id, type_, amount_coins, amount_gram, fee):
    db.execute('INSERT INTO exchange_history (user_id, type, amount_coins, amount_gram, fee, date) VALUES (?, ?, ?, ?, ?, datetime("now"))',
               (user_id, type_, amount_coins, amount_gram, fee))
    db_conn.commit()

def get_exchange_history(user_id, limit=10):
    db.execute('SELECT * FROM exchange_history WHERE user_id = ? ORDER BY date DESC LIMIT ?', (user_id, limit))
    return db.fetchall()

def get_active_today():
    db.execute('SELECT COUNT(*) FROM users WHERE last_click_date >= datetime("now", "-1 day")')
    return db.fetchone()[0]

# ============================================
#  🔘 КНОПКИ
# ============================================
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("📋 Задания", callback_data="tasks")],
        [InlineKeyboardButton("👥 Рефералка", callback_data="referrals")],
        [InlineKeyboardButton("🖱️ Кликер", callback_data="clicker")],
        [InlineKeyboardButton("💱 Биржа", callback_data="exchange")],
        [InlineKeyboardButton("⚙️ Админка", callback_data="admin")],
        [InlineKeyboardButton("📊 Профиль", callback_data="profile")]
    ])

def tasks_menu(tasks):
    buttons = [[InlineKeyboardButton(f"✅ {t[1]} (+{t[3]}🪙)", callback_data=f"task_{t[0]}")] for t in tasks]
    buttons.append([InlineKeyboardButton("🔙 Назад", callback_data="back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def clicker_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🖱️ Тапнуть!", callback_data="click_tap")],
        [InlineKeyboardButton("⚡ x2 (0.1 Gram)", callback_data="buy_boost_x2")],
        [InlineKeyboardButton("🔥 x5 (0.5 Gram)", callback_data="buy_boost_x5")],
        [InlineKeyboardButton("🤖 Автокликер (1 Gram)", callback_data="buy_autoclicker")],
        [InlineKeyboardButton("📈 Снять лимит (0.5 Gram)", callback_data="buy_unlimit")],
        [InlineKeyboardButton("📊 Статистика", callback_data="clicker_stats")],
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])

def exchange_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("💰 Купить монеты", callback_data="buy_coins")],
        [InlineKeyboardButton("💸 Продать монеты", callback_data="sell_coins")],
        [InlineKeyboardButton("💎 Вывести на Gram", callback_data="withdraw_gram")],
        [InlineKeyboardButton("📜 История", callback_data="exchange_history")],
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])

def admin_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("📢 Рассылка", callback_data="admin_mailing")],
        [InlineKeyboardButton("➕ Добавить задание", callback_data="admin_add_task")],
        [InlineKeyboardButton("🗑️ Удалить задание", callback_data="admin_delete_task")],
        [InlineKeyboardButton("🎁 Выдать монеты", callback_data="admin_give_coins")],
        [InlineKeyboardButton("📊 Статистика", callback_data="admin_stats")],
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])

# ============================================
#  🤖 БОТ
# ============================================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

class Form(StatesGroup):
    mailing_text = State()
    add_task_title = State()
    add_task_desc = State()
    add_task_reward = State()
    add_task_link = State()
    delete_task_id = State()
    give_coins_user = State()
    give_coins_amount = State()
    buy_coins_amount = State()
    sell_coins_amount = State()
    withdraw_amount = State()
    withdraw_address = State()

@router.message(Command("start"))
async def start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "user"
    
    args = message.text.split()
    referred_by = int(args[1]) if len(args) > 1 and args[1].isdigit() and int(args[1]) != user_id else 0
    if referred_by:
        add_referral(referred_by, user_id)
    
    add_user(user_id, username, referred_by)
    coins = get_coins(user_id)
    
    await message.answer(
        f"🚀 <b>Добро пожаловать в WorkX!</b>\n\n💰 Баланс: {coins} 🪙 ({(coins/100)*COINS_TO_GRAM:.4f} Gram)\n📌 Курс: 100 = {COINS_TO_GRAM} Gram\n💳 Мин. вывод: {MIN_WITHDRAW_GRAM} Gram",
        reply_markup=main_menu()
    )

@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):
    user_id = callback.from_user.id
    coins = get_coins(user_id)
    await callback.message.edit_text(
        f"📊 <b>Профиль</b>\n\n🪙 Монеты: {coins}\n💎 Gram: {(coins/100)*COINS_TO_GRAM:.4f}\n👥 Рефералов: {get_referrals_count(user_id)}\n💰 С рефералов: {get_referral_earnings(user_id):.0f} 🪙",
        reply_markup=main_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text("🏠 <b>Главное меню</b>", reply_markup=main_menu())
    await callback.answer()

# ----- ЗАДАНИЯ -----
@router.callback_query(F.data == "tasks")
async def show_tasks(callback: CallbackQuery):
    tasks = get_tasks()
    text = "📋 <b>Задания</b>\n\n" + "\n".join([f"{'✅' if is_task_completed(callback.from_user.id, t[0]) else '⬜'} {t[1]} (+{t[3]}🪙)" for t in tasks]) if tasks else "Пока нет заданий"
    await callback.message.edit_text(text, reply_markup=tasks_menu(tasks))
    await callback.answer()

@router.callback_query(F.data.startswith("task_"))
async def do_task(callback: CallbackQuery):
    task_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    if is_task_completed(user_id, task_id):
        await callback.answer("✅ Уже выполнено!", show_alert=True)
        return
    
    tasks = get_tasks()
    task = next((t for t in tasks if t[0] == task_id), None)
    if not task:
        await callback.answer("❌ Задание не найдено", show_alert=True)
        return
    
    await callback.message.edit_text(
        f"📋 <b>{task[1]}</b>\n\n{task[2]}\n💰 {task[3]} 🪙\n🔗 <a href='{task[5]}'>Перейти</a>",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton("✅ Проверить", callback_data=f"check_task_{task_id}")],
            [InlineKeyboardButton("🔙 Назад", callback_data="tasks")]
        ]),
        disable_web_page_preview=True
    )
    await callback.answer()

@router.callback_query(F.data.startswith("check_task_"))
async def check_task(callback: CallbackQuery):
    task_id = int(callback.data.split("_")[2])
    user_id = callback.from_user.id
    if is_task_completed(user_id, task_id):
        await callback.answer("✅ Уже выполнено!", show_alert=True)
        return
    
    tasks = get_tasks()
    task = next((t for t in tasks if t[0] == task_id), None)
    if not task:
        await callback.answer("❌ Ошибка", show_alert=True)
        return
    
    add_coins(user_id, task[3])
    complete_task(user_id, task_id)
    await callback.message.edit_text(f"🎉 +{task[3]} 🪙! Баланс: {get_coins(user_id)}", reply_markup=main_menu())
    await callback.answer()

# ----- РЕФЕРАЛКА -----
@router.callback_query(F.data == "referrals")
async def show_referrals(callback: CallbackQuery):
    user_id = callback.from_user.id
    username = (await bot.me()).username
    await callback.message.edit_text(
        f"👥 <b>Рефералка</b>\n\n🔗 <code>t.me/{username}?start={user_id}</code>\n👤 Приглашено: {get_referrals_count(user_id)}\n💰 Заработано: {get_referral_earnings(user_id):.0f} 🪙\n📈 %: {int(REFERRAL_PERCENT*100)}%",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("🔙 Назад", callback_data="back")]])
    )
    await callback.answer()

# ----- КЛИКЕР -----
@router.callback_query(F.data == "clicker")
async def show_clicker(callback: CallbackQuery):
    user_id = callback.from_user.id
    clicks = get_clicks_today(user_id)
    max_clicks = MAX_CLICKS_PER_DAY
    coins = get_coins(user_id)
    boost_x2 = get_boost(user_id, "boost_x2_end")
    boost_x5 = get_boost(user_id, "boost_x5_end")
    autoclicker = get_user(user_id)[7] if get_user(user_id) else 0
    
    reward = CLICK_REWARD * (5 if boost_x5 else 2 if boost_x2 else 1)
    await callback.message.edit_text(
        f"🖱️ <b>Кликер</b>\n\n🪙 {coins} монет\n📊 {clicks}/{max_clicks} кликов\n💰 +{reward:.2f} 🪙/клик\n\n⚡ x2: {'✅' if boost_x2 else '❌'}\n⚡ x5: {'✅' if boost_x5 else '❌'}\n🤖 Автокликер: {'✅' if autoclicker else '❌'}",
        reply_markup=clicker_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "click_tap")
async def click_tap(callback: CallbackQuery):
    user_id = callback.from_user.id
    clicks = get_clicks_today(user_id)
    max_clicks = MAX_CLICKS_PER_DAY
    
    if clicks >= max_clicks:
        await callback.answer("⛔ Лимит на сегодня!", show_alert=True)
        return
    
    reward = CLICK_REWARD
    if get_boost(user_id, "boost_x5_end"):
        reward *= 5
    elif get_boost(user_id, "boost_x2_end"):
        reward *= 2
    
    add_click(user_id)
    add_coins(user_id, int(reward))
    await callback.answer(f"🖱️ +{reward:.2f} 🪙!", show_alert=False)

@router.callback_query(F.data == "clicker_stats")
async def clicker_stats(callback: CallbackQuery):
    user_id = callback.from_user.id
    clicks = get_clicks_today(user_id)
    max_clicks = MAX_CLICKS_PER_DAY
    await callback.message.edit_text(
        f"📊 <b>Статистика</b>\n\n📅 {clicks}/{max_clicks} кликов\n📈 {int((clicks/max_clicks)*100)}%\n{'█'*int((clicks/max_clicks)*10)}{'░'*(10-int((clicks/max_clicks)*10))}",
        reply_markup=clicker_menu()
    )
    await callback.answer()

# ----- БУСТЫ -----
@router.callback_query(F.data.startswith("buy_"))
async def buy_boost(callback: CallbackQuery):
    user_id = callback.from_user.id
    boost_type = callback.data.split("_")[2] if len(callback.data.split("_")) > 2 else callback.data.split("_")[1]
    prices = {"x2": BOOST_X2_PRICE, "x5": BOOST_X5_PRICE, "autoclicker": AUTOCLICKER_PRICE, "unlimit": UNLIMIT_PRICE}
    price = prices.get(boost_type, 0)
    
    coins = get_coins(user_id)
    gram = (coins / 100) * COINS_TO_GRAM
    
    if gram < price:
        await callback.answer(f"❌ Нужно {price} Gram", show_alert=True)
        return
    
    cost_coins = int((price / COINS_TO_GRAM) * 100)
    add_coins(user_id, -cost_coins)
    
    if boost_type == "x2":
        set_boost(user_id, "boost_x2_end", 24)
    elif boost_type == "x5":
        set_boost(user_id, "boost_x5_end", 24)
    elif boost_type == "autoclicker":
        db.execute('UPDATE users SET autoclicker = 1 WHERE user_id = ?', (user_id,))
        db_conn.commit()
    elif boost_type == "unlimit":
        db.execute('UPDATE users SET unlimited_clicks = 5000 WHERE user_id = ?', (user_id,))
        db_conn.commit()
    
    await callback.answer("✅ Куплено!", show_alert=True)
    await show_clicker(callback)

# ----- БИРЖА -----
@router.callback_query(F.data == "exchange")
async def show_exchange(callback: CallbackQuery):
    user_id = callback.from_user.id
    coins = get_coins(user_id)
    await callback.message.edit_text(
        f"💱 <b>Биржа</b>\n\n📈 100 🪙 = {COINS_TO_GRAM} Gram\n🪙 {coins} монет\n💎 {(coins/100)*COINS_TO_GRAM:.4f} Gram\n⚙️ Комиссия: {int(EXCHANGE_FEE*100)}%\n💳 Мин. вывод: {MIN_WITHDRAW_GRAM} Gram",
        reply_markup=exchange_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "buy_coins")
async def buy_coins(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("💰 Введи сумму в Gram (например, 0.5):")
    await state.set_state(Form.buy_coins_amount)
    await callback.answer()

@router.message(Form.buy_coins_amount)
async def process_buy_coins(message: Message, state: FSMContext):
    try:
        amount = float(message.text.replace(",", "."))
        if amount <= 0:
            raise ValueError
    except:
        await message.answer("❌ Введи число > 0")
        return
    
    user_id = message.from_user.id
    coins_received = int((amount / COINS_TO_GRAM) * 100)
    fee = amount * EXCHANGE_FEE
    add_coins(user_id, coins_received)
    add_exchange_history(user_id, "buy", coins_received, amount, fee)
    
    await message.answer(f"✅ Куплено {coins_received} 🪙 за {amount:.4f} Gram (+{fee:.4f} комиссия)")
    await state.clear()

@router.callback_query(F.data == "sell_coins")
async def sell_coins(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("💸 Введи количество монет (мин. 1000):")
    await state.set_state(Form.sell_coins_amount)
    await callback.answer()

@router.message(Form.sell_coins_amount)
async def process_sell_coins(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        if amount < 1000:
            raise ValueError
    except:
        await message.answer("❌ Минимум 1000 монет")
        return
    
    user_id = message.from_user.id
    coins = get_coins(user_id)
    if coins < amount:
        await message.answer(f"❌ У тебя только {coins} 🪙")
        return
    
    gram = (amount / 100) * COINS_TO_GRAM
    fee = gram * EXCHANGE_FEE
    total = gram - fee
    add_coins(user_id, -amount)
    add_exchange_history(user_id, "sell", amount, total, fee)
    
    await message.answer(f"✅ Продано {amount} 🪙 за {total:.4f} Gram (-{fee:.4f} комиссия)")
    await state.clear()

@router.callback_query(F.data == "withdraw_gram")
async def withdraw_gram(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(f"💎 Введи сумму (мин. {MIN_WITHDRAW_GRAM} Gram):")
    await state.set_state(Form.withdraw_amount)
    await callback.answer()

@router.message(Form.withdraw_amount)
async def process_withdraw_amount(message: Message, state: FSMContext):
    try:
        amount = float(message.text.replace(",", "."))
        if amount < MIN_WITHDRAW_GRAM:
            raise ValueError
    except:
        await message.answer(f"❌ Минимум {MIN_WITHDRAW_GRAM} Gram")
        return
    
    user_id = message.from_user.id
    coins = get_coins(user_id)
    gram = (coins / 100) * COINS_TO_GRAM
    if gram < amount:
        await message.answer(f"❌ У тебя {gram:.4f} Gram")
        return
    
    await state.update_data(withdraw_amount=amount)
    await message.answer("📱 Введи адрес TON:")
    await state.set_state(Form.withdraw_address)

@router.message(Form.withdraw_address)
async def process_withdraw_address(message: Message, state: FSMContext):
    data = await state.get_data()
    amount = data.get('withdraw_amount', 0)
    user_id = message.from_user.id
    address = message.text.strip()
    
    fee = amount * EXCHANGE_FEE
    total = amount - fee
    coins_spent = int((amount / COINS_TO_GRAM) * 100)
    
    add_coins(user_id, -coins_spent)
    add_exchange_history(user_id, "withdraw", coins_spent, total, fee)
    
    await message.answer(f"💎 Заявка на {total:.4f} Gram отправлена на адрес {address[:10]}...")
    await bot.send_message(ADMIN_ID, f"💎 ВЫВОД: {message.from_user.id}\n{amount} Gram\n{address}")
    await state.clear()

@router.callback_query(F.data == "exchange_history")
async def exchange_history(callback: CallbackQuery):
    history = get_exchange_history(callback.from_user.id)
    text = "📜 <b>История</b>\n\n" + "\n".join([f"{h[2].upper()}: {h[3]} 🪙 = {h[4]:.4f} Gram" for h in history]) if history else "Пока пусто"
    await callback.message.edit_text(text, reply_markup=exchange_menu())
    await callback.answer()

# ----- АДМИНКА -----
@router.callback_query(F.data == "admin")
async def admin_panel(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    await callback.message.edit_text("⚙️ <b>Админка</b>", reply_markup=admin_menu())
    await callback.answer()

@router.callback_query(F.data == "admin_stats")
async def admin_stats(callback: CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    
    db.execute('SELECT COUNT(*) FROM users')
    total_users = db.fetchone()[0]
    db.execute('SELECT SUM(coins) FROM users')
    total_coins = db.fetchone()[0] or 0
    
    await callback.message.edit_text(
        f"📊 <b>Статистика</b>\n\n👥 Юзеров: {total_users}\n🪙 Монет: {total_coins}\n💎 Gram: {(total_coins/100)*COINS_TO_GRAM:.2f}\n📈 Активных: {get_active_today()}",
        reply_markup=admin_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "admin_mailing")
async def admin_mailing(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    await callback.message.edit_text("📢 Введи текст рассылки:")
    await state.set_state(Form.mailing_text)
    await callback.answer()

@router.message(Form.mailing_text)
async def process_mailing(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Доступ запрещен")
        return
    
    text = message.text
    db.execute('SELECT user_id FROM users')
    users = db.fetchall()
    
    sent = 0
    for user in users:
        try:
            await bot.send_message(user[0], text, parse_mode="HTML")
            sent += 1
            await asyncio.sleep(0.05)
        except:
            pass
    
    await message.answer(f"✅ Отправлено {sent} пользователям")
    await state.clear()

@router.callback_query(F.data == "admin_add_task")
async def admin_add_task(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    await callback.message.edit_text("➕ Введи название задания:")
    await state.set_state(Form.add_task_title)
    await callback.answer()

@router.message(Form.add_task_title)
async def process_task_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("📄 Введи описание:")
    await state.set_state(Form.add_task_desc)

@router.message(Form.add_task_desc)
async def process_task_desc(message: Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await message.answer("💰 Введи награду (монеты):")
    await state.set_state(Form.add_task_reward)

@router.message(Form.add_task_reward)
async def process_task_reward(message: Message, state: FSMContext):
    try:
        reward = int(message.text)
    except:
        await message.answer("❌ Введи число")
        return
    await state.update_data(reward=reward)
    await message.answer("🔗 Введи ссылку:")
    await state.set_state(Form.add_task_link)

@router.message(Form.add_task_link)
async def process_task_link(message: Message, state: FSMContext):
    data = await state.get_data()
    task_id = add_task(data['title'], data['desc'], data['reward'], "link", message.text)
    await message.answer(f"✅ Задание {task_id} добавлено!")
    await state.clear()

@router.callback_query(F.data == "admin_delete_task")
async def admin_delete_task(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    
    tasks = get_tasks()
    if not tasks:
        await callback.message.edit_text("❌ Нет заданий", reply_markup=admin_menu())
        return
    
    text = "🗑️ Введи ID задания:\n\n" + "\n".join([f"ID: {t[0]} — {t[1]}" for t in tasks])
    await callback.message.edit_text(text)
    await state.set_state(Form.delete_task_id)
    await callback.answer()

@router.message(Form.delete_task_id)
async def process_delete_task(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Доступ запрещен")
        return
    try:
        task_id = int(message.text)
        delete_task(task_id)
        await message.answer(f"✅ Задание {task_id} удалено")
    except:
        await message.answer("❌ Ошибка")
    await state.clear()

@router.callback_query(F.data == "admin_give_coins")
async def admin_give_coins(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("⛔ Доступ запрещен", show_alert=True)
        return
    await callback.message.edit_text("🎁 Введи ID пользователя:")
    await state.set_state(Form.give_coins_user)
    await callback.answer()

@router.message(Form.give_coins_user)
async def process_give_user(message: Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except:
        await message.answer("❌ Введи ID")
        return
    await state.update_data(give_user=user_id)
    await message.answer("💰 Введи количество монет:")
    await state.set_state(Form.give_coins_amount)

@router.message(Form.give_coins_amount)
async def process_give_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
    except:
        await message.answer("❌ Введи число")
        return
    data = await state.get_data()
    user_id = data['give_user']
    add_coins(user_id, amount)
    await message.answer(f"✅ {user_id} получил {amount} 🪙")
    await state.clear()

# ============================================
#  🏃 ЗАПУСК
# ============================================
async def main():
    dp.include_router(router)
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
