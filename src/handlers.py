from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import src.database.requests as rq
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Reg(StatesGroup):
    description = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в трекер задач \n добавить задачу </add> \n посмотреть задачи </task>')


@router.message(F.text == '/task')
async def get_task(message: Message) -> None:
    task = await rq.get_tasks()
    task_list = []
    for tasks in task:
        task_list.append(tasks.description)
    await message.answer(f'список задач \n{task_list}')


@router.message(F.text == '/add')
async def add_task(message: Message, state: FSMContext) -> None:
    await state.set_state(Reg.description)
    await message.answer('Введите задачу')


@router.message(Reg.description)
async def add_tasks_two(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    data = await state.get_data()
    await rq.add_task(data["description"])
    await state.clear()