from re import sub, split

from bs4 import BeautifulSoup
from wikipedia import wikipedia

info_mapping = {
    'Developer(s)': 'developers',
    'Publisher(s)': 'publishers',
    'Director(s)': 'directors',
    'Producer(s)': 'producers',
    'Designer(s)': 'designers',
    'Programmer(s)': 'programmers',
    'Artist(s)': 'artists',
    'Writer(s)': 'writers',
    'Composer(s)': 'composers',
    'Engine': 'engine',
    'Series': 'series',
    'Platform(s)': 'platforms',
    'Release': 'dates',
    'Genre(s)': 'genres',
    'Mode(s)': 'modes'
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
        # Find all table rows in the infobox
        rows = wikipedia_infobox.find_all('tr')
        for row in rows:
            # Find the table header in the row
            header = row.find('th')
            # If header exists and its text is in info_mapping
            if header and header.text in info_mapping:
                # Get corresponding key from info_mapping
                key = info_mapping[header.text]
                values = []
                cells = row.find_all('td')
                for cell in cells:
                    # Get the text content of the cell, separated by ', '
                    text = cell.get_text(separator=', ').strip()
                    # Split the text values based on a regex pattern
                    split_values = split(r',\s+(?![^\[]*])', text)
                    # Iterate over each split value
                    for value in split_values:
                        # Remove [a/b/c], and strip any  whitespace
                        value = sub(r'\[.*?\]', '', value).strip()
                        # If value is not empty, add it to the values list
                        if value:
                            values.append(value)
                # Assign the list of values to the corresponding key
                game_info[key] = values

    # Add game name to the dict
    game_info['title'] = game

    return game_info
