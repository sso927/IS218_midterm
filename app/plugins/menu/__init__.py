from app.commands import MenuCommand
import logging 

def execute():
    command = MenuCommand()
    logging.info('Menu command displayed with instructions.')
    return command.execute()

