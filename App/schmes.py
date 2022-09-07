
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint
class Post(BaseModel):
  id: Optional[int] = None
  title: str
  # description: str
  content: str
  # videoUrl: str
  # isFavorite : Optional[bool] = False
  published : Optional[bool] = True
  created_at: Optional[str] = datetime.now()
  
class returnUser(BaseModel):
  email: EmailStr
  id: int
  created_at: datetime

  class Config:
    orm_mode = True


class createPost(Post):
  pass

class postRequest(BaseModel):
  id:int
  title: str
  # description: str
  content: str
  user_id: int

  user: returnUser
  class Config:
    orm_mode = True


class createUser(BaseModel):
  email: EmailStr
  password: str





#Pydantic model of user login

class userLogin(BaseModel):
  email: EmailStr
  password: str




class token(BaseModel):
  acces_token: str
  token_type: str



class tokenData(BaseModel):
  id: Optional[int] = None
  created_at: datetime

class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)

class PostOut(BaseModel):
  Post: postRequest
  Votes: int