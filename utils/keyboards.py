from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def books_keyboard():
    kb = InlineKeyboardMarkup()
    for b in ["1A", "1B", "2A", "2B"]:
        kb.add(InlineKeyboardButton(text=b, callback_data=f"book:{b}"))
    return kb

def gwa_keyboard():
    kb = InlineKeyboardMarkup()
    for i in range(1, 9):
        kb.add(InlineKeyboardButton(text=f"{i}과", callback_data=f"gwa:{i}"))
    kb.add(InlineKeyboardButton(text="⬅ Ortga", callback_data="back_books"))
    return kb

def control_keyboard():
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton(text="➡ Keyingi", callback_data="next"),
        InlineKeyboardButton(text="🔊 Ovoz", callback_data="tts")
    )
    kb.add(InlineKeyboardButton(text="⬅ Ortga", callback_data="back_gwa"))
    return kb
