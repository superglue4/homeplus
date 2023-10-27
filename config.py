from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    dev: int = Field(alias='DEV')
    img_url: str = Field(alias='IMG_URL')
    db: str = Field(alias='DB')
    model_config = SettingsConfigDict(env_file='./.env')


# print(Settings().model_dump())
