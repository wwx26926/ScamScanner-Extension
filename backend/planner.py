from apscheduler.schedulers.background import BackgroundScheduler
from news_fetcher import fetch_latest_fragments

scheduler = BackgroundScheduler()

# Placeholder update functions
def update_wikipedia_dump():
    # In real setup, download and index Wikipedia dump
    print("update_wikipedia_dump called")


def update_news():
    fetch_latest_fragments("fake news")


def start():
    scheduler.add_job(update_wikipedia_dump, "cron", hour=2)
    scheduler.add_job(update_news, "interval", hours=6)
    scheduler.start()
