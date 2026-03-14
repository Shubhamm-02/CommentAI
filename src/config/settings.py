import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file explicitly from the project root
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    # Instagram config
    IG_USERNAME: str = os.getenv("IG_USERNAME", "")
    IG_PASSWORD: str = os.getenv("IG_PASSWORD", "")
    
    # LinkedIn config
    LI_USERNAME: str = os.getenv("LI_USERNAME", "")
    LI_PASSWORD: str = os.getenv("LI_PASSWORD", "")
    
    # LLM config
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "llama3:8b")
    
    # Bot settings
    DB_PATH: str = os.getenv("DB_PATH", "data/agent_history.sqlite")
    MAX_COMMENTS_PER_DAY: int = int(os.getenv("MAX_COMMENTS_PER_DAY", 20))
    DELAY_MIN_SECONDS: int = int(os.getenv("DELAY_MIN_SECONDS", 300))
    DELAY_MAX_SECONDS: int = int(os.getenv("DELAY_MAX_SECONDS", 1800))
    
    # System
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

settings = Settings()
