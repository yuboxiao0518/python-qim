from fastapi import FastAPI
import routers

def create_app():
    app = FastAPI()
    app.include_router(routers.router, prefix="/dev-api/api")
    return app
