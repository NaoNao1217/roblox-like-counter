@app.get("/likes")
def get_likes(place_id: int):
    # PlaceId → UniverseId を取得
    universe_api = f"https://apis.roblox.com/universes/v1/places/{place_id}/universe"
    universe_data = requests.get(universe_api).json()
    universe_id = universe_data["universeId"]

    # UniverseId から Like/Dislike を取得
    info_url = f"https://games.roblox.com/v1/games?universeIds={universe_id}"
    info_data = requests.get(info_url).json()

    vote_data = info_data["data"][0]["voteData"]

    return {
        "likes": vote_data["upVotes"],
        "dislikes": vote_data["downVotes"]
    }
