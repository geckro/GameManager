def tcrf_parser(game_title):
    game_title = game_title.replace(" ", "_")
    tcrf_link = f"https://tcrf.net/{game_title}"
    return tcrf_link
