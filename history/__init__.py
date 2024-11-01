import pandas as pd
import os
import logging 
import logging.config

class HistoryCommand:
    def __init__(self, file = 'data/history.csv'):
        self.file = file 
        self.history = []
        self.load_history()


    def load_history(self):
        if os.path.exists(self.file):
            if os.stat(self.file).st_size == 0:
                print(f'The file is empty.')
                self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
                self.save_history()
            '''
            self.history_df = pd.read_csv(self.file)

            if self.history_df.empty:
                print(f'The CSV file is empty. It will be initialized with the defaults.')
                logging.error('There is an empty CSV file.')
                self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
            '''
        else:
            self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
            print(f'File not found. It will be initialized with the defaults.')
            logging.error('File has not been found and cannot be loaded.')
        
    def log_history(self, num1, num2, operation, result):
        log_format = {
            'number 1': num1, 
            'number 2': num2, 
            'operation': operation, 
            'result': result
        }

        self.history.append(log_format)
        logging.info('Calculations have been logged.')

        self.history_df= pd.DataFrame(self.history)
        self.save_history()

    def save_history(self):
        self.history_df.to_csv(self.file, index = False)

    def retrieve_history(self):
        return self.history_df

    def clear_history(self):
        self.history = []
        self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
        self.save_history()

