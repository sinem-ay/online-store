from fastapi import FastAPI

from api.api import router

app = FastAPI()

app.include_router(router)