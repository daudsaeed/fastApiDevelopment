from fastapi  import  Depends, HTTPException, status, APIRouter
from .. import models, schmes, oauth
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter()

@router.get("/vote")
def vote(vote: schmes.Vote, db: Session() = Depends(get_db), get_current_user: int = Depends(oauth.get_current_user)):

  voteFind = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == get_current_user.id).first()

  if vote.dir == 1:
    if voteFind:
      raise HTTPException(detail="cant like the video", status_code=status.HTTP_409_CONFLICT)
    else:
      voteInsert = models.Vote(post_id = vote.post_id, user_id = get_current_user.id)
      db.add(voteInsert)
      db.commit()
      return {"vote": "Vote is liked "}
  else:
    if not voteFind:
      raise HTTPException(detail="cant dislike the video", status_code=status.HTTP_409_CONFLICT)
    else:
      db.delete(voteFind)
      db.commit()
      return {"vote": "Vote is deleted"}