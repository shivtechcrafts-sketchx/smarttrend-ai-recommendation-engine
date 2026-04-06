import math
from datetime import datetime

def calculate_score(engagement, created_time=None, source="unknown"):
    if engagement <= 0:
        return 0

    age_hours = 5

    if created_time:
        try:
            created = datetime.fromtimestamp(created_time)
            now = datetime.utcnow()
            age_hours = max((now - created).total_seconds() / 3600, 1)
        except:
            pass

    # 🔥 core formula
    velocity = engagement / age_hours
    score = velocity * math.log(engagement + 1)

    # 🔥 source boost
    if source == "youtube":
        score *= 1.2
    elif source == "hackernews":
        score *= 1.1

    return round(score, 2)