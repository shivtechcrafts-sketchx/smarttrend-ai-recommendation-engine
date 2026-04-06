import requests, os
from dotenv import load_dotenv
from app.services.ai_service import rank_videos
from app.services.cache import get_cache, set_cache

load_dotenv()
YT_API_KEY = os.getenv("YT_API_KEY")


def detect_category(title):
    title = title.lower()

    if any(w in title for w in ["ai", "machine learning"]):
        return "AI"
    elif any(w in title for w in ["react", "web", "javascript"]):
        return "Web"
    elif any(w in title for w in ["docker", "devops", "kubernetes"]):
        return "DevOps"
    return "Other"


def get_real_trends(user_interest="AI", search=""):
    
    cached = get_cache()
    if cached:
        return cached

    query = search if search else "programming python ai web devops"

    url = "https://youtube.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "maxResults": 10,
        "type": "video",
        "key": YT_API_KEY
    }

    res = requests.get(url).json()

    items = res.get("items", [])

    if not items:
        return [{
            "title": "⚠️ No data from YouTube API",
            "url": "#",
            "category": "Error",
            "score": 0
        }]

    data = []

    for item in items:
        title = item["snippet"]["title"]
        vid = item["id"]["videoId"]

        data.append({
            "title": title,
            "url": f"https://youtube.com/watch?v={vid}",
            "category": detect_category(title)
        })

    if user_interest != "All":
        data = [d for d in data if d["category"] == user_interest] or data

    ranked = rank_videos(data, user_interest)

    set_cache(ranked)
    return ranked