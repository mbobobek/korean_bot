from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

WEBAPP_URL = "https://korean-web-pied.vercel.app"   # 🔥 SENING WEBAPP LINKING

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🇰🇷 Flashcards ochish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )
