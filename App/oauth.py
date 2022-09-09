from datetime import datetime, timedelta
from jose import JWTError, jwt,ExpiredSignatureError
# from .exceptions import ExpiredSignatureError
from . import schmes
from .database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from .models import User
from App.config import settings

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token (data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


def verify_token_access(token:str , credential_exception):

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    id: int  = payload.get("user_id")
    expire = payload.get("exp")
    if id is None:
      raise credential_exception
    
    token_data = schmes.tokenData(id=id, created_at=expire)
  
  except ExpiredSignatureError:
    raise HTTPException(status_code=403, detail="token has been expired")
  except JWTError:
    raise credential_exception
  return token_data



def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
  credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to authroize", headers={'WWW-Authenticate': "Bearer"})
  token_data =  verify_token_access(token, credential_exception=credential_exception)

  user = db.query(User).filter(User.id == token_data.id).first()
  return user