from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result


# create (post)
async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
    ) -> task_model.Task:
    """ create a task, fill it into the db table (AsyncSession)

    Args:
        db (AsyncSession): data base session
        task_create (task_schema.TaskCreate): Request body; input by the user. 

    Returns:
        task_model.Task: a information that showing that the process is succesuful.
    """

    task = task_model.Task(**task_create.dict())
    db.add(task)

    # commit the input content into the database table
    await db.commit()
    # DB上のデータを元にTaskインスタンス task を更新する（この場合、作成したレコードの id を取得する）
    await db.refresh(task)
    return task


# read (get)
async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()



# update (put)
async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    """get the result according the input id 

    Args:
        db (AsyncSession): data base session
        task_id (int): primary id of the task 

    Returns:
        Optional[task_model.Task]: _description_
    """

    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()
    return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    """ update the task

    Args:
        db (AsyncSession): data base session
        task_create (task_schema.TaskCreate): Request body
        original (task_model.Task): result get from "get_task" function

    Returns:
        task_model.Task: _description_
    """

    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


# delete (delete)
async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    """delete the task

    Args:
        db (AsyncSession): data base session
        original (task_model.Task): result get from "get_task" function
    """
    await db.delete(original)
    await db.commit()