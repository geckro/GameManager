import requests
from bs4 import BeautifulSoup

from src.core.platform_conversion import platform_conv


def dolphin_parser(title):
    title = title.replace(" ", "_")
    dolphin_link = f"https://wiki.dolphin-emu.org/index.php?title={title}"

    response = requests.get(dolphin_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the star compatibility rating
    star_rating_element = soup.find('a', {'title': lambda value: value and 'stars (Rating)' in value})
    number_of_stars = int(star_rating_element.img['alt'][5])

    # Extract the input methods
    label_element = soup.find(lambda tag: tag.name == 'td' and tag.text.strip() == 'Input methods')
    input_methods_list = []
    if label_element:
        for input_method in label_element.find_next_sibling('td').find_all('a'):
            input_methods_list.append(input_method.text)

    return {
        'dolphin_link': dolphin_link,
        'dolphin_compatibility': number_of_stars,
        'dolphin_input_method': input_methods_list
    }


def rpcs3_parser(title):
    title = title.replace(" ", "_")
    rpcs3_link = f"https://wiki.rpcs3.net/index.php?title={title}"

    return {
        'rpcs3_link': rpcs3_link
    }


def pcsx2_parser(title):
    title = title.replace(" ", "_")
    pcsx2_link = f"https://wiki.pcsx2.net/{title}"

    return {
        'pcsx2_link': pcsx2_link
    }


def xenia_parser(title):
    title = title.replace(" ", "+").lower()
    xenia_link = f"https://github.com/xenia-project/game-compatibility/issues?q=is%3Aissue+is%3Aopen+{title}"

    return {
        'xenia_link': xenia_link
    }


def citra_parser(title):
    title = title.replace(" ", "-").lower()
    citra_link = f"https://citra-emu.org/game/{title}/"

    return {
        'citra_link': citra_link
    }


def switch_parser(title):
    title_ryujinx = title.replace(" ", "+")
    ryujinx_link = f"https://github.com/Ryujinx/Ryujinx-Games-List/issues?q=is%253Aissue+is%253Aopen+{title_ryujinx}"

    title_yuzu = title.replace(" ", "-").lower()
    yuzu_link = f"https://yuzu-emu.org/game/{title_yuzu}/"

    return {
        'ryujinx_link': ryujinx_link,
        'yuzu_link': yuzu_link
    }


def cemu_parser(title):
    title = title.replace(" ", "_")
    cemu_link = f"https://wiki.cemu.info/wiki/{title}"

    return {
        'cemu_link': cemu_link
    }


def ppsspp_parser(title):
    title = title.replace(" ", "+").lower()
    ppsspp_link = f"https://report.ppsspp.org/games?name={title}"

    return {
        'ppsspp_link': ppsspp_link
    }


def emulator_parser(systems, title):
    platforms = platform_conv(systems)
    parser_map = {
        'gcn': dolphin_parser, 'wii': dolphin_parser,
        'ps3': rpcs3_parser,
        'ps2': pcsx2_parser,
        'x36': xenia_parser,
        '3ds': citra_parser, 'n3d': citra_parser,
        'swi': switch_parser,
        'wiu': cemu_parser,
        'psp': ppsspp_parser
    }

    result_dict = {}
    for platform in platforms:
        if platform in parser_map:
            parser = parser_map[platform]
            result_dict.update(parser(title))

    return result_dict or None
