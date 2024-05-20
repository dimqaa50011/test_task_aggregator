from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from .settings import app_settings

client = AsyncIOMotorClient(app_settings.mongo.get_uri())
sampleDB: AsyncIOMotorDatabase = client["sampleDB"]
sample_collection: AsyncIOMotorCollection = sampleDB["sample_collection"]

