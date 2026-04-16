from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Proof of Energy API"
    app_version: str = "0.1.0"
    app_description: str = "Backend API for Proof of Energy (PoE)."
    api_prefix: str = "/api"


settings = Settings()
