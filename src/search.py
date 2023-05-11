import pandas
from ui.gameview import GameView

class Search:
    def search(search_box):
        # Convert the search text to lowercase
        search_text = search_box.text().lower()
        
        # Read the CSV file into a pandas DataFrame
        df = pandas.read_csv('data/db.csv')
        
        # Create a new temporary column with lowercase values
        df['<Title_Lower>'] = df['<Title>'].str.lower()
        
        # Filter the dataFrame based on the search text
        result_df = df[df['<Title_Lower>'].str.contains(search_text)]
        
        # Drop the <Title_Lower> column from the result_df
        result_df = result_df.drop(columns=['<Title_Lower>'])
        
        # Create a new GameView window with the result_df
        game_view = GameView(result_df)
        
        # Connect the row_selected signal to the handle_row_selected function
        game_view.row_selected.connect(Search.handle_row_selected)
        
        # Show the game view table
        game_view.exec()

    def handle_row_selected(row):
        # Do something with the selected row
        print(row)

