import telebot
import json
import time
import os
import requests
import threading

TOKEN = "8247692459:AAEvzCtjIK29dFweAcGvfH6xnC3Z6mkBG5I"
ADMIN_ID = 8684827145
TON_WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps"
CRYPTO_TOKEN = "609707:AAeIzAOOmCZj2LjlZGlVc8oYWd2t35UZ8KX"
COURSE = 100
BONUS_DAILY = 0.5
REF_BONUS = 1
MIN_WITHDRAW = 50

bot = telebot.TeleBot(TOKEN)
DB_FILE = "data.json"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"users": {}, "tasks": [], "promos": [], "invoices": {}}

def save():
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def reg(uid):
    uid = str(uid)
    if uid not in data["users"]:
        data["users"][uid] = {"bal": 0.0, "btime": 0, "ref": None, "refs": [], "tasks": [], "heroes": [0], "htime": time.time(), "hearn": 0, "ban": False}
        save()

def get_rate(uid):
    u = data["users"][uid]
    r = 0.05 if 0 in u["heroes"] else 0
    r += 0.1 if 1 in u["heroes"] else 0
    r += 0.25 if 2 in u["heroes"] else 0
    r += 0.5 if 3 in u["heroes"] else 0
    r += 1 if 4 in u["heroes"] else 0
    r += 2.5 if 5 in u["heroes"] else 0
    r += 5 if 6 in u["heroes"] else 0
    r += 10 if 7 in u["heroes"] else 0
    r += 25 if 8 in u["heroes"] else 0
    return r

def collect(uid):
    u = data["users"][uid]
    inc = get_rate(uid) * (time.time() - u["htime"]) / 3600
    if inc > 0:
        u["bal"] += inc
        u["hearn"] += inc
        u["htime"] = time.time()
        save()
    return inc

# ========== CRYPTO BOT ==========
def create_crypto_invoice(uid, amount_rub):
    url = "https://pay.crypt.bot/api/createInvoice"
    headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
    payload = {
        "asset": "TON",
        "amount": str(amount_rub),
        "description": f"Пополнение Clash Farm. ID: {uid}",
        "payload": uid,
        "allow_comments": False
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        resp = r.json()
        if resp.get("ok"):
            inv = resp["result"]
            data["invoices"][str(inv["invoice_id"])] = {"uid": uid, "amount": amount_rub}
            save()
            return inv["bot_invoice_url"], inv["invoice_id"]
    except Exception as e:
        print(f"CryptoBot error: {e}")
    return None, None

def check_crypto_payment(invoice_id):
    url = "https://pay.crypt.bot/api/getInvoices"
    headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
    params = {"invoice_ids": str(invoice_id)}
    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        resp = r.json()
        if resp.get("ok") and resp["result"]["items"]:
            inv = resp["result"]["items"][0]
            return inv["status"] == "paid"
    except:
        pass
    return False

def crypto_checker():
    """Фоновая проверка оплат каждые 10 секунд"""
    while True:
        try:
            for inv_id, inv_data in list(data["invoices"].items()):
                if check_crypto_payment(int(inv_id)):
                    uid = inv_data["uid"]
                    amount = inv_data["amount"]
                    reg(uid)
                    diamonds = amount * COURSE / 100  # 100 руб = 100💎
                    data["users"][uid]["bal"] += diamonds
                    # Реферальный бонус 5%
                    ref = data["users"][uid].get("ref")
                    if ref and ref in data["users"]:
                        data["users"][ref]["bal"] += diamonds * 0.05
                    del data["invoices"][inv_id]
                    save()
                    try:
                        bot.send_message(uid, f"✅ Пополнение зачислено!\n💰 +{diamonds:.0f}💎\n💎 Баланс: {data['users'][uid]['bal']:.1f}💎")
                    except:
                        pass
        except Exception as e:
            print(f"Checker error: {e}")
        time.sleep(10)

threading.Thread(target=crypto_checker, daemon=True).start()

# ========== БОТ ==========
hnames = ["🏹 Лучница", "👶 Гоблин", "⚔️ Рыцарь", "🐗 Кабан", "🧙 Волшебник", "🐉 Дракон", "🔮 Искра", "👸🏼 Принцесса", "🤴🏼 Король"]
hprices = [0, 100, 250, 500, 1000, 2500, 5000, 10000, 25000]
hincomes = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10, 25]

def menu():
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("💰 Баланс", "👥 Рефералы")
    kb.row("📋 Задания", "🎁 Бонус")
    kb.row("🏰 Герои", "💎 Пополнение")
    kb.row("💸 Вывод")
    return kb

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    ref = message.text.split()[1] if len(message.text.split()) > 1 else None
    reg(uid)
    if data["users"][uid]["ban"]:
        return bot.send_message(message.chat.id, "⛔ Бан!")
    inc = collect(uid)
    if ref and ref != uid and ref in data["users"]:
        if not data["users"][uid]["ref"]:
            data["users"][uid]["ref"] = ref
            data["users"][ref]["refs"].append(uid)
            save()
    bot.send_message(message.chat.id, f"👋 Добро пожаловать в Clash Farm!\n💰 +{inc:.1f}💎", reply_markup=menu())

@bot.message_handler(func=lambda m: m.text == "💰 Баланс")
def bal(message):
    uid = str(message.from_user.id)
    reg(uid)
    collect(uid)
    u = data["users"][uid]
    rate = get_rate(uid)
    txt = f"💰 Баланс: {u['bal']:.1f}💎\n⚡ Доход: +{rate}💎/ч\n\nГерои:\n"
    for h in u["heroes"]:
        txt += f"{hnames[h]} — {hincomes[h]}💎/ч\n"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(func=lambda m: m.text == "👥 Рефералы")
def refs(message):
    uid = str(message.from_user.id)
    u = data["users"][uid]
    link = f"https://t.me/{bot.get_me().username}?start={uid}"
    bot.send_message(message.chat.id, f"👥 Рефералы\n\n🔗 {link}\n👤 {len(u['refs'])} чел.\n💎 +1 за 5 заданий\n💸 +5% от пополнений")

@bot.message_handler(func=lambda m: m.text == "📋 Задания")
def tasks(message):
    uid = str(message.from_user.id)
    if not data["tasks"]:
        return bot.send_message(message.chat.id, "📭 Нет заданий")
    comp = data["users"][uid]["tasks"]
    txt = "📋 Задания:\n\n"
    kb = telebot.types.InlineKeyboardMarkup()
    for t in data["tasks"]:
        s = "✅" if t["id"] in comp else "⏳"
        txt += f"#{t['id']} {s} | {t['name']} | +{t['r']}💎\n"
        if t["id"] not in comp:
            kb.add(telebot.types.InlineKeyboardButton(f"🔗 {t['name']}", url=t['link']))
            kb.add(telebot.types.InlineKeyboardButton(f"✅ #{t['id']}", callback_data=f"c_{t['id']}"))
    bot.send_message(message.chat.id, txt, reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("c_"))
def check_task(call):
    uid = str(call.from_user.id)
    tid = int(call.data.split("_")[1])
    task = next((t for t in data["tasks"] if t["id"] == tid), None)
    if not task or tid in data["users"][uid]["tasks"]:
        return bot.answer_callback_query(call.id, "❌")
    data["users"][uid]["tasks"].append(tid)
    data["users"][uid]["bal"] += task["r"]
    ref = data["users"][uid].get("ref")
    if ref and ref in data["users"] and len(data["users"][uid]["tasks"]) == 5:
        data["users"][ref]["bal"] += 1
    save()
    bot.answer_callback_query(call.id, f"✅ +{task['r']}💎!")
    bot.send_message(call.message.chat.id, f"🎉 +{task['r']}💎 | 💰 {data['users'][uid]['bal']:.1f}💎")

@bot.message_handler(func=lambda m: m.text == "🎁 Бонус")
def bonus(message):
    uid = str(message.from_user.id)
    reg(uid)
    kb = telebot.types.InlineKeyboardMarkup()
    kb.add(telebot.types.InlineKeyboardButton("🎁 Забрать", callback_data="db"))
    kb.add(telebot.types.InlineKeyboardButton("🎫 Промокод", callback_data="ep"))
    bot.send_message(message.chat.id, "🎁 +0.5💎", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "db")
def db(call):
    uid = str(call.from_user.id)
    if time.time() - data["users"][uid]["btime"] < 86400:
        return bot.answer_callback_query(call.id, "Уже!")
    data["users"][uid]["bal"] += 0.5
    data["users"][uid]["btime"] = time.time()
    save()
    bot.answer_callback_query(call.id, "✅ +0.5💎!")

@bot.callback_query_handler(func=lambda c: c.data == "ep")
def ep(call):
    msg = bot.send_message(call.message.chat.id, "Код:")
    bot.register_next_step_handler(msg, check_promo)

def check_promo(message):
    uid = str(message.from_user.id)
    code = message.text.strip().upper()
    p = next((x for x in data["promos"] if x["code"] == code), None)
    if not p or uid in p.get("used", []) or p["uses"] == 0:
        return bot.send_message(message.chat.id, "❌")
    data["users"][uid]["bal"] += p["r"]
    p["uses"] -= 1
    p.setdefault("used", []).append(uid)
    save()
    bot.send_message(message.chat.id, f"✅ +{p['r']}💎")

@bot.message_handler(func=lambda m: m.text == "🏰 Герои")
def heroes(message):
    uid = str(message.from_user.id)
    reg(uid)
    collect(uid)
    u = data["users"][uid]
    txt = f"🏰 Герои\n⚡ +{get_rate(uid)}💎/ч\n\n"
    kb = telebot.types.InlineKeyboardMarkup()
    for i in range(9):
        if i in u["heroes"]:
            txt += f"{hnames[i]} ✅\n"
        else:
            txt += f"{hnames[i]} — {hprices[i]}💎\n"
            kb.add(telebot.types.InlineKeyboardButton(f"Купить {hnames[i]}", callback_data=f"b_{i}"))
    bot.send_message(message.chat.id, txt, reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("b_"))
def buy(call):
    uid = str(call.from_user.id)
    i = int(call.data.split("_")[1])
    u = data["users"][uid]
    if i in u["heroes"]:
        return bot.answer_callback_query(call.id, "Уже!")
    if u["bal"] < hprices[i]:
        return bot.answer_callback_query(call.id, "Мало 💎!")
    u["bal"] -= hprices[i]
    u["heroes"].append(i)
    u["htime"] = time.time()
    save()
    bot.answer_callback_query(call.id, f"✅ {hnames[i]}!")

@bot.message_handler(func=lambda m: m.text == "💎 Пополнение")
def depo(message):
    uid = str(message.from_user.id)
    kb = telebot.types.InlineKeyboardMarkup()
    kb.add(telebot.types.InlineKeyboardButton("💎 Пополнить через CryptoBot", callback_data="crypto_pay"))
    kb.add(telebot.types.InlineKeyboardButton("💼 Пополнить вручную (TON)", callback_data="manual_depo"))
    bot.send_message(message.chat.id, "💎 Выберите способ пополнения:", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "crypto_pay")
def crypto_pay(call):
    uid = str(call.from_user.id)
    msg = bot.send_message(call.message.chat.id, "Введите сумму в рублях (минимум 50₽):")
    bot.register_next_step_handler(msg, create_payment)

def create_payment(message):
    uid = str(message.from_user.id)
    try:
        amount = float(message.text.strip())
        if amount < 50:
            return bot.send_message(message.chat.id, "❌ Минимум 50₽")
    except:
        return bot.send_message(message.chat.id, "❌ Введите число")
    
    url, inv_id = create_crypto_invoice(uid, amount)
    if url:
        kb = telebot.types.InlineKeyboardMarkup()
        kb.add(telebot.types.InlineKeyboardButton("💳 Оплатить", url=url))
        bot.send_message(message.chat.id, f"💎 Счёт на {amount}₽ создан!\n\nОплатите по кнопке ниже.\nПосле оплаты 💎 зачислятся автоматически.", reply_markup=kb)
    else:
        bot.send_message(message.chat.id, "❌ Ошибка создания счёта")

@bot.callback_query_handler(func=lambda c: c.data == "manual_depo")
def manual_depo(call):
    uid = str(call.from_user.id)
    bot.send_message(call.message.chat.id, f"💼 Ручное пополнение\n\n📌 Кошелёк:\n{TON_WALLET}\n\n⚠️ В комментарии укажите ID: {uid}")

@bot.message_handler(func=lambda m: m.text == "💸 Вывод")
def wd1(message):
    uid = str(message.from_user.id)
    reg(uid)
    collect(uid)
    bal = data["users"][uid]["bal"]
    if bal < MIN_WITHDRAW:
        return bot.send_message(message.chat.id, f"❌ Мин: {MIN_WITHDRAW}💎\n💰 {bal:.1f}💎")
    msg = bot.send_message(message.chat.id, f"💸 Вывод\n💰 {bal:.1f}💎\nКурс: 100💎 = 1 TON\n\nСумма:")
    bot.register_next_step_handler(msg, wd2)

def wd2(message):
    uid = str(message.from_user.id)
    try:
        amt = float(message.text.strip())
    except:
        return bot.send_message(message.chat.id, "❌")
    if amt < MIN_WITHDRAW or amt > data["users"][uid]["bal"]:
        return bot.send_message(message.chat.id, "❌")
    fee = amt * 0.05
    ton = (amt - fee) / 100
    msg = bot.send_message(message.chat.id, f"💰 {ton:.2f} TON\nКошелёк:")
    bot.register_next_step_handler(msg, wd3, amt, ton)

def wd3(message, amt, ton):
    uid = str(message.from_user.id)
    data.setdefault("withdraws", []).append({"uid": uid, "amt": amt, "ton": ton, "wallet": message.text.strip()})
    data["users"][uid]["bal"] -= amt
    save()
    bot.send_message(message.chat.id, f"✅ {ton:.2f} TON")
    bot.send_message(ADMIN_ID, f"💸 Вывод! ID: {uid} | {ton:.2f} TON")

@bot.message_handler(commands=['admin'])
def admin(message):
    if message.from_user.id != ADMIN_ID:
        return
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📋 Задание +", "📋 Задания", "🗑 Удалить")
    kb.row("👤 Юзеры", "💸 Выводы")
    kb.row("➕ Начислить", "➖ Снять", "📢 Рассылка")
    kb.row("🎫 Промокод", "🔙 Выйти")
    bot.send_message(message.chat.id, "🔧 Админ", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "🔙 Выйти")
def ex(message):
    bot.send_message(message.chat.id, "✅", reply_markup=menu())

@bot.message_handler(func=lambda m: m.text == "📋 Задание +" and m.from_user.id == ADMIN_ID)
def at1(message):
    msg = bot.send_message(message.chat.id, "Название:")
    bot.register_next_step_handler(msg, at2)

def at2(message):
    n = message.text.strip()
    msg = bot.send_message(message.chat.id, "Ссылка:")
    bot.register_next_step_handler(msg, at3, n)

def at3(message, n):
    l = message.text.strip()
    msg = bot.send_message(message.chat.id, "Награда:")
    bot.register_next_step_handler(msg, at4, n, l)

def at4(message, n, l):
    try: r = float(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    tid = max([t["id"] for t in data["tasks"]] + [0]) + 1
    data["tasks"].append({"id": tid, "name": n, "link": l, "r": r})
    save()
    bot.send_message(message.chat.id, f"✅ #{tid}")

@bot.message_handler(func=lambda m: m.text == "📋 Задания" and m.from_user.id == ADMIN_ID)
def atasks(message):
    if not data["tasks"]: return bot.send_message(message.chat.id, "📭")
    txt = ""
    for t in data["tasks"]:
        txt += f"#{t['id']} {t['name']} +{t['r']}💎\n"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(func=lambda m: m.text == "🗑 Удалить" and m.from_user.id == ADMIN_ID)
def dt1(message):
    msg = bot.send_message(message.chat.id, "Номер:")
    bot.register_next_step_handler(msg, dt2)

def dt2(message):
    tid = int(message.text.strip())
    data["tasks"] = [t for t in data["tasks"] if t["id"] != tid]
    save()
    bot.send_message(message.chat.id, "✅")

@bot.message_handler(func=lambda m: m.text == "👤 Юзеры" and m.from_user.id == ADMIN_ID)
def au(message):
    txt = f"👥 {len(data['users'])}\n\n"
    for uid, u in list(data["users"].items())[:20]:
        txt += f"{uid} | 💎{u['bal']:.1f}\n"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(func=lambda m: m.text == "💸 Выводы" and m.from_user.id == ADMIN_ID)
def aw(message):
    reqs = data.get("withdraws", [])
    if not reqs: return bot.send_message(message.chat.id, "📭")
    txt = ""
    for r in reqs:
        txt += f"{r['uid']} | {r['amt']}💎 → {r['ton']:.2f} TON\n"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(func=lambda m: m.text == "➕ Начислить" and m.from_user.id == ADMIN_ID)
def ab1(message):
    msg = bot.send_message(message.chat.id, "ID СУММА")
    bot.register_next_step_handler(msg, ab2)

def ab2(message):
    try:
        p = message.text.split()
        uid, amt = str(p[0]), float(p[1])
        reg(uid)
        data["users"][uid]["bal"] += amt
        save()
        bot.send_message(message.chat.id, "✅")
    except:
        bot.send_message(message.chat.id, "❌")

@bot.message_handler(func=lambda m: m.text == "➖ Снять" and m.from_user.id == ADMIN_ID)
def rb1(message):
    msg = bot.send_message(message.chat.id, "ID СУММА")
    bot.register_next_step_handler(msg, rb2)

def rb2(message):
    try:
        p = message.text.split()
        uid, amt = str(p[0]), float(p[1])
        reg(uid)
        data["users"][uid]["bal"] = max(0, data["users"][uid]["bal"] - amt)
        save()
        bot.send_message(message.chat.id, "✅")
    except:
        bot.send_message(message.chat.id, "❌")

@bot.message_handler(func=lambda m: m.text == "📢 Рассылка" and m.from_user.id == ADMIN_ID)
def br1(message):
    msg = bot.send_message(message.chat.id, "Текст:")
    bot.register_next_step_handler(msg, br2)

def br2(message):
    c = 0
    for uid in data["users"]:
        try:
            bot.send_message(uid, message.text)
            c += 1
        except:
            pass
    bot.send_message(message.chat.id, f"✅ {c}")

@bot.message_handler(func=lambda m: m.text == "🎫 Промокод" and m.from_user.id == ADMIN_ID)
def pr1(message):
    msg = bot.send_message(message.chat.id, "Код:")
    bot.register_next_step_handler(msg, pr2)

def pr2(message):
    code = message.text.strip().upper()
    msg = bot.send_message(message.chat.id, "Награда:")
    bot.register_next_step_handler(msg, pr3, code)

def pr3(message, code):
    try: r = float(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    msg = bot.send_message(message.chat.id, "Активаций:")
    bot.register_next_step_handler(msg, pr4, code, r)

def pr4(message, code, r):
    try: u = int(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    data["promos"].append({"code": code, "r": r, "uses": u if u > 0 else 999999, "used": []})
    save()
    bot.send_message(message.chat.id, f"✅ {code}")

print("✅ Бот запущен с CryptoBot!")
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print(f"❌ {e}")
        time.sleep(5)
