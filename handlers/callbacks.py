from aiogram import Router, types
from utils.api import get_words
from utils.keyboards import gwa_keyboard, control_keyboard, books_keyboard

router = Router()

user_data = {}   # foydalanuvchi uchun eslab qolish

@router.callback_query(lambda q: q.data.startswith("book:"))
async def choose_book(call: types.CallbackQuery):
    b = call.data.split(":")[1]
    user_data[call.from_user.id] = {"book": b}
    await call.message.edit_text(f"📘 *{b}* — 과 tanlang:", parse_mode="Markdown")
    await call.message.edit_reply_markup(gwa_keyboard())


@router.callback_query(lambda q: q.data.startswith("gwa:"))
async def choose_gwa(call: types.CallbackQuery):
    gwa = int(call.data.split(":")[1])
    user_data[call.from_user.id]["gwa"] = gwa

    b = user_data[call.from_user.id]["book"]
    data = await get_words(b, gwa)

    if not data or len(data["words"]) == 0:
        await call.message.edit_text("❌ So‘zlar topilmadi")
        return

    user_data[call.from_user.id]["words"] = data["words"]
    user_data[call.from_user.id]["i"] = 0

    w = data["words"][0]

    await call.message.edit_text(f"🇰🇷 *{w['kr']}*\n🇺🇿 {w['uz']}", parse_mode="Markdown")
    await call.message.edit_reply_markup(control_keyboard())


@router.callback_query(lambda q: q.data == "next")
async def next_word(call: types.CallbackQuery):
    d = user_data[call.from_user.id]
    words = d["words"]

    d["i"] = (d["i"] + 1) % len(words)
    w = words[d["i"]]

    await call.message.edit_text(f"🇰🇷 *{w['kr']}*\n🇺🇿 {w['uz']}", parse_mode="Markdown")
    await call.message.edit_reply_markup(control_keyboard())


@router.callback_query(lambda q: q.data == "back_books")
async def back_books(call: types.CallbackQuery):
    await call.message.edit_text("📘 Kitobni tanlang:")
    await call.message.edit_reply_markup(books_keyboard())


@router.callback_query(lambda q: q.data == "back_gwa")
async def back_books(call: types.CallbackQuery):
    await call.message.edit_text("과 tanlang:")
    await call.message.edit_reply_markup(gwa_keyboard())
