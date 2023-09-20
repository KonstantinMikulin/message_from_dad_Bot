import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
# TODO: Code user_handlers.py
from handlers import user_handlers, other_handlers
# TODO: Code keyboards.py
from keyboards import keyboards

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s'
                        )
    logger.info('Starting bot')
    
    config: Config = load_config('C:/Users/user/PycharmProjects/message_from_dad_Bot/.env')

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
