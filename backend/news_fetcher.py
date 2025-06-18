import requests
from config import settings
from logger import logger

def fetch_latest_fragments(query: str, max_articles: int = 5) -> str:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": settings.newsapi_key,
        "pageSize": max_articles,
        "sortBy": "publishedAt"
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        articles = r.json().get("articles", [])
        fragments = [a.get("description") or a.get("title") or "" for a in articles]
        logger.info(f"Fetched {len(fragments)} fragments for query={query}")
        return "\n".join(fragments)
    except Exception as e:
        logger.error(f"Error fetching news: {e}")
        return ""