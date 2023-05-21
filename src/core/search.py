from wikipedia import search as search_wikipedia


def search_wikipedia_results(value):
    matching_rows = search_wikipedia(value, results=4)
    return matching_rows


# For raw debugging purposes
if __name__ == "__main__":
    from src.core.parsers.parser import parser
    debug_input = "Super Mario Galaxy"
    search_results = search_wikipedia_results(debug_input)
    if search_results:
        parsed_result = parser(search_results[0])
        print(parsed_result)
    else:
        print(f"No search results found for '{debug_input}'.")
