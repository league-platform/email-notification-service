from fastapi import FastAPI
from app.routes import router
import motor.motor_asyncio
from app.config import settings

app = FastAPI(
    title="Email Notification Service",
    description="Handles sending transactional emails based on events.",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
    app.database = app.mongodb_client[settings.MONGO_DB]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(router)
