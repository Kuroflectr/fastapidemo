from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import api_v2.schemas.movie as movie_schema
import api_v2.cruds.movie as movie_crud
from api_v2.db import get_db

router = APIRouter()


# read 
@router.get("/movies", response_model=List[movie_schema.Movie])
def list_tasks(db: AsyncSession = Depends(get_db)):
    return movie_crud.get_movies(db)