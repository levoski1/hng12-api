from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()
@app.get("/")
def get_root():
    # Preapare the response data
    response = {
        "email": "levibliss2000@gmail.com",
        "current_datetime":  datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/levoski1/hng12-api",
    }
    return response