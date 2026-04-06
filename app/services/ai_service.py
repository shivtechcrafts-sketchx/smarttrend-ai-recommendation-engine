from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_videos(videos, user_interest="AI"):
    if not videos:
        return []

    titles = [v["title"] for v in videos]

    embeddings = model.encode(titles)
    ref = model.encode([user_interest + " programming tutorials"])

    scores = cosine_similarity(embeddings, ref)

    for i, v in enumerate(videos):
        score = float(scores[i])

        if user_interest.lower() in v["title"].lower():
            score += 0.3

        v["score"] = round(score, 3)

    return sorted(videos, key=lambda x: x["score"], reverse=True)