import requests
from bs4 import BeautifulSoup

from src.core.platform_conversion import platform_conv


def emulator_parser(systems, title, title_2):
    platform = platform_conv(systems)

    result_dict = {}  # Initialize an empty dictionary to store the results

    # Dolphin Emulator
    if 'gcn' in platform or 'wii' in platform:
        dolphin_link = f"https://wiki.dolphin-emu.org/index.php?title={title_2}"
        result_dict['Dolphin Link'] = dolphin_link  # Store the Dolphin link in the dictionary

        response = requests.get(dolphin_link)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the star compatibility rating
        star_rating_element = soup.find('a', {'title': lambda value: value and 'stars (Rating)' in value})
        number_of_stars = int(star_rating_element.img['alt'][5])
        result_dict['Compatibility'] = number_of_stars

        # Extract the input methods
        label_element = soup.find(lambda tag: tag.name == 'td' and tag.text.strip() == 'Input methods')
        input_methods_list = []
        if label_element:
            for input_method in label_element.find_next_sibling('td').find_all('a'):
                input_methods_list.append(input_method.text)
        result_dict['Input Methods'] = input_methods_list

        return result_dict
