import pandas as pd
import os

# TODO Filter by date (window of time)
class DataLoader:
    def __init__(self, history_folder):
        self.history_folder = history_folder

    def load_data(self, start_date=None, end_date=None):
        history_folder_path = os.path.join(os.getcwd(), self.history_folder)

        dataframes = []

        for history_filename in os.listdir(history_folder_path):
            with open(os.path.join(history_folder_path, history_filename), 'r', encoding='utf-8') as history_file:
                dataframes.append(pd.read_csv(history_file))
        
        data = pd.concat(dataframes)

        return data
        