import aiohttp
from utils.config import API_BASE

async def get_words(book: str, gwa: int):
    url = f"{API_BASE}/flashcards?book={book}&gwa={gwa}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status != 200:
                return None
            return await res.json()
