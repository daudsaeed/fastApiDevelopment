from fastapi import FastAPI, status, HTTPException, Depends
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor 
from .routes import post, user, auth, votes
from fastapi.middleware.cors import CORSMiddleware


# from fastapi import pyda


while True:
  try:
    connection = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="MSCgL64843", cursor_factory=RealDictCursor)
    cursor = connection.cursor()
    print("connection Established")
    break
  except Exception as error:
    print("connection Failed")

my_movie = [
  {
    "id": 1,
    "title": "Hit the First Case",
    "description": "The film is set to be followed by a standalone sequel titled HIT: The Second \
    Case. Kolanu also helmed the Hindi remake of The First Case as same title. Both the films were released on July 2022.",
  },

  {
    "id": 2,
    "title": "Me Time",
    "description": "Me Time is a 2022 American buddy comedy film written and directed by John \
      Hamburg. The film stars Kevin Hart, Mark Wahlberg, and Regina Hall. Me Time was released on \
      August 26, 2022, by Netflix.",
  }
]


################## HELPER METHODS ###############################

def findMovieById(id:int):
  for movie in my_movie:
    if movie["id"] == id:
      return movie
  return None

def findIndexOfMovie(id:int):
  for index, movie in enumerate(my_movie):
    if movie["id"] == id:
      return index
  return -1


# models.Base.metadata.create_all(bind=engine)  



####################### INCLUDE THE ROUTER ###################
app = FastAPI();

# @app.get("/")
# def default():
#   return {"Working": "Succesfuly working "}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

app.include_router(votes.router)




