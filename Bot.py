import telebot
import json
import time
import os
from telebot import types

TOKEN = "8247692459:AAEvzCtjIK29dFweAcGvfH6xnC3Z6mkBG5I"
ADMIN_ID = 8684827145
TON_WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps"

bot = telebot.TeleBot(TOKEN)
DB_FILE = "data.json"

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"users": {}, "tasks": [], "promos": [], "withdraws": [], "deposits": []}

def save():
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

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

hnames = ["🏹 Лучница", "👶 Гоблин", "⚔️ Рыцарь", "🐗 Кабан", "🧙 Волшебник", "🐉 Дракон", "🔮 Искра", "👸🏼 Принцесса", "🤴🏼 Король"]
hprices = [0, 100, 250, 500, 1000, 2500, 5000, 10000, 25000]
hincomes = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10, 25]

# WebApp дизайн
WEBAPP_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clash Farm</title>
    <style>
        body { font-family: Arial; background: #1a1a2e; color: white; padding: 10px; margin: 0; }
        .header { text-align: center; padding: 15px; background: #16213e; border-radius: 10px; margin-bottom: 10px; }
        .card { background: #0f3460; padding: 15px; border-radius: 10px; margin: 8px 0; }
        .btn { background: #e94560; color: white; border: none; padding: 12px; border-radius: 8px; width: 100%; font-size: 16px; margin: 5px 0; }
        .hero { display: flex; align-items: center; gap: 10px; padding: 10px; }
        .hero img { width: 50px; height: 50px; border-radius: 10px; }
        .balance { font-size: 32px; font-weight: bold; color: #f5c518; }
        .row { display: flex; gap: 10px; }
        .col { flex: 1; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏰 Clash Farm</h1>
        <div class="balance">💎 <span id="balance">0</span></div>
    </div>
    <div id="content"></div>
    <script>
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
        
        let userData = {};
        
        function loadMain() {
            document.getElementById('content').innerHTML = `
                <div class="row">
                    <div class="col"><button class="btn" onclick="showHeroes()">🏰 Герои</button></div>
                    <div class="col"><button class="btn" onclick="showTasks()">📋 Задания</button></div>
                </div>
                <div class="row">
                    <div class="col"><button class="btn" onclick="showRefs()">👥 Рефералы</button></div>
                    <div class="col"><button class="btn" onclick="showBonus()">🎁 Бонус</button></div>
                </div>
                <div class="row">
                    <div class="col"><button class="btn" onclick="showDepo()">💎 Пополнение</button></div>
                    <div class="col"><button class="btn" onclick="showWithdraw()">💸 Вывод</button></div>
                </div>
            `;
        }
        
        function showHeroes() {
            tg.sendData(JSON.stringify({action: "heroes"}));
        }
        
        function showTasks() {
            tg.sendData(JSON.stringify({action: "tasks"}));
        }
        
        function showRefs() {
            tg.sendData(JSON.stringify({action: "refs"}));
        }
        
        function showBonus() {
            tg.sendData(JSON.stringify({action: "bonus"}));
        }
        
        function showDepo() {
            tg.sendData(JSON.stringify({action: "depo"}));
        }
        
        function showWithdraw() {
            tg.sendData(JSON.stringify({action: "withdraw"}));
        }
        
        loadMain();
    </script>
</body>
</html>
"""

# ===== БОТ =====
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
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🎮 Открыть Clash Farm", web_app=types.WebAppInfo(url="https://YOUR_USERNAME.github.io/clash-farm/webapp.html")))
    bot.send_message(message.chat.id, f"👋 Добро пожаловать!\n💰 +{inc:.1f}💎", reply_markup=kb)

@bot.message_handler(commands=['menu'])
def menu_cmd(message):
    uid = str(message.from_user.id)
    reg(uid)
    collect(uid)
    u = data["users"][uid]
    rate = get_rate(uid)
    txt = f"💰 Баланс: {u['bal']:.1f}💎\n⚡ Доход: +{rate}💎/ч\n\n"
    txt += "Твои герои:\n"
    for h in u["heroes"]:
        txt += f"{hnames[h]} — {hincomes[h]}💎/ч\n"
    
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("💰 Баланс", callback_data="bal"),
        types.InlineKeyboardButton("👥 Рефералы", callback_data="ref"),
        types.InlineKeyboardButton("📋 Задания", callback_data="tasks"),
        types.InlineKeyboardButton("🎁 Бонус", callback_data="bonus"),
        types.InlineKeyboardButton("🏰 Герои", callback_data="heroes"),
        types.InlineKeyboardButton("💎 Пополнение", callback_data="depo"),
        types.InlineKeyboardButton("💸 Вывод", callback_data="wd"),
    )
    bot.send_message(message.chat.id, txt, reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "bal")
def bal(call):
    uid = str(call.from_user.id)
    reg(uid)
    collect(uid)
    u = data["users"][uid]
    rate = get_rate(uid)
    txt = f"💰 Баланс: {u['bal']:.1f}💎\n⚡ Доход: +{rate}💎/ч\n\nГерои:\n"
    for h in u["heroes"]:
        txt += f"{hnames[h]} — {hincomes[h]}💎/ч\n"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "ref")
def ref(call):
    uid = str(call.from_user.id)
    u = data["users"][uid]
    link = f"https://t.me/{bot.get_me().username}?start={uid}"
    txt = f"👥 Рефералы\n\n🔗 {link}\n👤 {len(u['refs'])} чел.\n💎 +1 за 5 заданий"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "tasks")
def tasks_cb(call):
    uid = str(call.from_user.id)
    if not data["tasks"]:
        bot.answer_callback_query(call.id, "Нет заданий")
        return bot.send_message(call.message.chat.id, "📭 Нет заданий")
    comp = data["users"][uid]["tasks"]
    txt = "📋 Задания:\n\n"
    kb = types.InlineKeyboardMarkup()
    for t in data["tasks"]:
        s = "✅" if t["id"] in comp else "⏳"
        txt += f"#{t['id']} {s} | {t['name']} | +{t['r']}💎\n"
        if t["id"] not in comp:
            kb.add(types.InlineKeyboardButton(f"🔗 {t['name']}", url=t['link']))
            kb.add(types.InlineKeyboardButton(f"✅ Проверить #{t['id']}", callback_data=f"c_{t['id']}"))
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, txt, reply_markup=kb)

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

@bot.callback_query_handler(func=lambda c: c.data == "bonus")
def bonus_cb(call):
    uid = str(call.from_user.id)
    reg(uid)
    if time.time() - data["users"][uid]["btime"] < 86400:
        bot.answer_callback_query(call.id, "Уже получен!")
    else:
        data["users"][uid]["bal"] += 0.5
        data["users"][uid]["btime"] = time.time()
        save()
        bot.answer_callback_query(call.id, "✅ +0.5💎!")
    bot.send_message(call.message.chat.id, f"💰 Баланс: {data['users'][uid]['bal']:.1f}💎")

@bot.callback_query_handler(func=lambda c: c.data == "heroes")
def heroes_cb(call):
    uid = str(call.from_user.id)
    reg(uid)
    collect(uid)
    u = data["users"][uid]
    txt = f"🏰 Герои\n⚡ Доход: +{get_rate(uid)}💎/ч\n\n"
    kb = types.InlineKeyboardMarkup()
    for i in range(9):
        if i in u["heroes"]:
            txt += f"{hnames[i]} ✅\n"
        else:
            txt += f"{hnames[i]} — {hprices[i]}💎\n"
            kb.add(types.InlineKeyboardButton(f"Купить {hnames[i]}", callback_data=f"b_{i}"))
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, txt, reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("b_"))
def buy(call):
    uid = str(call.from_user.id)
    i = int(call.data.split("_")[1])
    u = data["users"][uid]
    if i in u["heroes"]:
        return bot.answer_callback_query(call.id, "Уже куплен!")
    if u["bal"] < hprices[i]:
        return bot.answer_callback_query(call.id, "Мало 💎!", show_alert=True)
    u["bal"] -= hprices[i]
    u["heroes"].append(i)
    u["htime"] = time.time()
    save()
    bot.answer_callback_query(call.id, f"✅ {hnames[i]}!")
    bot.send_message(call.message.chat.id, f"🎉 {hnames[i]} куплен! +{hincomes[i]}💎/ч")

@bot.callback_query_handler(func=lambda c: c.data == "depo")
def depo_cb(call):
    uid = str(call.from_user.id)
    txt = f"💎 Пополнение\n\n📌 1 TON = 100💎\n📌 Кошелёк:\n{TON_WALLET}\n\n⚠️ В комментарии укажите ID: {uid}"
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("💎 Я оплатил", callback_data="dp"))
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, txt, reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "dp")
def dp(call):
    msg = bot.send_message(call.message.chat.id, "Введи сумму TON:")
    bot.register_next_step_handler(msg, dp2, call.from_user.id)

def dp2(message, uid):
    uid = str(uid)
    try:
        ton = float(message.text.strip())
    except:
        return bot.send_message(message.chat.id, "❌")
    ref = data["users"][uid].get("ref")
    if ref and ref in data["users"]:
        data["users"][ref]["bal"] += ton * 5
    data.setdefault("deposits", []).append({"uid": uid, "ton": ton})
    save()
    bot.send_message(message.chat.id, "✅ Заявка отправлена!")
    bot.send_message(ADMIN_ID, f"💎 Пополнение! ID: {uid} | {ton} TON")

@bot.callback_query_handler(func=lambda c: c.data == "wd")
def wd_cb(call):
    uid = str(call.from_user.id)
    reg(uid)
    collect(uid)
    bal = data["users"][uid]["bal"]
    if bal < 50:
        bot.answer_callback_query(call.id, f"Мин: 50💎")
        return bot.send_message(call.message.chat.id, f"❌ Мин: 50💎\n💰 {bal:.1f}💎")
    bot.answer_callback_query(call.id)
    msg = bot.send_message(call.message.chat.id, f"💰 Баланс: {bal:.1f}💎\nВведите сумму:")
    bot.register_next_step_handler(msg, wd2)

def wd2(message):
    uid = str(message.from_user.id)
    try:
        amt = float(message.text.strip())
    except:
        return bot.send_message(message.chat.id, "❌")
    if amt < 50 or amt > data["users"][uid]["bal"]:
        return bot.send_message(message.chat.id, "❌")
    fee = amt * 0.05
    ton = (amt - fee) / 100
    msg = bot.send_message(message.chat.id, f"💰 {ton:.2f} TON\nКошелёк:")
    bot.register_next_step_handler(msg, wd3, amt, ton)

def wd3(message, amt, ton):
    uid = str(message.from_user.id)
    wallet = message.text.strip()
    data.setdefault("withdraws", []).append({"uid": uid, "amt": amt, "ton": ton, "wallet": wallet})
    data["users"][uid]["bal"] -= amt
    save()
    bot.send_message(message.chat.id, f"✅ {ton:.2f} TON")
    bot.send_message(ADMIN_ID, f"💸 Вывод! ID: {uid} | {ton:.2f} TON\n{wallet}")

@bot.message_handler(commands=['admin'])
def admin_cmd(message):
    if message.from_user.id != ADMIN_ID:
        return
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("📋 +Задание", callback_data="a_add"),
        types.InlineKeyboardButton("📋 Задания", callback_data="a_tasks"),
        types.InlineKeyboardButton("🗑 Удалить", callback_data="a_del"),
        types.InlineKeyboardButton("👤 Юзеры", callback_data="a_users"),
        types.InlineKeyboardButton("💸 Выводы", callback_data="a_wd"),
        types.InlineKeyboardButton("💎 Пополнения", callback_data="a_dep"),
        types.InlineKeyboardButton("➕ Начислить", callback_data="a_addb"),
        types.InlineKeyboardButton("➖ Снять", callback_data="a_remb"),
        types.InlineKeyboardButton("📢 Рассылка", callback_data="a_broad"),
        types.InlineKeyboardButton("🎫 Промокод", callback_data="a_promo"),
    )
    bot.send_message(message.chat.id, "🔧 Админ-панель", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "a_add")
def a_add(call):
    if call.from_user.id != ADMIN_ID: return
    msg = bot.send_message(call.message.chat.id, "Название:")
    bot.register_next_step_handler(msg, a_add2)

def a_add2(message):
    n = message.text.strip()
    msg = bot.send_message(message.chat.id, "Ссылка:")
    bot.register_next_step_handler(msg, a_add3, n)

def a_add3(message, n):
    l = message.text.strip()
    msg = bot.send_message(message.chat.id, "Награда:")
    bot.register_next_step_handler(msg, a_add4, n, l)

def a_add4(message, n, l):
    try: r = float(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    tid = max([t["id"] for t in data["tasks"]] + [0]) + 1
    data["tasks"].append({"id": tid, "name": n, "link": l, "r": r})
    save()
    bot.send_message(message.chat.id, f"✅ #{tid}")

@bot.callback_query_handler(func=lambda c: c.data == "a_tasks")
def a_tasks(call):
    if not data["tasks"]: return bot.send_message(call.message.chat.id, "📭")
    txt = ""
    for t in data["tasks"]:
        txt += f"#{t['id']} {t['name']} +{t['r']}💎\n"
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "a_del")
def a_del(call):
    msg = bot.send_message(call.message.chat.id, "Номер:")
    bot.register_next_step_handler(msg, a_del2)

def a_del2(message):
    tid = int(message.text.strip())
    data["tasks"] = [t for t in data["tasks"] if t["id"] != tid]
    save()
    bot.send_message(message.chat.id, "✅")

@bot.callback_query_handler(func=lambda c: c.data == "a_users")
def a_users(call):
    txt = f"👥 {len(data['users'])}\n\n"
    for uid, u in list(data["users"].items())[:20]:
        txt += f"{uid} | 💎{u['bal']:.1f}\n"
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "a_wd")
def a_wd(call):
    reqs = data.get("withdraws", [])
    if not reqs: return bot.send_message(call.message.chat.id, "📭")
    txt = ""
    for r in reqs:
        txt += f"{r['uid']} | {r['amt']}💎 → {r['ton']:.2f} TON\n"
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "a_dep")
def a_dep(call):
    reqs = data.get("deposits", [])
    if not reqs: return bot.send_message(call.message.chat.id, "📭")
    txt = ""
    for r in reqs:
        txt += f"{r['uid']} | {r['ton']} TON\n"
    bot.send_message(call.message.chat.id, txt)

@bot.callback_query_handler(func=lambda c: c.data == "a_addb")
def a_addb(call):
    msg = bot.send_message(call.message.chat.id, "ID СУММА")
    bot.register_next_step_handler(msg, a_addb2)

def a_addb2(message):
    try:
        p = message.text.split()
        uid, amt = str(p[0]), float(p[1])
        reg(uid)
        data["users"][uid]["bal"] += amt
        save()
        bot.send_message(message.chat.id, "✅")
    except:
        bot.send_message(message.chat.id, "❌")

@bot.callback_query_handler(func=lambda c: c.data == "a_remb")
def a_remb(call):
    msg = bot.send_message(call.message.chat.id, "ID СУММА")
    bot.register_next_step_handler(msg, a_remb2)

def a_remb2(message):
    try:
        p = message.text.split()
        uid, amt = str(p[0]), float(p[1])
        reg(uid)
        data["users"][uid]["bal"] = max(0, data["users"][uid]["bal"] - amt)
        save()
        bot.send_message(message.chat.id, "✅")
    except:
        bot.send_message(message.chat.id, "❌")

@bot.callback_query_handler(func=lambda c: c.data == "a_broad")
def a_broad(call):
    msg = bot.send_message(call.message.chat.id, "Текст:")
    bot.register_next_step_handler(msg, a_broad2)

def a_broad2(message):
    c = 0
    for uid in data["users"]:
        try:
            bot.send_message(uid, message.text)
            c += 1
        except:
            pass
    bot.send_message(message.chat.id, f"✅ {c}")

@bot.callback_query_handler(func=lambda c: c.data == "a_promo")
def a_promo(call):
    msg = bot.send_message(call.message.chat.id, "Код:")
    bot.register_next_step_handler(msg, a_promo2)

def a_promo2(message):
    code = message.text.strip().upper()
    msg = bot.send_message(message.chat.id, "Награда:")
    bot.register_next_step_handler(msg, a_promo3, code)

def a_promo3(message, code):
    try: r = float(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    msg = bot.send_message(message.chat.id, "Активаций:")
    bot.register_next_step_handler(msg, a_promo4, code, r)

def a_promo4(message, code, r):
    try: u = int(message.text.strip())
    except: return bot.send_message(message.chat.id, "❌")
    data["promos"].append({"code": code, "r": r, "uses": u if u > 0 else 999999, "used": []})
    save()
    bot.send_message(message.chat.id, f"✅ {code}")

print("✅ Бот запущен!")
while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print(f"❌ {e}")
        time.sleep(5)
