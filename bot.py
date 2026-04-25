    import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8761013730:AAGAyz1GAjHKlm9LS_K9rSUVUaudxW8CZXA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

RICK_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я твой первый бот!\n\n"
        "Вот что я умею:\n"
        "/rick - получить СЕКРЕТНОЕ видео 🎵\n"
        "/start - показать это сообщение\n\n"
        "Или просто напиши мне что-нибудь, и я повторю!"
    )

@dp.message(Command("rick"))
async def cmd_rick(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎬 НАЖМИ МЕНЯ (осторожно, залипательно)", url=RICK_URL)],
        [InlineKeyboardButton(text="🎵 Никогда не дам тебе сдаться", url=RICK_URL)]
    ])
    
    await message.answer(
        "🎶 *ВНИМАНИЕ!* 🎶\n\n"
        "Вас ожидает:\n"
        "✓ Легендарный хит 80-х\n"
        "✓ Бесконечный плейлист похожих треков\n"
        "✓ Гарантированное послевкусие на весь день\n\n"
        "*Нажми на кнопку ниже... если готов* 😈",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты сказал: {message.text}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен... Отправь /rick в Telegram и наслаждайся реакцией!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())