from src.core.platform_conversion import platform_conv


def retroachievements_parser(game_title, platform_list):
    game_title = game_title.replace(" ", "+")
    shortened_platforms = platform_conv(platform_list)

    # Ordered as shows on The RetroAchievements "Games" tab
    ra_platform_list = ('gby', 'gbc', 'gba', 'nes', 'sfc', 'stv', 'n64', '64d', 'nds', 'dsi', 'pkm', 'vby', 'ps1', 'ps2', 'psp', 'a26', 'a78', 'jag', 'lyx', 't16', 'tcd', 'p88', 'pfx', 'sg1', 'sms', 'sgg', 'gen', 'scd', '32x', 'sat', 'sdc', '3do', 'acp', 'ap2', 'arc', 'ard', 'col', 'fcf', 'int', 'mo2', 'mgd', 'msx', 'ngp', 'npc', 'vec', 'wa4', 'wsv', 'wsn')

    if any(platform in shortened_platforms for platform in ra_platform_list):
        retroachievements_link = f"https://retroachievements.org/searchresults.php?s={game_title}"
        return retroachievements_link
    else:
        return None
