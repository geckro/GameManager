import pathlib
import yaml

_config_file_path = 'config/config.yml'


def _check_config():
    data_file_path = pathlib.Path(_config_file_path) if _config_file_path else None
    data_file_path.parent.mkdir(parents=True, exist_ok=True)
    if not data_file_path.exists():
        with open(data_file_path, 'w') as config_file:
            yaml.safe_dump({}, config_file)

    return True if data_file_path else False


def add_to_config(configuration, value):
    _check_config_var = _check_config()

    if not _check_config_var:
        raise ValueError(f"File does not exist!")

    with open(_config_file_path, 'r') as _config_file:
        _config_data = yaml.safe_load(_config_file)

    _config_data[configuration] = value

    with open(_config_file_path, 'w') as _config_file:
        yaml.safe_dump(_config_data, _config_file, default_flow_style=False)


def check_option(configuration: str):
    _check_config_var = _check_config()

    if not _check_config_var:
        raise ValueError(f"File does not exist!")

    with open(_config_file_path, 'r') as _config_file:
        _config_data = yaml.safe_load(_config_file)

    return _config_data[configuration] if _config_data[configuration] else False

