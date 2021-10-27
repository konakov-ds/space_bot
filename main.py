import os
import time

import telegram
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TELEGRAM_TOKEN')
delay = float(os.getenv('TIME_DELAY'))
channel = os.getenv('TG_CHANNEL')
img_dir = 'images'


def send_photo_to_channel(delay, channel=channel):
    bot = telegram.Bot(token=token)
    images = os.listdir('images/')
    i = 0
    while True:
        i = i % len(images)
        img_path = os.path.join(img_dir, images[i])
        bot.send_photo(
            chat_id=channel, photo=open(img_path, 'rb')
        )
        i += 1
        time.sleep(delay)


if __name__ == '__main__':
    send_photo_to_channel(delay)