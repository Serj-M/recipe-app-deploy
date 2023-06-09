from fastapi import APIRouter
from app.handlers.recipes.routes import recipes_router


class HeadRouter:

    def __init__(self):
        self.router = APIRouter()
        self.router.include_router(recipes_router, prefix='/recipes/v1')
