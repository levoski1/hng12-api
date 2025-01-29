from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from typing import Dict

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", response_model=Dict[str, str], status_code=200)
def get_root():
    """
    Root endpoint that returns JSON response with email, current datetime (UTC ISO 8601), and GitHub URL.
    """
    response = {
        "email": "levibliss2000@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/levoski1/hng12-api",
    }
    return response
