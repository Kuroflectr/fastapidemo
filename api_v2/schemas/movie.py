from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    movieid: int
    title: str = Field(default='Toy story', example='the movie title will be shown here')
    genres: str = Field(default='Animation', example='the genres of the movie will be shown here')


class MovieResponse(Movie):

    class Config:
        orm_mode =True


class MovieCreate(BaseModel): 
    movieid: int
    title: str = Field(default='Toy story', example='the movie title will be shown here')
    genres: str = Field(default='Animation', example='the genres of the movie will be shown here')
