import pkgutil
import importlib

from calculator.calculator import Calculator
from history import HistoryCommand

from dotenv import load_dotenv
import logging
import logging.config
import os 

class App:   
    def __init__(self): 
        os.makedirs('logs', exist_ok = True)
        self.configure_logging()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('DATABASE_USERNAME','PASS_KEY')
        self.history = HistoryCommand()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging is now configured and ready.") 

    def load_environment_variables(self):
        load_dotenv()
        settings = {key: value for key, value in os.environ.items()}
        logging.info('Environment variables have been loaded.')
       
        database_username = os.getenv('DATABASE_USERNAME')
        pass_key = os.getenv('PASS_KEY')

        print(f"\nHello, World! Welcome to my calculator program :D \nThere is some important information below. Thank you for being here!")

        print(f"\nThe username for the database is {database_username}.")
        logging.info('The username database information has been logged.')
        print(f"The pass key is {pass_key}... but SHUSHHH it's a secret!")
        logging.info('The pass key information has been logged.')  
    
        setting = os.getenv('SETTING')
        if setting == 'production':
            print(f"The setting is production.")
        else:
            print(f"The setting is not production. It is {setting}.")
        logging.info(f'The setting has been logged.')

        return settings 
    
    def load_plugins(self):
        plugins_package = 'app.plugins' 
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if not is_pkg:
                try:
                    module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    logging.info(f'Loading plugins: {module}')
                except Exception as e:
                    logging.error(f'Failed to load plugins: {e}')

    def start(self):
        self.load_plugins()
        print("\nType 'exit' to exit the program. Type in 'menu' to view avaliable commands.")
        logging.info('Program has started.')
        
        calc = Calculator()

        while True:  
            whole_input = input(">>> ").strip()
            input_parts = whole_input.split()

            if len(input_parts) == 3:
                try: 
                    num1 = float(input_parts[0])
                    num2 = float(input_parts[1])
                    input_functionCommand = input_parts[2].lower()

                    if input_functionCommand in ['add', 'subtract', 'multiply', 'divide']:
                        result = getattr(calc, input_functionCommand)(num1, num2)
                        print('The result is ',result)
                        if input_functionCommand == 'add':
                            logging.info("Addition Command performed properly. Yay!")
                            self.history.log_history(num1, num2, 'add', result)
                        elif input_functionCommand == 'subtract':
                            logging.info("Subtraction Command performed properly. Yay!")
                            self.history.log_history(num1, num2, 'subtract', result)
                        elif input_functionCommand == 'multiply':
                            logging.info("Multiply Command performed properly. Yay!")
                            self.history.log_history(num1, num2, 'multiply', result)
                        elif input_functionCommand == 'divide':
                            logging.info("Divide Command performed properly. Yay!")
                            self.history.log_history(num1, num2, 'divide', result)

                    else:
                        print(f'User did not input a valid command. Try again.')
                        logging.error('Invalid arithemetic command.')
                except ValueError as e:
                    print(f"Error: You put in invalid numbers. Please try again.")
                    logging.error("ValueError from user inputting invalid numbers.")
                except ZeroDivisionError as e:
                    print(f"Error: You cannot divide by zero. Please try again.")
                    logging.error("ZeroDivisionError from user inputting invalid numbers.")
                continue  


            if len(input_parts) == 1:
                input_command = input_parts[0]
                if input_command.lower() not in ['greet', 'exit', 'menu', 'add', 'subtract', 'multiply', 'divide', 'history', 'clear']:
                    print(f"There is no such command as: {input_command}.")
                    logging.error('User has inputted an unknown command.')
                elif input_command.lower() == 'menu':
                    from app.plugins.menu import execute as menu_execute 
                    menu_execute()
                    logging.info('Menu command has been executed.')
                elif input_command.lower() == 'exit':
                    logging.info('System will exit.')
                    raise SystemExit('The system will now be exiting...Bye!!!')
                elif input_command.lower() == 'greet':
                    from app.plugins.greet import execute as greet_execute 
                    greet_execute()
                    logging.info('Greetings prompted.')
                elif input_command.lower() == 'history':
                    history_df = self.history.retrieve_history()
                    if history_df.empty:
                        print('There is no history.')
                    else: 
                        print(history_df)
                elif input_command.lower() == 'clear':
                    self.history.clear_history()
                    print('History has been cleared.')
                else:
                    print(f'Unknown command.')
