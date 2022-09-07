from fastapi import  Depends, HTTPException, status, APIRouter
from typing import List, Optional
from .. import models, utility, schmes, oauth
from sqlalchemy import func
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
  prefix="/movies"
)
# GET ALL THE MOVIES ####################
@router.get("/", response_model=List[schmes.PostOut])
# get_current_user: int = Depends (oauth.get_current_user),
def getMovies(db: Session = Depends(get_db),  limit: int = 10, skip:int = 0,search:Optional[str] = ""):

  # cursor.execute(""" SELECT * FROM movies""")
  # movies = cursor.fetchall();
# models.Post.user_id == get_current_user.id 

  print(search)
  # movies = db.query(models.Post).filter(models.Post.title.contains(search)).offset(skip).limit(limit).all()
  movies_result = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).filter(models.Post.title.contains(search)).join(models.Vote, models.Post.id  == models.Vote.post_id, isouter=True).group_by(models.Post.id).offset(skip).limit(limit).all() 
  print(movies_result)
  return movies_result

# CREATE A MOVIE #########################
@router.post("/", status_code=status.HTTP_201_CREATED)
def createMovie(post: schmes.createPost, db: Session = Depends(get_db), get_current_user: int = Depends(oauth.get_current_user)):
  # new_movie = post.dict()
  # new_movie["id"] = randrange(0, 20000000)
  # my_movie.append(new_movie)

  # cursor.execute(""" INSERT INTO movies (title, description, videourl) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.description, post.videoUrl))
  # new_movie = cursor.fetchone()
  # connection.commit()

  new_post = models.Post(user_id = get_current_user.id, **post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

# GET A CERTAIN MOVIE WITH CERTAIN ID ###########
@router.get("/{id}", response_model=schmes.PostOut)
# get_current_user: int = Depends(oauth.get_current_user)
def getMovie(id:int, db: Session = Depends(get_db) ):
  # movie = findMovieById(id)
  # cursor.execute(""" SELECT * FROM movies WHERE id = %s """, (str(id), ))
  # movie  = cursor.fetchone()

  # movie = db.query(models.Post).filter(models.Post.id == id).first();
  movie = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).filter(models.Post.id == id).join(models.Vote, models.Post.id  == models.Vote.post_id, isouter=True).group_by(models.Post.id).first()
  if movie == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with this id wquals {id} was not FOUND")
  # print("Current USER: " , get_current_user)
  return movie

# UPDATE THE MOVIE WITH A GIVEN ID ##############
@router.patch("/{id}")
def updateMovie(id:int, post: schmes.createPost, db: Session = Depends(get_db), get_current_user: int = Depends(oauth.get_current_user)):
  # updatedMovie = post.dict()
  # indexOfMovie = findIndexOfMovie(id)
  # cursor.execute(""" UPDATE movies SET title = %s, description = %s, videourl=%s WHERE id = %s RETURNING *""", (post.title, post.description, post.videoUrl, str(id)))
  # movie = cursor.fetchone()
  # connection.commit()


  post_query = db.query(models.Post).filter(models.Post.id == id);
  postToUpdate =  post_query.first()
  if postToUpdate == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with {id} id was found")

  if get_current_user.id != postToUpdate.user_id:
    raise HTTPException(detail="Sorry, You are unauthorize to perform the a task", status_code=status.HTTP_403_FORBIDDEN)
  # updatedMovie["id"] = id
  # my_movie[indexOfMovie] = updatedMovie

  updated_post = post.dict()
  updated_post["id"] = id;
  post_query.update(updated_post, synchronize_session=False)
  db.commit()
  return  post_query.first()


#DELETE A MOVIE GIVEN AN ID ###############
@router.delete("/{id}")
def deleteMovie(id:int, db: Session = Depends(get_db), get_current_user: int = Depends(oauth.get_current_user) ):
  # indexOfMovie = findIndexOfMovie(id)
  # cursor.execute(""" DELETE FROM movies WHERE id = %s RETURNING *""", (str(id), ))
  # deletedMovie = cursor.fetchone()
  # connection.commit()

  deletedMovie = db.query(models.Post).filter(models.Post.id == id).first()
  
  if deletedMovie == None:
    print("Movie Not deleted")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with {id} id was found")

  if get_current_user.id !=  deletedMovie.user_id:
    raise HTTPException(detail="Not authorize to perform this task", status_code=status.HTTP_403_FORBIDDEN)
  # movieToBeDeleted = my_movie[indexOfMovie]
  # my_movie.pop(indexOfMovie)
  db.delete(deletedMovie)
  db.commit()
  return deletedMovie

