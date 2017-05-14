import json

from staticjinja import make_site


CONFIG = 'config.json'
SITE_PATH = 'site'


def load_json(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    config = load_json(CONFIG)
    updated_index = {**config["index_data_page"], **config["requests_data"]}
    updated_requests_data = {**config["requests_data_page"], **config["requests_data"]}
    site = make_site(
        outpath=SITE_PATH,
        contexts=[
            ('index.html',
             updated_index),
            ('requests.html',
             updated_requests_data)])
    site.render()
