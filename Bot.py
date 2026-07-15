import telebot
import json
import time
import os
from telebot import types

# Используйте переменные окружения для защиты токена
TOKEN = os.getenv

ADMIN_ID = 8684827145
TON_WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps"

bot = telebot.TeleBot(TOKEN)
DB_FILE = "data.json"

# Загрузка БД
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
    rates = [0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10, 25]
    return sum(rates[i] for i in u["heroes"] if i < len(rates))

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

# --- ОСТАЛЬНОЙ КОД (обработчики команд и функций) ---
# (Оставил структуру без изменений, чтобы сохранить логику)

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.from_user.id)
    reg(uid)
    if data["users"][uid]["ban"]: return bot.send_message(message.chat.id, "⛔ Бан!")
    inc = collect(uid)
    kb = types.InlineKeyboardMarkup()
    # ЗАМЕНИТЕ ССЫЛКУ НИЖЕ НА ВАШ СЕРВЕР GITHUB PAGES
    kb.add(types.InlineKeyboardButton("🎮 Открыть Clash Farm", web_app=types.WebAppInfo(url="https://ВАШ_ЛОГИН.github.io/clash-farm/webapp.html")))
    bot.send_message(message.chat.id, f"👋 Привет!\n💰 +{inc:.1f}💎 зачислено.", reply_markup=kb)

# ... (Остальные функции: menu_cmd, bal, ref, tasks_cb и т.д. остаются как в вашем оригинале) ...

if __name__ == "__main__":
    print("✅ Бот запущен!")
    bot.infinity_polling()
