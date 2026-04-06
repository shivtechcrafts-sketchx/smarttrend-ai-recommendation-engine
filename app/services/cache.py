import time

cache = {"data": None, "time": 0}
CACHE_DURATION = 300  # 5 min

def get_cache():
    if time.time() - cache["time"] < CACHE_DURATION:
        return cache["data"]
    return None

def set_cache(data):
    cache["data"] = data
    cache["time"] = time.time()