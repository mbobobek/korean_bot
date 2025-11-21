import importlib

def load_words(book: str, gwa: int):
    try:
        # misol: bot.data.book_1A.gwa1
        module_path = f"bot.data.book_{book}.gwa{gwa}"
        module = importlib.import_module(module_path)
        return module.WORDS
    except Exception as e:
        print("Error loading module:", e)
        return []
