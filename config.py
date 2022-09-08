from pathlib import Path
import yaml


def load_config():
    root_project_path = str(Path(__file__).parent)
    with open(f'{root_project_path}/config.yml', 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc


yml_config = load_config()

# base url
BASE_URL = f'{yml_config["base_url"]}'
CHROME_DRIVER = f'{yml_config["chrome_driver"]}'
FIREFOX_DRIVER = f'{yml_config["firefox_driver"]}'
OPERA_DRIVER = f'{yml_config["opera_driver"]}'
YANDEX_DRIVER = f'{yml_config["yandex_driver"]}'
