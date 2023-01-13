from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import api_v2.schemas.movie as movie_schema
# import api.cruds.task as task_crud
# from api.db import get_db

router = APIRouter()


# read 
@router.get("/movies", response_model=List[movie_schema.Movie])
async def list_movies():
    pass