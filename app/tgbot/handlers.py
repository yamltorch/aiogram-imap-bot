from aiogram import Router, F, types

router = Router()


@router.message(F.text)
async def add_experience(message: types.Message):
    text = message.text

    await message.answer()
