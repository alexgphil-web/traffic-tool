from fastapi import FastAPI
from traffic import calculate_traffic
from scraper import get_keywords

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS fix (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/traffic")
def get_traffic(domain: str):
    keywords = get_keywords(domain)
    traffic = calculate_traffic(keywords)

    return {
        "domain": domain,
        "estimated_traffic": traffic,
        "keywords": keywords[:5]
    }