### Python to md converter(Kinda).

Taking inspiration from reading the book 'automate the boring stuff with python' I decided to create a python script so that I don't have to waste the time that takes me to take a screenshot of the python code(both code and output) and convert that into a word file and add the questions and so on and on. The script will convert the python files into a MD file which can be easily converted into a pdf file.

#### How to use
* Create python programs starting from 1.py, 2.py, 3.py... for each question.
* Each program should start with the respective question as comments.
* The question must be enclosed with '#-q' like in sample.
* Run main.py with python files that have to be converted into md file at the same directory as the main.py script.
* Programs that require user input will also work, but the terminal won't promt the user with text 
    * For example, if 4.py is the program that will prompt for user input, the terminal output will be like
    ``` bash
    ...
    Executing 4.py
    6 # The user input.
    ```
    * The converted md file won't have this input. It has to be manually entered.

* The converted md file can be converted into pdf using this https://dillinger.io/ website for assignment submission.

* This script is created for students for reducing their time that takes them to screenshot their code and output and convert that to pdf for assignment submission.
