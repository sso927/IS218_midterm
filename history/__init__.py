import pandas as pd
import os
import logging 
import logging.config

class HistoryCommand:
    def __init__(self, file = 'data/history.csv'):
        self.file = file 
        self.load_history()


    def load_history(self):
        if os.path.exists(self.file):             
            if os.stat(self.file).st_size == 0: #checks if file is completely empty and will make headers
                logging.info('There is no history in the csv file.')
                self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
                self.save_history()
           
            else: #saying that there is previous info in the file
                self.history_df = pd.read_csv(self.file)
                logging.info('There is history in the csv file.')
           
        else: #file literally doesn't exist 
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

        new_calculations_df = pd.DataFrame([log_format])
        if self.history_df.empty:
            self.history_df = new_calculations_df
        else:
            #self.history.append(log_format)
            self.history_df = pd.concat([self.history_df, new_calculations_df], ignore_index=True)
        self.save_history()
        
    

    def save_history(self):
        self.history_df.to_csv(self.file, index = False)

    def retrieve_history(self):
        return self.history_df

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['number 1', 'number 2', 'operation', 'result'])
        self.save_history()

''' self.history.append(log_format)
        logging.info('Calculations have been logged.')

        self.history_df= pd.DataFrame(self.history)
        self.save_history()'''

#the above doesn't work since it will break if there is the csv is empty 