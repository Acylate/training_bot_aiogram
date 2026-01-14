import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import BotCommand, BotCommandScopeDefault

from db_handler.db_class import PostgresHandler
from core.config import Config


async def set_commands():
    commands = [BotCommand(command='start', description='Start'),
                BotCommand(command='start_2', description='Start 2'),
                BotCommand(command='start_3', description='Start 3')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

pg_db = PostgresHandler(Config.DB_URL)
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = [int(admin_id) for admin_id in Config.ADMINS.split(',')] #list comprehension
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
bot = Bot(token=Config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

