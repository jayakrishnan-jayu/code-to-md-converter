#-q
# 4. Write a python program that finds the factorial of a number, N (N>2). Please note that the
# code to find the factorial of the number, N is to be written in a function.
#-q
def fact(n):
    if n==1 or n==0:
        return n
    elif n<0:
        return -1
    
    return n * fact(n-1)
n = int(input("Enter number for factorial:"))
print(fact(n))