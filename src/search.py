import pandas

class Search:
    def search(search_box):
        search_text = search_box.text()
        print(f"Searching for '{search_text}'...")
        df = pandas.read_csv('data/db.csv')
        result_df = df[df['Title'].str.contains(search_text)]
        print(result_df)

