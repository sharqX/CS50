# ***YOUR POMODORO***
#### Video Demo: https://youtu.be/PGrC-EUHY2g
#### Description:
>The Pomodoro Technique is a time management method developed by __Francesco Cirillo__ in the late 1980s. It uses a kitchen timer to break work into intervals, typically 25 minutes in length, separated by short breaks. Each interval is known as a __pomodoro__, from the Italian word for tomato, after the tomato-shaped kitchen timer Cirillo used as a university student.
---
## Project Folder contains:
- `project.py`
- `test_project.py`
- `settings.txt`
- `sounds folder`
- `requirements.txt`
- `README.md`

***Your Pomodoro*** replaces traditional kitchen timer with a python program which helps users to manage their time effectively by breaking work or study sessions into intervals separated by short breaks. The program consists of 6 functions for setting up the timer, running the timer and the user interface which have been explained below. An additional 3 functions namely `settings_` , `menu_` and , `conti_` have been implemented for testing purposes.

### Functions
1. *`timer`* serves as the backbone of the application. It orchestrates the countdown for both work/study sessions and break periods. Utilizing the ***datetime*** module, the timer tracks and displays the remaining time until the end of each phase. Upon completion of each session, the function triggers sound notifications to alert users with the help of the ***playsound*** module, fostering a seamless workflow.  

2. *`settings`* prompts users to input their preferred durations for work/study sessions and breaks, thereby accommodating diverse schedules and preferences. Error handling mechanisms ensure that user inputs are validated, maintaining the integrity of the application. 

3. *`menu`* and *`conti`* function plays a vital role to facilitate user navigation and selection of desired functionalities such as start the timer, customize timer settings, or exit the program. It employs the ***tabulate*** module to present the options with a corresponding number which is selected by the user for a desired function. After every session the conti function is called which offers options to start a new session, change timer settings, or exit the program.

4. *`title`* function utilizes the ***pyfiglet*** library to render a stylized title for the Pomodoro timer application.

5. *`main`* function serves as the entry point of the script. It displays the title and invokes the _menu()_ function to start the timer application

A key aspect of the application is its persistence of user settings. Timer configurations are stored in a file named "settings.txt", allowing users to seamlessly restart their sessions without reconfiguring preferences. The *`timer`* function reads values for hours, minutes and seconds for both study/work session and break periods. Also the *`settings`* function makes use of this file by saving the user entered values on disk.

A folder called *`sounds`* is created to store the _.wav_ audio files which are accessed by the program for notification sounds.

*`test_project`* validates user inputs while navigating the menus and also changing the timer settings. Both conditional statements as well as *`re`* module for regular expressions are utilized in the main program for correct input. The tests are carried out by *`pytest`* module.
