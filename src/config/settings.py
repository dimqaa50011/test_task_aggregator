from typing import NamedTuple, Optional
from pathlib import Path, PurePath
import os

from dotenv import load_dotenv

from .db import MongoConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class AppSettings(NamedTuple):
    mongo: MongoConfig


def load_cofig(env_path: Optional[str] = None) -> AppSettings:
    env_path = Path(env_path).resolve() if env_path is not None else BASE_DIR / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    
    return AppSettings(
        mongo=MongoConfig(
            host=os.getenv("MONGO_HOST"),
            port=os.getenv("MONGO_PORT")
        )
    )
    

app_settings = load_cofig()
