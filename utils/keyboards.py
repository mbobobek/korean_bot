from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

WEBAPP_URL = "https://korean-web-pied.vercel.app"  # Web app URL


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="Korean Botni ochish",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )
