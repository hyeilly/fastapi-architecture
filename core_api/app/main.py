from fastapi import FastAPI
from recommend_llm.main import router as recommend_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the core FastAPI application!123"}

@app.get("/test")
async def read_test():
    return {"message": "test"}

app.mount("/recommend-llm", recommend_router)