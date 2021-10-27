import os

import requests

dir_path = 'images/'
os.makedirs(dir_path, exist_ok=True)


def load_img(url, name):
    img_path = os.path.join(dir_path, name)

    response = requests.get(url)
    response.raise_for_status()

    with open(img_path, 'wb') as img:
        img.write(response.content)


def get_spacex_img_links():
    spacex_api = 'https://api.spacexdata.com/v3/launches/'
    # params = {
    #     'launch_year': 2021
    # }
    response = requests.get(spacex_api)
    response.raise_for_status()
    response_list = response.json()
    links = [
        doc['links']['flickr_images'] for doc in response_list if len(doc['links']['flickr_images']) > 0
    ]
    links_flat = [link for sub in links for link in sub]
    return links_flat


def fetch_spacex_last_launch(links):
    for i, link in enumerate(links):
        name = f'spacex_{i}.jpg'
        load_img(link, name)


def get_url_extension(url):
    url_split = urlsplit(url)
    path = [unquote(i) for i in url_split if '.' in i]
    extension = [os.path.split(p)[1] for p in path]
    extension = [
        ext.split('.')[1] for ext in extension
        if any([_ in ext for _ in ['txt', 'jpeg', 'png', 'gif', 'jpg']])
    ]
    return extension[0]


def get_apod_links(links_count):
    api_apod = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': 'TzRclLIAzTV0pLMYpY1XARqbGOeYA5cRHt93lmSw',
        'count': links_count,
    }
    response = requests.get(api_apod, params)
    response.raise_for_status()
    links = [res['url'] for res in response.json()]
    return links


def get_nasa_apod_images(count):
    links = get_apod_links(count)
    for i, link in enumerate(links):
        ext = get_url_extension(link)
        name = f'nasa_apod_{i}.{ext}'
        load_img(link, name)


def get_nasa_epic_links(url, date):
    nasa_epic = 'https://epic.gsfc.nasa.gov/epic-archive/jpg/'
    params = {
        'api_key': 'TzRclLIAzTV0pLMYpY1XARqbGOeYA5cRHt93lmSw',
        'date': date,
    }
    response = requests.get(url, params)
    response.raise_for_status()

    raw_links = [res['image'] for res in response.json()]
    links = [f'{nasa_epic}{link}.jpg' for link in raw_links]
    return links


def get_nasa_epic_images(url, date):
    links = get_nasa_epic_links(url, date)
    for i, link in enumerate(links):
        ext = get_url_extension(link)
        name = f'nasa_epic_{i}.{ext}'
        load_img(link, name)
