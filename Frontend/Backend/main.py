from fastapi import FastAPI
from Backend.api.health import router as health_router
from Backend.core.config import settings

app = FastAPI(title=settings.APP_NAME)
app.include_router(health_router)
@app.get("/")
def root():
    return {
        "mesage": "Backend running",
        "app": settings.APP_NAME,
        "debug": settings.DEBUG
    }