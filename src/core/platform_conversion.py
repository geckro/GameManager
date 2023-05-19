platform_mapping = {'3DO Interactive Multiplayer': '3do', '3DO': '3do', 'Acorn Archimedes': 'ros', 'Amiga 1200': 'am12', 'Amiga CDTV': 'acdtv', 'Amiga': 'ami', 'Amstrad CPC': 'acpc', 'Android': 'and', 'Apple II': 'ap2', 'Apple IIGS': 'ap2gs', 'Apple TV': 'aptv', 'Arcade': 'arc', 'arcade': 'arc', 'Archimedes': 'ros', 'Atari 8-bit': 'a8b', 'Atari 2600': 'a26', 'Atari 5200': 'a52', 'Atari 7800': 'a78', 'Atari Jaguar': 'jag', 'Atari Lynx': 'lynx', 'Atari ST': 'ast', 'BBC Micro': 'bbc', 'BREW': 'brew', 'CD32': 'cd32', 'Classic Mac OS': 'mac', 'Coleco Mini-Arcade': 'cma', 'ColecoVision': 'col', 'Commodore 64': 'c64', 'DESQview': 'dqv', 'DOS': 'dos', 'Electron': 'ael', 'EPOC32': 'e32', 'Famicom/NES': 'nes', 'FM Towns': 'fmt', 'FM-7': 'fm7', 'Game & Watch': 'gaw', 'Game Boy Advance': 'gba', 'Game Boy Color': 'gbc', 'Game Boy': 'gb', 'Game Gear': 'sgg', 'GameCube': 'gcn', 'Google Stadia': 'gsta', 'IBM PC': 'ibmpc', 'Intellivision': 'int', 'iOS': 'ios', 'iQue Player': 'ique', 'IRIX': 'irix', 'J2ME': 'j2me', 'Jaguar': 'jag', 'Java ME': 'jme', 'Linux': 'lin', 'Mac OS': 'mac', 'Macintosh': 'mac', 'macOS': 'mac', 'Master System': 'sms', 'Mega Drive': 'gen', 'Microsoft Windows': 'win', 'MS-DOS': 'dos', 'MSX': 'msx', 'Neo Geo CD': 'ngcd', 'Neo Geo Pocket Color': 'ngpc', 'Neo Geo Pocket': 'ngp', 'Neo Geo': 'ng', 'NES': 'nes', 'NeXTSTEP': 'ntsp', 'Nintendo 64': 'n64', 'Nintendo e-Reader': 'ner', 'Nintendo Entertainment System': 'nes', 'Nintendo Switch': 'swi', 'Nvidia Shield TV': 'nstv', 'OLPC XO-1': 'olpc', 'OS X': 'mac', 'OS/2': 'os2', 'PC Engine CD-ROM²': 'tgcd', 'PC Engine Super CD-ROM²': 'tgscd', 'PC-88': 'pc88', 'PC-98': 'pc98', 'Philips CD-i,': 'cdi', 'PlayStation 2': 'ps1', 'PlayStation 3': 'ps3', 'PlayStation 4': 'ps4', 'PlayStation 5': 'ps5', 'PlayStation Portable': 'psp', 'PlayStation Vita': 'psv', 'PlayStation': 'ps1', 'RISC OS': 'ros', 'SAM Coupé': 'cou', 'Sega 32X': '32x', 'Sega CD': 'scd', 'Sega Saturn': 'sat', 'Sharp X68000': 'x68', 'SNES': 'snes', 'Solaris': 'sol', 'Super NES': 'snes', 'Super Nintendo Entertainment System': 'snes', 'TI-99/4A': 'ti994', 'Unix': 'lin', 'VIC-20': 'v20', 'Wii U': 'wiiu', 'Wii': 'wii', 'Windows': 'win', 'WonderSwan': 'ws', 'Xbox 360': 'x36', 'Xbox One': 'xb1', 'ZX Spectrum': 'zxs'}


def platform_conv(systems):
    shortened_platforms = []

    for platform in systems:
        if platform in platform_mapping:
            shortened_platform = platform_mapping[platform]
            shortened_platforms.append(shortened_platform)
        else:
            shortened_platforms.append(platform)

    return shortened_platforms
