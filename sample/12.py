#-q
# 12. What is meant by returning a value from a function? Give an explanation with an example.
#-q
# returning a value from a function is returning a peiece of data
# after the function execution is finished to function call

def greet(name):
    return "Hello " + name

text = greet("world")
print(text)