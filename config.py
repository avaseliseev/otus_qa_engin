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

# urls
BASE_URL = f'{yml_config["urls"]["base_url"]}'
URL_ADMIN_PAGE = '/admin'
URL_REGISTR_PAGE = '/index.php?route=account/register'
URL_CARD_PRODUCT = '/desktops/mac/imac'
URL_DESKTOP_PAGE = '/desktops'

# drivers
CHROME_DRIVER = f'{yml_config["driver"]["chrome_driver"]}'
FIREFOX_DRIVER = f'{yml_config["driver"]["firefox_driver"]}'
OPERA_DRIVER = f'{yml_config["driver"]["opera_driver"]}'
YANDEX_DRIVER = f'{yml_config["driver"]["yandex_driver"]}'

# user
LOGIN = f'{yml_config["user"]["login"]}'
PASSWORD = f'{yml_config["user"]["password"]}'
TELEPHONE = int(f'{yml_config["user"]["telephone"]}')
EMAIL = f'{yml_config["user"]["email"]}'
