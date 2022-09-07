from pydantic import BaseSettings

class Settings(BaseSettings):
  database_hostname:str
  database_port:str
  database_password:str
  database_name:str
  database_username:str
  # database_url:str
 

  class Config:
    env_file = ".env"

settings = Settings()


# class Token_Settings(BaseSettings):
#   secret_key:str
#   alogrithm:str
#   access_token_expire_minutes:int

# token_settings = Token_Settings()