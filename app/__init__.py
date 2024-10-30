import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

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
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info('Environment variables have been loaded.')
       
        secret_key = os.getenv('SECRET_KEY')
        database_username = os.getenv('DATABASE_USERNAME')

        print(f"Secret Key: {secret_key}")
        print(f"Database Username: {database_username}")

        return settings 
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg: 
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                logging.info('Plugins have been loaded.')

                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue   

                
    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit. Format math commands as: <number1> <number2> <add>/<subtract>/<multiply>/<divide>.")
        while True:  
            command_input = input(">>> ").strip()
            if command_input.lower() == 'exit':
                logging.info('Exit command registered.')
                raise SystemExit('Exiting...')
    
            user_input = command_input.split()

            if len(user_input) == 3: 
                userCommand = user_input[2]
                numbers = user_input[:2]

                if userCommand not in ['add', 'subtract', 'multiply', 'divide']:
                    print(f'User did not input valid command.')
                    logging.error('Invalid command.')
                    continue

                self.command_handler.execute_command(userCommand, *numbers)
                continue

            else:
                userCommand = user_input[0]

                if userCommand not in ['menu', 'greet', 'exit', 'add', 'subtract', 'multiply', 'divide']:
                     print(f"No such command: {command_input}")
                     logging.error('Unknown command.')
                     continue 

            self.command_handler.execute_command(userCommand)