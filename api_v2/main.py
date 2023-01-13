from fastapi import FastAPI
from api_v2.routers import movie

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}

app.include_router(movie.router)