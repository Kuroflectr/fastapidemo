from sqlalchemy.ext.asyncio import AsyncSession

import api_v2.models.movie as movie_model
import api_v2.schemas.movie as movie_schema

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



# create (post)
def create_movies(
        db: AsyncSession, movie_create: movie_schema.MovieCreate
    ) :

    movie = movie_model.Movie(**movie_create.dict())
    db.add(movie)

    # commit the input content into the database table
    db.commit()
    # DB上のデータを元にTaskインスタンス task を更新する（この場合、作成したレコードの id を取得する）
    db.refresh(movie)
    return movie


