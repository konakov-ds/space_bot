import os
from urllib.parse import urlsplit, unquote

import requests
from dotenv import load_dotenv


def load_img(url, name, dir_path):

    img_path = os.path.join(dir_path, name)

    response = requests.get(url)
    response.raise_for_status()

    with open(img_path, 'wb') as img:
        img.write(response.content)


def get_spacex_img_links():
    spacex_api = 'https://api.spacexdata.com/v3/launches/'

    response = requests.get(spacex_api)
    response.raise_for_status()
    response = response.json()

    links = [
        doc['links']['flickr_images'] for doc in response if doc['links']['flickr_images']
    ]
    img_links = [link for sub in links for link in sub]
    return img_links


def fetch_spacex_launches_images(dir_path):
    links = get_spacex_img_links()
    for img_num, link in enumerate(links):
        ext = get_url_extension(link)
        name = f'spacex_{img_num}.{ext}'
        load_img(link, name, dir_path)


def get_url_extension(url):
    url_split = urlsplit(url)
    path = unquote(url_split.path)
    extension = os.path.splitext(path)[1]
    return extension


def get_apod_links(links_count, nasa_api_token):
    api_apod = 'https://api.nasa.gov/planetary/apod/'
    params = {
        'api_key': nasa_api_token,
        'count': links_count,
    }
    response = requests.get(api_apod, params)
    response.raise_for_status()
    links = [res.get('url') for res in response.json()]
    return links


def fetch_nasa_apod_images(count, nasa_api_token, dir_path):
    links = get_apod_links(count, nasa_api_token)
    for img_num, link in enumerate(links):
        ext = get_url_extension(link)
        name = f'nasa_apod_{img_num}{ext}'
        load_img(link, name, dir_path)


def get_nasa_epic_links(date):
    url = 'https://epic.gsfc.nasa.gov/api/natural'
    nasa_epic = 'https://epic.gsfc.nasa.gov/epic-archive/jpg/'
    params = {
        'date': date,
    }
    response = requests.get(url, params)
    response.raise_for_status()

    raw_links = [res['image'] for res in response.json()]
    links = [f'{nasa_epic}{link}.jpg' for link in raw_links]
    return links


def fetch_nasa_epic_images(date, dir_path):
    links = get_nasa_epic_links(date)
    for img_num, link in enumerate(links):
        ext = get_url_extension(link)
        name = f'nasa_epic_{img_num}{ext}'
        load_img(link, name, dir_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_token = os.getenv('NASA_API')
    apod_count = os.getenv('APOD_COUNT')
    epic_date = os.getenv('EPIC_DATE')
    dir_path = 'images'

    os.makedirs(dir_path, exist_ok=True)
    fetch_spacex_launches_images(dir_path)
    fetch_nasa_apod_images(apod_count, nasa_api_token, dir_path)
    fetch_nasa_epic_images(epic_date, dir_path)
