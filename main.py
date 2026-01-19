from fastapi import FastAPI
from app.api.route import user_routers
from app.logging import setup_logger

setup_logger()

app = FastAPI(
    title="User Management API",
    description="An API for managing users, built with FastAPI.",
    version="1.0.0",
)

# /api 접두사와 함께 라우터를 포함시킵니다.
app.include_router(user_routers.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API"}
