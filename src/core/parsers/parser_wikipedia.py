import re

from bs4 import BeautifulSoup
from wikipedia import wikipedia

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
