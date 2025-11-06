from fastapi import FastAPI, Request
from .routers import recipes
from .database import Base, engine
from fastapi.responses import JSONResponse

app = FastAPI()

# DB のテーブル作成
Base.metadata.create_all(bind=engine)

app.include_router(recipes.router)

# ✅ すでにある API 以外の全てを 404 にする
@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={"message": "Not Found"}
    )