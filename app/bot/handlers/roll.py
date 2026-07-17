import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("roll"))
async def command_roll(message: Message) -> None:
    """Бросает число 1-100 и отвечает в зависимости от результата."""
    user_name = message.from_user.full_name
  
    num = random.randint(1, max_value) # вместо 100 значение пользователя

    parts = message.text.split()

    if len(parts) > 2: # при написании более 1 аргумента
        await message.answer("Эй, я одна не могу обработать столько всего! Один аргумент, пожалуйста...")

    if len(parts) > 1:
        if not parts[1].isdigit():
            await message.answer(f"'{parts[1]}' - это не число. Я не тупая!") # при написании текста
            return
        try:
            max_value = int(parts[1])
            if max_value < 2:
                await message.answer("Я, конечно, не такая как остальные, но все равно, дай хотя бы 2...")
                return
        except ValueError:
            await message.answer("Это не число... Ты ебушка?")
            return
    else:
        max_value = 100 # по умолчанию

    if num == 13:
        result = f"Оу {num}... Откуды ты знаешь, что у меня др в этот день!"
    elif num > max_value * 0.8:
        result = f"ОГО! {user_name}, тебе выпало {num}! Вселенная на твоей стороне!"
    elif num > max_value * 0.5:
        result = f"Неплохо, {user_name}! {num} — среднячок, как и я..?"
    elif num > max_value * 0.2:
        result = f"Всего {num}? Ну... бывало и лучше. Но я в тебя верю!"
    else:
        result = f"{num}... Это знак. Меня никто не любит. И тебя тоже, наверное... 😭"

    await message.answer(result)
