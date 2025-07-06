import os

class Settings:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/qa-mongo-db")
    MONGO_DB = os.getenv("MONGO_DB", "qa-mongo-db")

settings = Settings()
