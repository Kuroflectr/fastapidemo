from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model


async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
    """get the done flag of the task

    Args:
        db (AsyncSession): data base session
        task_id (int): primary id of the task 

    Returns:
        Optional[task_model.Done]: Done
    """
    result: Result = await db.execute(
        select(task_model.Done).filter(task_model.Done.id == task_id)
    )
    done: Optional[Tuple[task_model.Done]] = result.first()
    return done[0] if done is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
    """change the done into True by specifying the task_id 

    Args:
        db (AsyncSession): data base session
        task_id (int): primary id of the task 

    Returns:
        task_model.Done: _description_
    """
    done = task_model.Done(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done


async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
    """denoting done into false 

    Args:
        db (AsyncSession): data base session
        original (task_model.Done): data base session
    """
    await db.delete(original)
    await db.commit()