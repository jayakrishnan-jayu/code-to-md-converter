#-q
# 10. Write a Python program that displays a Floyd’s triangle until the number, N. An example
# of Floyd’s triangle for the number, N = 5 is given below. Please note that the code is to be
# written within a function. Flow chart for a Floyd’s triangle is given below:
#-q
def display_floyds_triangle(n):
    x=1
    num = 1

    while(x<=n):
        y=1
        while(y<=x):
            print(num, end=" ")
            num+=1
            y+=1
        print("")
        x+=1
        
display_floyds_triangle(10)