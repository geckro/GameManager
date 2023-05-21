from src.core.db import write_to_database
from src.core.parsers.parser_emulators import emulator_parser
from src.core.parsers.parser_howlongtobeat import howlongtobeat_parser
from src.core.parsers.parser_retroachievements import retroachievements_parser
from src.core.parsers.parser_tcrf import tcrf_parser
from src.core.parsers.parser_wikipedia import wikipedia_parser
from src.core.time import current_time


def parser(game_title):
    # Call parsers
    time_data = current_time()

    wikipedia_data = wikipedia_parser(game_title)
    platforms = wikipedia_data.get('platforms', [])

    emulator_data = emulator_parser(platforms, game_title)
    tcrf_data = tcrf_parser(game_title)
    hltb_data = howlongtobeat_parser(game_title)
    ra_data = retroachievements_parser(game_title, platforms)

    data_dict = {
        'time': time_data,
        'wikipedia': wikipedia_data,
        'emulator': emulator_data,
        'tcrf': tcrf_data,
        'hltb': hltb_data,
        'ra': ra_data,
    }

    # Writes the finished parser results to "data/db.json"
    write_to_database(data_dict)

    return data_dict
