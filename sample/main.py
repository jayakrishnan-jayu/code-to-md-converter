
import sys
import os
import subprocess
def main():
    print("This program requires python files which are to be converted to md file\nto be present at the same directory as this file.\nIt should start with 1.py and continue like 2.py, 3.py etc")

    no_of_files = int(input("Enter the number of files to be converted: "))
    question_tag = '#-q'     # This is the question tag that should be present at the top of the program in between the question.
    output_string = ""

    for i in range(no_of_files):         # Loop through every file.
        program_name = "{}.py".format(i+1)  
        try:
            question = ""
       
            cmd = 'python3 '+program_name

            
            with open(program_name, "r") as codeFile:     #open each file as codeFile

                lines = [line.rstrip('\n') for line in codeFile]     # Remove trailing newline character from every line

                if lines.count(question_tag) == 2:
    
                    question_start = lines.index('#-q') + 1         # The index at which the question starts
        
                    while (lines[question_start] != question_tag):    #loop until the second question tag is reached.
                        
                        question += lines[question_start].lstrip("# ") + " "
                        question_start +=1
        

                    if (question != ""):
                        output_string += "### " + question + "\n\n"    # Question as H3 title
                        output_string += "```python\n"   # Starting of code
                        question_start += 1

                        while (question_start < len(lines)):    #add code to output string

                            output_string += lines[question_start] + "\n"
                            question_start +=1

                        output_string += "```"  # End of code

        
                        print("Executing "+program_name) 
                        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)  # Execute program to get the output
                        p.wait()
                        out, err = p.communicate()
                        
                        program_output = out.decode().split("\n")
                        
                        if program_output != [''] and program_output != []:     # Checking if there is output
                        
                            program_questions = program_output[0].split(":")[:-1]
            
                            output_string += "\n\n## Output\n"
                            output_string += "```python\n"

                            for program_question in program_questions:
                                print(program_question)    
                                output_string += program_question+": \n"     # Adding the input question that prompts the user, the input provided will not be stored. Have to enter that manually.

                            output_string += program_output[0].split(":")[-1]+"\n"
  
                            for text in program_output[1:-1]:
                                output_string += text+"\n"

                            output_string += "```"



                        print("Done executing")

                       
                        if (i+1 != no_of_files):
                            output_string += "\n---\n\n"


                       
                    else:
                        print("No question found in program {}\nExiting...".format(program_name))
                        sys.exit()
                else:
                    
                    error = "Invalid use of question tag '{}' in program {}\nThere should be only two question tag.\nExiting...".format(question_tag, program_name)
                    print(error)
                    sys.exit(0)
        

        except FileNotFoundError:
            error = "File {} not found.\nPlease create file {}\nExiting...".format(program_name, program_name)
            print(error)
            sys.exit()

    with open("output.md", "w") as output_file:
            output_file.write(output_string)
            print("output.md file created.")
            
            


if __name__ == "__main__":
    main()