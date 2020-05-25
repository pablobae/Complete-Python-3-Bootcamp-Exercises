import re
import requests
from requests.exceptions import HTTPError


def get_links(tags_a_raw):
    links = []
    for tag_link in tags_a_raw:
        href = tag_link.split('href="')
        link = href[1][:href[1].index('"')]

        if not link in links:
            links.append(link)

    return links


def get_images(tags_img_raw):
    images = []
    for tag_image in tags_img_raw:
        src = tag_image.split('src="')
        image = src[1][:src[1].index('"')]

        if not image in images:
            images.append(image)

    return images


if __name__ == '__main__':
    print('*** Web Scraper ***')

    url = input("Please enter an URL: ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'GET {url}: SUCCESS')
        decoded_content = response.content.decode()

        tag_items = {
            'link': [],
            'image': []
        }
        tag_patterns = {
            'link': {'pattern': '<a .*href="http.*"', 'processor': get_links},
            'image': {'pattern': '<img .* src=".*"', 'processor': get_images}
        }

        clean_data = {}
        for tag_key, tag_data in tag_patterns.items():
            pattern = re.compile(r'{}'.format(tag_data['pattern']))
            tag_items[tag_key] = pattern.findall(decoded_content)
            clean_data[tag_key] = tag_data['processor'](tag_items[tag_key])

            print(clean_data[tag_key])
            print(f'{tag_key}: found {len(tag_items[tag_key])}, collected {len(clean_data[tag_key])}')
            input("Press a key to continue.")
