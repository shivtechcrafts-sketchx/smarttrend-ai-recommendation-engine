import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def fetch_hackernews():
    try:
        ids = requests.get(f"{BASE_URL}/topstories.json").json()

        posts = []

        for story_id in ids[:5]:
            data = requests.get(f"{BASE_URL}/item/{story_id}.json").json()

            posts.append({
                "title": data.get("title"),
                "source": "hackernews",
                "engagement": data.get("score", 0),
                "url": data.get("url", "")
            })

        return posts

    except Exception as e:
        print("HN Error:", e)
        return []