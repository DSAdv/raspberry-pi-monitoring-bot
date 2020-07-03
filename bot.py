import logging
import time

import utils
import messages
import config

from apscheduler.schedulers.background import BackgroundScheduler

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())


def send_weather_message():
    weather_json = utils.request_weather_information(**utils.WEATHER_COORDINATES)
    executor.start(dp, bot.send_message(config.CHANNEL_ID, messages.prepare_weather_message(weather_json)))


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_weather_message, "interval", minutes=15)
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
