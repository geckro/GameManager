import pandas
from ui.gameview import GameView
class Search:
    def search(search_box):
        search_text = search_box.text()
        print(f"Searching for '{search_text}'...")
        df = pandas.read_csv('data/db.csv')
        result_df = df[df['<Title>'].str.contains(search_text)]
        game_view = GameView(result_df)
        game_view.row_selected.connect(Search.handle_row_selected)
        game_view.exec()
    def handle_row_selected(row):
        # Do something with the selected row
        print(row)

