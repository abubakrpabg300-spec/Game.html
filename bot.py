# ==================== ЗАПУСК ====================
import logging
import sys

# Включаем логирование, чтобы видеть ошибки, если бот не отвечает
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

dp.include_router(router)

async def main():
    print("🚀 Тоникс запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
