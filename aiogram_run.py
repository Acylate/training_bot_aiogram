import asyncio

from handlers.userinfo import info_router
from create_bot import bot, dp, scheduler
from handlers.start import start_router
from create_bot import set_commands
# from work_time.time_func import send_time_msg


async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    dp.include_router(info_router)
    await set_commands()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())