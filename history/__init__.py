#place code to read history here using pandas
#it calls from history.csv file 
#pandas has to write the file and also read the file 
import pandas as pd
import logging 
import logging.config

dataFrame = pd.read_csv('data/history.csv')

class HistoryCommand:
    def __init__(self, file = 'data/history.csv'):
        self.file = file 
        self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
        self.load_history()


    def load_history(self):
        try:
            self.history = pd.read_csv(self.file)
        except FileNotFoundError:
            print('File not found.')
            logging.error('File has been found and cannot be loaded.')

    def log_history(self, num1, num2, operation, result):
        user_entry = pd.DataFrame([[num1, num2, operation, result]], columns=['number 1', 'number 2', 'operation', 'result'])
        self.history_df = pd.concat([self.history_df, user_entry], ignore_index = True)
        self.save_history()
         

    def save_history(self, file):
        self.history_df.to_csv(file, index = False)

    def retrieve_history(self):
        return self.history_df
