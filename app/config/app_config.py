from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    appName: str = "FastAPITemplate4Javaer"

appConfig = AppConfig()
