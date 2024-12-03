import logging
from aiogram import types, Router
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from src.tg_bot.filters.chat_types import ChatTypeFilter

from src.database.repository import Repository

logger = logging.getLogger('app')
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    try:
        repository = Repository(session)
        token = message.text.split()[1]
        chat_id = message.chat.id
        user_name = message.from_user.first_name
        existing_user_with_token = await repository.get_user_by_token(token)
        if existing_user_with_token:
            await message.reply("Вы успешно авторизованы.")
            return
        existing_user_by_chat_id = await repository.get_user_by_chat_id(chat_id)
        if existing_user_by_chat_id:
            await message.reply("Вы успешно авторизованы.")
            await repository.update_user_token(token, chat_id)
            return
        await repository.save_user_info(token, user_name, chat_id)
        await message.reply("Вы успешно авторизованы.")
    except Exception as e:
        logger.error(e, exc_info=True)
