from src.core.db import write_to_database
from src.core.parsers.parser_emulators import emulator_parser
from src.core.parsers.parser_howlongtobeat import howlongtobeat_parser
from src.core.parsers.parser_retroachievements import retroachievements_parser
from src.core.parsers.parser_tcrf import tcrf_parser
from src.core.parsers.parser_wikipedia import wikipedia_parser
from src.core.time import current_time


def parser(result):
    title_2 = result.replace(" ", "_")  # Replace any spaces with an underscore
    title_3 = result.replace(" ", "%2520")
    title_4 = result.replace(" ", "+")

    # Call parsers
    time_data = current_time()
    wikipedia_data = wikipedia_parser(result)
    emulator_data = emulator_parser(wikipedia_data.get('Platform', []), result, title_2)
    tcrf_data = tcrf_parser(title_2)
    hltb_data = howlongtobeat_parser(title_3)
    ra_data = retroachievements_parser(title_4, (wikipedia_data.get('Platform', [])))

    data_dict = {
        'time': time_data,
        'wikipedia': wikipedia_data,
        'emulator': emulator_data,
        'tcrf': tcrf_data,
        'hltb': hltb_data,
        'ra': ra_data,
    }

    write_to_database(data_dict)

    return data_dict
