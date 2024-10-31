from app.commands import GreetCommand
import logging 

def execute():
    command = GreetCommand()
    logging.info('Greet command displayed.')
    return command.execute()

