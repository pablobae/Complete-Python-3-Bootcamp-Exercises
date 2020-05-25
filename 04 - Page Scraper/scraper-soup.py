import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def get_links(tags_a_raw):
    links = []
    for tag_link in tags_a_raw:
        if 'href' in tag_link.attrs:
            link = tag_link.attrs['href']
            if not link in links and link.startswith('http'):
                links.append(link)

    return links


def get_images(tags_img_raw):
    images = []
    for tag_image in tags_img_raw:
        if 'src' in tag_image.attrs:
            image = tag_image.attrs['src']
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
        soup = BeautifulSoup(response.content.decode(), "html.parser")

        tags = {
            'link': {'tag': 'a', 'processor': get_links},
            'image': {'tag': 'img', 'processor': get_images}
        }

        clean_data = {}
        for tag_key, tag_data in tags.items():
            tag_key_occurrences = soup.find_all(tag_data['tag'])
            clean_data[tag_key] = tag_data['processor'](tag_key_occurrences)

            print(clean_data[tag_key])
            print(f'{tag_key}: found {len(tag_key_occurrences)}, collected {len(clean_data[tag_key])}')
            input("Press a key to continue.")
