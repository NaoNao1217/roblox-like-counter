import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/likes")
def get_likes(place_id: int):
    # PlaceID を UniverseID として扱う（あなたのゲームはこの方式）
    info_url = f"https://games.roblox.com/v1/games?universeIds={place_id}"
    info_data = requests.get(info_url).json()
    print("info_data:", info_data)

    # voteData が存在しない場合の対策
    if "data" not in info_data or len(info_data["data"]) == 0:
        return {"error": "Game data not found"}

    vote_data = info_data["data"][0].get("voteData")
    if vote_data is None:
        return {"error": "voteData not available"}

    likes = vote_data.get("upVotes", 0)
    dislikes = vote_data.get("downVotes", 0)

    return {"likes": likes, "dislikes": dislikes}
