import requests
import os

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
dir_path = 'images/'
img_name = 'hubble.jpeg'
os.makedirs(dir_path, exist_ok=True)


def load_img(url, name):
    img_path = os.path.join(dir_path, name)

    response = requests.get(url)
    response.raise_for_status()

    with open(img_path, 'wb') as img:
        img.write(response.content)

    dir_content = os.listdir(dir_path)
    if name in dir_content:
        print('Image load successfully!')


if __name__ == '__main__':
    load_img(url, img_name)