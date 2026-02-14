
from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    db_port:int
    db_host:str
    db_user:str
    db_password:str
    db_name:str

    model_config = SettingsConfigDict(
        from_attributes=True,
        env_file= ".env",                                                                                                 
        case_sensitive=False
    )

settings = Settings()