import json

from staticjinja import make_site


CONFIG = 'config.json'
TEMPLATES_PATH = 'templates'
SITE_PATH = 'site'


def load_json(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        return json.loads(json_file.read())


if __name__ == '__main__':
    config = load_json(CONFIG)
    config["index_data_page"].update(config["requests_data"])
    config["requests_data_page"].update(config["requests_data"])
    site = make_site(
        outpath=SITE_PATH,
        contexts=[
            ('index.html',
             config["index_data_page"]),
            ('requests.html',
             config["requests_data_page"])])
    site.render()
