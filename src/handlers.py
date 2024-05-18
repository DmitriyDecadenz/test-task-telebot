from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import src.database.requests as rq
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import src.keyboards as kb

router = Router()


class Reg(StatesGroup):
    description = State()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в трекер задач \nдобавить задачу </add> \nпосмотреть задачи </tsk>')
    await message.answer('Выберите действие', reply_markup=kb.main)



@router.message(F.text == '/tsk')
async def get_task(message: Message) -> None:
    task = await rq.get_tasks()
    for task in await rq.get_tasks():
        await message.answer(f'Задача: \n \n{task.id}. {task.description}')


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
