# import time
#
# import requests
# from bs4 import BeautifulSoup
# import logging

# TODO: Make this click on a search result.
# HLTB is a dynamic website with no public API. Might need a new library

def howlongtobeat_parser(game_title):
    game_title = game_title.replace(" ", "%2520")
    url = f'https://www.howlongtobeat.com/?q={game_title}'
    # temporary return statement
    return url
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Referer': 'https://www.howlongtobeat.com/',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    # }
    # data = {
    #     'queryString': game_title,
    # }
    #
    # try:
    #     # Send HTTP GET request
    #     response = requests.post(url, headers=headers, data=data)
    #
    #     # Raise an exception for HTTP errors (4xx or 5xx)
    #     response.raise_for_status()
    #
    #     # Parse HTML from response.content
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     print(f'SOUP{soup}')
    #
    #     # Find the link from HLTB search results
    #     result_link = soup.find('a', {'title': game_title})
    #     print(f'RESULTLINK{result_link}')
    #
    #     if result_link:
    #         # return a clickable link
    #         return f"https://www.howlongtobeat.com/{result_link['href']}"
    #     else:
    #         # if it cannot find anything then do not return any link
    #         return None
    # except (requests.RequestException, ValueError) as e:
    #     logging.error(f'An error occurred: {e}')
