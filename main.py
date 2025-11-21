import sys
import os

# bot/ papkasini ko‘ra olishi uchun parent dir qo‘shamiz
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_words

app = FastAPI(title="Korean Flashcards API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend ishlayapti", "version": "1.0"}

@app.get("/api/flashcards")
def get_flashcards(book: str, gwa: int):
    words = load_words(book, gwa)
    return {
        "book": book,
        "gwa": gwa,
        "count": len(words),
        "words": words
    }
