import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, WEB_APP_URL

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    url = WEB_APP_URL or "https://example.com"
    web_app_info = types.WebAppInfo(url=url)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🚀 Открыть Proxy App", web_app=web_app_info)]
    ])
    
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы быстро подключить актуальный прокси.",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    print("🤖 Бот на aiogram 2.x успешно запущен!")
    
    # КОСТЫЛЬ ДЛЯ PYTHON 3.14+: создаем event loop вручную, чтобы старый aiogram не падал
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    executor.start_polling(dp, skip_updates=True, loop=loop)