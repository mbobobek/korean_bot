from aiogram import Router, types
from utils.keyboards import books_keyboard

router = Router()

@router.message(commands=["start"])
async def start_command(msg: types.Message):
    await msg.answer(
        "📘 *Koreys tili — Flashcards bot*\n\nKitobni tanlang:",
        reply_markup=books_keyboard(),
        parse_mode="Markdown"
    )
