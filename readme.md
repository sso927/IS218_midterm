IS218 Midterm 
Sharon Oh 


if video is short, include tutorial on how to install program from github link 


Setup Instructions:
To begin the setup of this program, I first created the repository in GitHub and connected it to my local repository so that all my changes would sync up to the GitHub repo. I set up the necessary virtual environments after downloading them and activated it using "source my_env/bin/activate" so that the program would be able to run on this particular environment. I downloaded necessary packages/libraries/test such as pandas, pytest, etc to prepare the program for the different functions that will utilize those external downloads. At the initial stages, I made sure to freeze the requirements and transfer fundamental configuration files such as the logging.conf, .pylintrc, and pytest.ini files to name a few. Doing all of these smaller steps set up the program so that I could then work on the REPL interface and the plugin system. 

The command-line interface uses REPL which is the read, evaluate, print loop to process user inputs from the command terminal and enacts direct interaction with the program. Users can utilize a plugin system that dynamically loads at the start of the program and allows for the flexible usage of various commands including both arithemtic commands and general program commands. For example, some plugins in the program include: add, subtract, multiple, divide, greet, menu, exit. The "menu" command can be used to list all the other available plugins in the calculator program to enable accessibility by the users. 

The calculation history is managed through pandas which permits the users to load, clear, save, and delete the history records through the interactive terminal. 

Logging practices 

YAML file for GitHub Actions 

Test cases 