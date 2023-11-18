def steam_url_cleanup(url: str):
    if url.isdigit():
        url = f"https://store.steampowered.com/app/{url}"

    if 'http://' in url:
        url.replace('http://', 'https://', 1)

    if 'https://' not in url:
        url = f"https://{url}"

    return url


def steam_scraper(url):
    url = steam_url_cleanup(url) if url else None
