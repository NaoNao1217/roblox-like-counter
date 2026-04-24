import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/likes")
def get_likes(place_id: int):
    # PlaceId → UniverseId を取得
    universe_api = f"https://apis.roblox.com/universes/v1/places/{place_id}/universe"
    universe_data = requests.get(universe_api).json()

    if "universeId" not in universe_data:
        return {"error": "UniverseId not found"}

    universe_id = universe_data["universeId"]

    # UniverseId から Like/Dislike を取得
    info_url = f"https://games.roblox.com/v1/games?universeIds={universe_id}"
    info_data = requests.get(info_url).json()

    if "data" not in info_data or len(info_data["data"]) == 0:
        return {"error": "Game data not found"}

    vote_data = info_data["data"][0].get("voteData")
    if vote_data is None:
        return {"error": "voteData not available"}

    return {
        "likes": vote_data.get("upVotes", 0),
        "dislikes": vote_data.get("downVotes", 0)
    }
