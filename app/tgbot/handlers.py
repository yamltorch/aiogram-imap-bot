from aiogram import Router, F, types
from app import EmailCodeManager

router = Router()


@router.message(F.text)
async def get_code(message: types.Message):
    manager = EmailCodeManager()
    text = message.text
    email, vinted_code = manager.get_email_code(text)
    text_answer = (f'{email} \n\n '
                   f'Code:   `{vinted_code}`')
    await message.answer(text_answer, parse_mode='Markdown')
