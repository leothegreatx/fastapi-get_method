from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.core.config import settings

# Define the Item class outside the function
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @_app.get("/")
    async def read_root():
        return {"message": "Hello, World!"}

    @_app.post("/items/")
    async def create_item(item: Item):
        return item

    return _app

app = get_application()

