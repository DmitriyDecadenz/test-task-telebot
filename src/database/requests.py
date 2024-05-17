from typing import Any
from src.database.models import async_session
from src.database.models import UserModel, TaskModel
from sqlalchemy import select, insert


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(UserModel).where(UserModel.tg_id == tg_id))

        if not user:
            session.add(UserModel(tg_id=tg_id))
            await session.commit()


async def get_tasks():
    async with async_session() as session:
        tasks_query = select(TaskModel)
        result = await session.execute(tasks_query)
        return result.scalars().all()
        # return await session.scalars(select(TaskModel))


async def add_task(description: str) -> None:
    async with async_session() as session:
        task = await session.scalar(select(TaskModel).where(TaskModel.description == description))

        if not task:
            session.add(TaskModel(description=description))
            await session.commit()
