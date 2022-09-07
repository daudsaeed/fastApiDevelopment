

# from typing import Optional
# from fastapi import FastAPI, status, HTTPException
# from pydantic import BaseModel
# from random import randrange
# my_movies  = [{"id": 1, "title": "Innocent Lies (2022)", "rating": "0", "videoUrl": "https://908472281.tapecontent.net/radosgw/yrQxDWKYqJi18LB/rNfr8peDROuRg_KQ6TGlFEg9gAJ8ePaeD5oEBLBoZBp6kRg4_OtdjwzCrk3Of-tp_qxz2GKkHYaQDzlBV1rSJvtyoYvMjeVY9KeSQraGoG69GjxtDuAJhhsnjI88lyhzi93q8L-S8spc5DUWfpbX_bunO4A0pWpUoLwpncjcBWtmFZpu0SwuCRqHut1UkafBUHXiYHh4Q4HrE-RBRvpRC9rJzMOstvuqwcJayO3h_telgXM-9rWEALDSDTnQvlobt_9Zab_FXHumAF3wU8Nm0dvpEgjnANiBWiYLaQ/innocent-lies-2022-episode-11661349601.0.mp4?stream=1"},
#   {"id": 2, "title": "My Only 12% (2022)", "rating": "0", "videoUrl": "https://908471762.tapecontent.net/radosgw/Dq4Z0JwLgMCkPla/C1WkkfQ67pn5DP5sTVmbxwHoK0Yx-92PJ0skXzPcWpv8KZ3J3iJ9Wj7ZPN7dwVWNGJA0dx5REcXW4OP6LTBY3JJynP_1_GKXSmzT3PWDGCXmNTI8k_kSUu8rhm0EyrubEDqQpXRqhasSuywmBs-2SQQj_pBU0DlrHULAQctP2bJzIZBsWtz5JO7ieIg-Tqj_P36U29p3Lp4nnuOj-8MGmHs8CK1qJE69Dv3SO2b11KPYEVvpUhuFjQgKD931Hve3LJsf6G4vmOli5W25P3H33bfulrBM3zLKTbPRzQ/my-only-12-2022-episode-31661551802.0.mp4?stream=1"}
# ]

# class Post(BaseModel):
#   id: Optional[int] = None
#   title: str
#   favorite: bool = False
#   rating: Optional[int] = None
#   videoUrl: str



# # Helper Methods//////
# def findMovieById(id):
#   print("the id is"+ str(id))
#   for movie in my_movies:
#     if movie["id"] == id:
#       return movie

# def indexOfMovie(id: int):
#   i = 0
#   for movie in my_movies:
#     if movie["id"] == id:
#       return i
#     i+=1
#   return -1;


# app = FastAPI();

# @app.get("/movies")
# def getMovies():
#   return {"movies": my_movies}

# @app.post("/movies", status_code=status.HTTP_201_CREATED)
# def createMovie(post: Post):
#   new_post  = post.dict()
#   new_post["id"] = randrange(1, 1000000000000)
#   my_movies.append(new_post)
#   return {"movie": new_post}


# @app.get("/movies/{id}")
# def getMovie(id: int):
#   movie = findMovieById(id)
#   if not movie:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sorry couldnt movie the with this ID")
#   else:
#     return {"movie": movie}


# @app.delete("/movies/{id}")
# def deleteMovie(id: int):
#   idx = indexOfMovie(id)

#   if(idx == -1):
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#   else:
#     movie = my_movies[idx]
#     my_movies.pop(idx)
#     return {"movie": movie}

# @app.put("/movies/{id}")
# def updateMovie(id: int, post: Post):
#   idx = indexOfMovie(id)
#   if(idx == -1):
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#   updatedMovie = post.dict()
#   updatedMovie["id"] = id
#   my_movies[idx] = updatedMovie
#   return {"movie" : f"Succesfully updated the movie with ID {id}"}