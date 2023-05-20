import json
import os


def write_to_database(data_dict):
    if not os.path.exists('data'):
        os.makedirs('data')

    db_file_path = 'data/db.json'

    if os.path.isfile(db_file_path):
        # Load existing data from the file as a list
        with open(db_file_path, 'r') as db_file:
            existing_data = json.load(db_file)

        if isinstance(existing_data, list):
            # Append the new data dictionary to the existing list
            existing_data.append(data_dict)
        else:
            # If the existing data is not a list, create a new list with both existing and new data
            existing_data = [existing_data, data_dict]
    else:
        # Create a new list with the new data dictionary
        existing_data = [data_dict]

    # Save the updated data to the file
    with open(db_file_path, 'w') as db_file:
        json.dump(existing_data, db_file)
