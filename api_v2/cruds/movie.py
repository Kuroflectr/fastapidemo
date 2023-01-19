from sqlalchemy.ext.asyncio import AsyncSession

import api_v2.models.movie as movie_model
# import api_v2.schemas.movie as movie_schema

from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result


# read (get)
def get_movies(db: AsyncSession) -> List[Tuple[int, str, str]]:
    result: Result =  (
        db.execute(
            select(
                movie_model.Movie.movieid,
                movie_model.Movie.title,
                movie_model.Movie.genres,
            )
        )
    )
    return result.all()
