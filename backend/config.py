from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    newsapi_key: str
    local_model: str = "gpt2-medium"
    max_length: int = 512
    temperature: float = 0.7
    rag_keywords: list[str] = ["dziś", "wczoraj", "ostatnio"]
    cache_ttl: int = 3600

    class Config:
        env_file = ".env"

settings = Settings()