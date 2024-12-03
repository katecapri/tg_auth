import uuid
from sqlalchemy import select, update

from src.database.models import User


class Repository:
    def __init__(self, session):
        self.session = session
        self.model_user = User

    async def get_user_by_chat_id(self, chat_id):
        query = select(self.model_user).where(self.model_user.chat_id == chat_id)
        result = await self.session.execute(query)
        return result.scalar()

    async def get_user_by_token(self, token):
        query = select(self.model_user).where(self.model_user.token == token)
        result = await self.session.execute(query)
        return result.scalar()

    async def save_user_info(self, token, user_name, chat_id):
        new_user = self.model_user(
            id=uuid.uuid4(),
            token=token,
            name=user_name,
            chat_id=chat_id,
        )
        self.session.add(new_user)
        await self.session.commit()
        return new_user.id

    async def update_user_token(self, token, chat_id):
        query = update(self.model_user).where(self.model_user.chat_id == chat_id).values(
            token=token
        )
        await self.session.execute(query)
        await self.session.commit()