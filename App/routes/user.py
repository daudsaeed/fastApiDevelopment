
from fastapi import  status, HTTPException, Depends, APIRouter
from .. import models, schmes, utility
from sqlalchemy.orm import Session
from ..database import get_db
################################## USER AUTHENTICATION ##################################

router = APIRouter(
  prefix="/user"
)

@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schmes.returnUser)
def createUser(usr: schmes.createUser,  db: Session = Depends(get_db)):
  hasedPassword = utility.hashPassword(usr.password)
  usr.password = hasedPassword
  new_user = models.User(**usr.dict())

  # if(status.HTTP_500_INTERNAL_SERVER_ERROR):
  #   raise HTTPException(detail="Cant create a new user", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


#Get user by id 
@router.get("/{id}", response_model=schmes.returnUser)
def getUserById(id:int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).first()

  if user == None:
    raise HTTPException(detail="Couldnt find the user with this id", status_code=status.HTTP_404_NOT_FOUND)
  
  return user