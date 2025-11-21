from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from utils.keyboards import main_menu

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Salom! Quyidagi tugma orqali Korean Bot web-appni oching:",
        reply_markup=main_menu()
    )


@router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("Yaratuvchi: Murodov Bobobek")
