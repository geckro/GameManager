from wikipedia import search as wikisearch


def search(value):
    matching_row = wikisearch(value, results=4)
    return matching_row


# Uncomment if debugging
if __name__ == "__main__":
    from src.core.parser import parser
    debug_input = "Super Mario Galaxy"
    search_results = search(debug_input)
    if search_results:
        parsed_result = parser(search_results[0])
        print(parsed_result)
    else:
        print("No search results found.")
