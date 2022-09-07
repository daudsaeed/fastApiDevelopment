
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from .. import models, schmes, utility , oauth
from ..database import get_db


router = APIRouter(
  tags=["Authentication"]
)

@router.post("/login", response_model=schmes.token)
def login(userCredentials: OAuth2PasswordRequestForm  = Depends(), db: Session = Depends(get_db)):

  find_user = db.query(models.User).filter(models.User.email == userCredentials.username).first()

  if not find_user:
    raise HTTPException(detail="User with this email is not found", status_code=status.HTTP_403_FORBIDDEN)
  
  if not utility.passwordVerification(userCredentials.password , find_user.password):
    raise HTTPException(detail="Password doesnt match", status_code=status.HTTP_403_FORBIDDEN)

  acces_token = oauth.create_access_token(data={"user_id": find_user.id})
  return { "acces_token": acces_token, "token_type": "bearer" }



