# src/app/core/db.py
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

log = logging.getLogger("robust.db")

client: AsyncIOMotorClient | None = None
db = None

def connect():
    global client, db
    uri = settings.MONGO_URI
    if not uri:
        log.warning("MONGO_URI not set; DB operations will be skipped.")
        return
    client = AsyncIOMotorClient(uri)
    dbname = uri.rsplit("/", 1)[-1] or "robustdb"
    db = client[dbname]
    log.info("Connected to MongoDB", extra={"uri": uri, "db": dbname})

def close():
    global client
    if client:
        client.close()
        log.info("MongoDB connection closed")
