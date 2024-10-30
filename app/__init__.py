import pkgutil
import importlib
from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand

from dotenv import load_dotenv
import logging
import logging.config
import os 

class App: #all of the environment variable things 
    def __init__(self): 
        self.command_handler = CommandHandler()
        os.makedirs('logs', exist_ok = True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('SECRET_KEY', 'DATABASE_USERNAME')

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.") #you can change the log message 

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info('Environment variables have been loaded.')
       
        secret_key = os.getenv('SECRET_KEY')
        database_username = os.getenv('DATABASE_USERNAME')
        mode = os.getenv('testing')
            if mode == 'testing':
            #blah blah 

        print(f"Secret Key: {secret_key}") #you can change the log message 
        print(f"Database Username: {database_username}")

        return settings 
    
    #mode = testing
    
    #keep this function 
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins' #can change the name if you want 
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg: 
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                logging.info('Plugins have been loaded.') #change log messages 

                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue   
#know how to use the code/understand 
#add in your own plugins 
#if you can't change your code, don't know, you can play around with the code and structure (as long as you meet the requirements + commits) 

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")


#new code... similar logic different code 
    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit the program. Format the commands as: <number1> <number2> <command>. \nPossible commands are: 'greet', 'exit', 'add', 'subtract', 'multiply', 'divide'.")
        logging.info('Program has started.')
        
        while True:  
            whole_input = input(">>> ").strip()
            input_parts = whole_input.split()

            if len(input_parts) == 3:
                input_numbers = input_parts[:2]
                input_functionCommand = input_parts[2]

                if input_functionCommand.lower() == ['add', 'subtract', 'multiply', 'divide']:
                    self.command_handler.execute_command(input_functionCommand, *input_numbers)
                else:
                    print(f'User did not input a valid command. Try again.')
                    logging.error('Invalid arithemetic command.')
                continue 
            
            if len(input_parts) == 1:
                input_command = input_parts[0]

                if input_command.lower() not in ['greet', 'exit', 'add', 'subtract', 'multiply', 'divide']:
                    print(f"There is no such command as: {input_command}.")
                    logging.error('User has inputted an unknown command.')
                else:
                    self.command_handler.execute_command(input_functionCommand)

                if input_command.lower() == 'exit':
                    logging.info('System will exit.')
                    raise SystemExit('Exiting.')