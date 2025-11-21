from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo
from utils.keyboards import main_menu

router = Router()

@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Salom! Quyidagi tugma orqali Koreys Flashcards web-appni oching:",
        reply_markup=main_menu()
    )
