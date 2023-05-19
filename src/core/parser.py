import json
import re
import os

import wikipedia
from bs4 import BeautifulSoup
import requests

from src.core.platform_conversion import platform_conv
from src.core.time import current_time

info_mapping = {
    'Developer(s)': 'Developer',
    'Publisher(s)': 'Publisher',
    'Director(s)': 'Director',
    'Producer(s)': 'Producer',
    'Designer(s)': 'Designer',
    'Programmer(s)': 'Programmer',
    'Artist(s)': 'Artist',
    'Writer(s)': 'Writer',
    'Composer(s)': 'Composer',
    'Engine': 'Engine',
    'Series': 'Series',
    'Platform(s)': 'Platform',
    'Release': 'Release Date',
    'Genre(s)': 'Genre',
    'Mode(s)': 'Mode'
}


def wikipedia_parser(game):
    # Get raw HTML of the game wikipedia page
    wikipedia_page = wikipedia.WikipediaPage(game).html()
    # Create a BS object from the page content
    soup = BeautifulSoup(wikipedia_page, 'html.parser')

    # Find the wikipedia infobox in the raw HTML
    wikipedia_infobox = soup.find('table', {'class': 'infobox'})

    # Initialize a dictionary to store the extracted values
    game_info = {}

    # Extract the information from the infobox
    if wikipedia_infobox:
        rows = wikipedia_infobox.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header and header.text in info_mapping:
                key = info_mapping[header.text]
                values = []
                cells = row.find_all('td')
                for cell in cells:
                    text = cell.get_text(separator=', ').strip()
                    split_values = re.split(r',\s+(?![^\[]*\])', text)
                    for value in split_values:
                        value = re.sub(r'\[.*\]', '', value).strip()
                        if value:
                            values.append(value)
                game_info[key] = values

    # Add game name to the dict
    game_info['Name'] = game

    return game_info


def emulator_parser(systems, title):
    platform = platform_conv(systems)
    title_2 = title.replace(" ", "_")  # Replace any spaces with an underscore
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


def parser(result):
    # Call parsers
    time_data = current_time()
    wikipedia_data = wikipedia_parser(result)
    emulator_data = emulator_parser(wikipedia_data.get('Platform', []), wikipedia_data.get('Name', ''))

    data_dict = {
        'time': time_data,
        'wikipedia': wikipedia_data,
        'emulator': emulator_data
    }

    if not os.path.exists('data'):
        os.makedirs('data')

    # Put all the information into a text file as cache.
    with open('data/cache.json', 'a') as cache_file:
        json.dump(data_dict, cache_file)
        cache_file.write('\n')

    return data_dict
