#IS218 Midterm - Calculator Project  
##Sharon Oh 
This midterm is for the course IS218 during the Fall 2024 semester at the New Jersey Institute of Technology. The midterm project requires us to develop an advanced calculator application using Python, Ubuntu, WSL, GitHub, and other knowledge we acquired from the previous lectures during the course. 

The video that demos this calculator application is here.

##Details 
During the initial stages of the project, I started off with setting up the repo and downloading the necessary packages to ensure I had everything prepared. I first created the repository in GitHub and connected it to my local repository so that all my changes would sync up to the GitHub repo. I set up the necessary virtual environments after downloading them and activated it using "source my_env/bin/activate" so that the program would be able to run on this particular environment. I downloaded necessary packages/libraries/test such as pandas, pytest, etc to prepare the program for the different functions that will utilize those external downloads. At the initial stages, I made sure to freeze the requirements and transfer fundamental configuration files such as the logging.conf, .pylintrc, and pytest.ini files to name a few. Doing all of these smaller steps set up the program so that I could then work on the REPL interface and the plugin system.  

Design Patterns: 
The command-line interface uses REPL which is the read, evaluate, print loop to process user inputs from the command terminal and enacts direct interaction with the program. Users can utilize a plugin system that dynamically loads at the start of the program and allows for the flexible usage of various commands including both arithemtic commands and general program commands. For example, some plugins in the program include: add, subtract, multiple, divide, greet, menu, exit. The "menu" command can be used to list all the other available plugins in the calculator program to enable accessibility by the users. The main design pattern used for this application was the command pattern and a plugin system that allowed me to create objects for each particular operation such as add or subtract. This kept everything organized. I kept all of the arithematic commands in a separate file in the separate command folder that included functions like AddCommand or SubtractCommand. I utilized plugins to organize the execution of these operations which called from the command folder. Therefore, the majority of the action was occuring not amongst the plugin files, but in the command/__init__.py file. Additionally, I have a calculator folder with a file that defines the class Calculator which is used in my main app/__init__.py file. In this file there is the "App"" class that is defined with various functions in that contribute to the REPL process. The user input is read by the "start" function and since the calculator is instantiated and called in this method, the plugins dealing with the operations are executed. Since these plugins are simply executing the commands in the commands folder, essentially the design of the application is very tightly related to each other. To backtrack a little bit, the user input is read through the app/__init__.py file (by the "App" class) and has the plugins registered based on the input of the user. The plugins are connected to the mathematical function within the AddCommand, SubtractCommand, etc and once that command runs, the result is outputted into the terminal. There are exception cases that I added in this design pattern to catch any invalid user inputs. For example, if a use were to type in "bye" or "school" which are not valid commands, they would be notified. Additionally, if they were to mistype and accidentally include a letter in their input (such as "3 d add"), they would be notified that they also had another invalid input. This makes the calculator interactive and engages the user with the functionality of the calculator. The use of a interconnected design system that is structured in an organized manner, through utilizing only necessary files and a flexibile plugin system, users can easily utilize all of the available commands and features. 


Environment Variables:
Environment variables were used to store secret or sensitive information through its key and value pairs. While perhaps unnecessary in the context of a calculator application, because there isn't really secretive information, it is useful to utilize as it offers a way of protection of important data. I used environment variables to keep track of sensitive information such as "DATABASE_USERNAME", "PASS_KEY", and "SETTING". Rather than hardcoding this information somewhere in the program, I placed it into an .env file and had the program just print off of it. I had to utilize a load_dotenv and create a separate function to load the environment variables from the operating system. This will all done in the class "App" method.

Logging:
Throughout the program, I used logging to ensure that the program was running smoothly and that all the information was recorded down. I used various levels of logs, mainly "logging.info" and "logging.error" to record the messages that were generated by the program. It helped me keep track of the application and to better understand how the program flowed. The log was used in multiple areas of the program and was stored in its own private log folder/file. 

Try/Catch/Exceptions:



if video is short, include tutorial on how to install program from github link 


Setup Instructions:


The calculation history is managed through pandas which permits the users to load, clear, save, and delete the history records through the interactive terminal. The user's calculation history needed to be saved and also recalled based on the user input. Pandas was used in conjunction with a csv file titled "histor.csv" to be able to read and input the calculation histories from the user input and also back into the terminal.  


Choices for architectural descisions 

YAML file for GitHub Actions 

Test cases 