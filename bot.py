import asyncio
import json
import sqlite3
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "8837313825:AAF5OrrUYh9WmhhASmZqLY8m0ntgzk9SUJo"
ADMIN_ID = 8684827145

# ЗАМЕНИ ЭТУ ССЫЛКУ НА СВОЮ (ПОСЛЕ ТОГО КАК ВКЛЮЧИШЬ GITHUB PAGES)
WEB_APP_URL = "https://твой-юзер.github.io/rich-clicker/"

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        created_at TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER,
        type TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()
    print("✅ База данных готова")

def get_balance(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def update_balance(user_id, amount):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE id = ?", (user_id,))
    if c.fetchone():
        c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
    else:
        c.execute("INSERT INTO users (id, balance, created_at) VALUES (?, ?, ?)",
            (user_id, amount, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return get_balance(user_id)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🪙 Открыть игру",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ])
    await message.answer(
        "🐹 RICH CLICKER\n\n"
        "💰 Нажимай на монету и зарабатывай RICH!\n"
        "👤 В профиле смотри баланс и ID\n\n"
        "👇 Нажми кнопку ниже!",
        reply_markup=kb
    )

@dp.message(F.web_app_data)
async def handle_web_app_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        action = data.get('action')
        user_id = data.get('userId')
        
        if action == 'tap':
            balance = update_balance(user_id, 1)
            await message.answer(json.dumps({"balance": balance}))
        
        elif action == 'getBalance':
            balance = get_balance(user_id)
            await message.answer(json.dumps({"balance": balance}))
            
    except Exception as e:
        await message.answer("❌ Ошибка: " + str(e))

async def main():
    init_db()
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
