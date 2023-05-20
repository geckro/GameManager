import requests
from bs4 import BeautifulSoup

from src.core.platform_conversion import platform_conv


def dolphin_parser(title, result_dict):
    dolphin_link = f"https://wiki.dolphin-emu.org/index.php?title={title}"
    result_dict.setdefault('dolphin_link', []).append(dolphin_link)

    response = requests.get(dolphin_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the star compatibility rating
    star_rating_element = soup.find('a', {'title': lambda value: value and 'stars (Rating)' in value})
    number_of_stars = int(star_rating_element.img['alt'][5])
    result_dict.setdefault('dolphin_compatibility', []).append(number_of_stars)

    # Extract the input methods
    label_element = soup.find(lambda tag: tag.name == 'td' and tag.text.strip() == 'Input methods')
    input_methods_list = []
    if label_element:
        for input_method in label_element.find_next_sibling('td').find_all('a'):
            input_methods_list.append(input_method.text)
    result_dict.setdefault('dolphin_input_method', []).extend(input_methods_list)
    return result_dict


def rpcs3_parser(title, result_dict):
    rpcs3_link = f"https://wiki.rpcs3.net/index.php?title={title}"
    result_dict.setdefault('rpcs3_link', []).append(rpcs3_link)
    return result_dict


def pcsx2_parser(title, result_dict):
    pcsx2_link = f"https://wiki.pcsx2.net/{title}"
    result_dict.setdefault('pcsx2_link', []).append(pcsx2_link)
    return result_dict


def xenia_parser(title, result_dict):
    xenia_link = f"https://github.com/xenia-project/game-compatibility/issues?q=is%3Aissue+is%3Aopen+{title}"
    result_dict.setdefault('xenia_link', []).append(xenia_link)
    return result_dict


def emulator_parser(systems, title, title_2, title_plus):
    platforms = platform_conv(systems)
    result_dict = {}
    parser_map = {
        'gcn': dolphin_parser, 'wii': dolphin_parser,
        'ps3': rpcs3_parser,
        'ps2': pcsx2_parser,
        'x36': xenia_parser
    }

    for platform in platforms:
        if platform in parser_map:
            parser = parser_map[platform]
            if platform != 'x36':
                result = parser(title_2, result_dict)
            else:
                result = parser(title_plus, result_dict)

    if result_dict:
        return result_dict

    return None
