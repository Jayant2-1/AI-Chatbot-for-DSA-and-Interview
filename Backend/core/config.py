from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "AI CSE Tutor"
    DEBUG: bool = True



settings = Settings() 