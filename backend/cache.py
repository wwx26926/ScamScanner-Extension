from cachetools import TTLCache

# Cache 1000 pozycji, TTL = 3600s (1h)
cache = TTLCache(maxsize=1000, ttl=3600)