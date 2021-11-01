import os
import time

import telegram
from dotenv import load_dotenv


def send_photo_to_channel(delay, channel):
    bot = telegram.Bot(token=token)
    images = os.listdir('images/')
    while True:
        for image in images:
            img_path = os.path.join(img_dir, image)
            with open(img_path, 'rb') as p:
                photo = p.read()
            bot.send_photo(
                chat_id=channel,
                photo=photo
            )
            time.sleep(delay)


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    delay = float(os.getenv('TIME_DELAY'))
    channel = os.getenv('TG_CHANNEL')
    img_dir = 'images'

    send_photo_to_channel(delay)