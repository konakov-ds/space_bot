# Программа для размещения фото в телеграм канал

Программа позволяет автоматизировать постинг фото в телеграм канал. Добавьте в папку images
изображения, и скрипт будет публиковать их в ваш канал. Вы также можете автоматически скачать коллекцию фото с запусков
[Spacex](https://www.spacex.com/), случайные фото дня и снимки Земли от [НАСА](https://www.nasa.gov/).


###  Переменные окружения


Для начала создайте файл, в котором будут хранится переменные окружения:

```
   touch .env
```
В файле .env нужно будет прописать следующие переменные:
```
TELEGRAM_TOKEN=2082348512***C0 - токен вашего бота (можно получить через @BotFather)
```
```
TG_CHANNEL=@space_inspire - название вашего канала
```
```
TIME_DELAY=86400 - задержка публикации (в секундах)
```
```
NASA_API=TzR***cSw - токен апи для скачивания фото (https://api.nasa.gov/)
```
```
APOD_COUNT=100 - количество случайных фото дня
```
```
EPIC_DATE=2021-10-25 - получение фото Земли от этой даты
```
###  Зависимости
- Установить зависимости:

   ```
   pip install -r requirements.txt
  ```
###  Запуск скрипта
- Запустить скрипт можно командой:
  #### Запуск бота
  ```
  python main.py
  ```
  #### Запуск скачивания изображений
  ```
  python serve.py
  ```