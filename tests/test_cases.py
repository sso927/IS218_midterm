#using direct function calls 

import pytest
import pandas as pd
import os
from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand
from app.commands import GreetCommand
from app.commands import MenuCommand

from history import HistoryCommand

def test_case_greet_command():
    command = GreetCommand()
    result = command.execute()
    assert result == "Greetings! Hello, Professor! Welcome to my calculator program."


def test_case_menu_command():
    command = MenuCommand()
    result = command.execute()
    assert result == "The avaliable plugin commands are as follows: add, subtract, multiply, divide, greet, exit, and menu. To utilize these commands, simply format your input as either <number 1> <number 2> <command> or just the <command>, depending on what you want the program to do.\nView your calculation history by inputting 'history' or 'clear'."
    
def test_case1_add_command():
    command = AddCommand(10, 2)
    result = command.execute()
    assert result == 12, "The app did not provide the correct answer."


def test_case2_add_command():
     command = AddCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()


def test_case3_add_command():
     command = AddCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case1_subtract_command():
    command = SubtractCommand(10, 2)
    result = command.execute()
    assert result == 8, "The app did not provide the correct answer."


def test_case2_subtract_command():
     command = SubtractCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()


def test_case3_subtract_command():
     command = SubtractCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case1_multiply_command():
    command = MultiplyCommand(10, 2)
    result = command.execute()
    assert result == 20, "The app did not provide the correct answer."

def test_case2_multiply_command():
    command = MultiplyCommand(10, 'b')
    with pytest.raises(TypeError):
        command.execute()

def test_case3_multiply_command():
    command = MultiplyCommand('b', 10)
    with pytest.raises(TypeError):
        command.execute()

def test_case1_divide_command():
    command = DivideCommand(10, 2)
    result = command.execute()
    assert result == 5, "The app did not provide the correct answer."
   
def test_case2_divide_command():
     command = DivideCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()

def test_case3_divide_command():
     command = DivideCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case_dividebyzero_command():
    with pytest.raises(ZeroDivisionError):
        command = DivideCommand(10,0)
        command.execute()

def test_case_log_history():
    test_file = 'data/history.csv'
    if os.path.exists(test_file):
        os.remove(test_file)

    command = HistoryCommand(file= test_file)    
    command.log_history(3, 4, 'add', 7)
    new_history_df = command.retrieve_history() #retrieves the current history into a dataframe
    new_dataframe = pd.DataFrame({ #this creates the expected dataframe
        'number 1': [3],
        'number 2': [4], 
        'operation': ['add'],
        'result': [7]
    })

    pd.testing.assert_frame_equal(new_history_df, new_dataframe)

    command.log_history(10, 2, 'subtract', 8)
    new_history_df2 = command.retrieve_history()
    new_dataframe2 = pd.DataFrame({
        'number 1': [3, 10], 
        'number 2': [4, 2],
        'operation': ['add', 'subtract'],
        'result': [7, 8]
    })

    pd.testing.assert_frame_equal(new_history_df2, new_dataframe2)

   
    command.log_history(3, 3, 'multiply', 9)
    new_history_df3 = command.retrieve_history()
    new_dataframe3 = pd.DataFrame({
        'number 1': [3, 10, 3], 
        'number 2': [4, 2, 3],
        'operation': ['add', 'subtract', 'multiply'],
        'result': [7, 8, 9]
    })

    pd.testing.assert_frame_equal(new_history_df3, new_dataframe3)

   
    command.log_history(100, 5, 'divide', 20)
    new_history_df4 = command.retrieve_history()
    new_dataframe4 = pd.DataFrame({
        'number 1': [3, 10, 3, 100], 
        'number 2': [4, 2, 3, 5],
        'operation': ['add', 'subtract', 'multiply', 'divide'],
        'result': [7, 8, 9, 20]
    })

    pd.testing.assert_frame_equal(new_history_df4, new_dataframe4)

 


