#-q
# 8. Write a python program that accepts a string (lowercase) and displays the same string in
# uppercase. Please note that the code to convert a lowercase string to uppercase is to be
# written in a function. 
#-q
def to_upper(string):
    output_string = ""
    for x in string:
        ascii_value = ord(x)
        if (ascii_value >= 97 and ascii_value <= 122):
            output_string += chr(ascii_value-32)
            continue
        output_string += chr(ascii_value)

    print(output_string)

to_upper("Hello world")