import aiohttp

API_URL = "https://koreanapi-production.up.railway.app"  # 🔥 Flashcards API

async def get_words(book: str, gwa: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/flashcards?book={book}&gwa={gwa}") as resp:
            if resp.status == 200:
                return await resp.json()
            return None
