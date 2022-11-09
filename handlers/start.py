from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.fsm.context import FSMContext
from keyboards.henerator import generate
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import chars
import random

router = Router()  # [1]


class lengthOfPass(StatesGroup):
    otvet = State()


@router.message(commands=["start"])  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Приветствую в нашем генераторе паролей, введите /pass что бы сгенерировать пароль",
        reply_markup=generate()
    )


@router.message(commands=["pass"])
async def cmd_dialog(message: Message, state: FSMContext):
    await message.answer("Введите длину пароля",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(lengthOfPass.otvet)


@router.message(lengthOfPass.otvet)
async def food_size_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer("Вот ваши пароли")
    length = message.text
    for n in range(3):
        password = ''
        for i in range(int(length)):
            password += random.choice(chars)
        await message.answer(password)
    await state.clear()
