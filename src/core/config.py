import pathlib
import yaml

_settings_path = 'config/config.yml'


def _check_config():
    data_file_path = pathlib.Path(_settings_path) if _settings_path else None
    data_file_path.parent.mkdir(parents=True, exist_ok=True)

    return True if data_file_path else False


def add_to_config(configuration, value):
    # _check_config_var = _check_config()
    # if _check_config_var:
    #     with open(_settings_path, 'r') as config:
    #         yaml.safe_load(config)
    pass


def check_option(configuration: str):
    # _check_config_var = _check_config()
    return True
