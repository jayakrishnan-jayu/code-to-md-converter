#-q
# 5. Write a python program that displays the Fibonacci series until the number, N (N>2).
# Please note that the code to display the Fibonacci series until the number, N is to be written
# in a function.
#-q
def fibonacci(n):
    if (n>2):
        first = 0
        second = 1
        for i in range(n):
            print(first, end=" ")
            third = first + second
            first = second
            second = third
        print()
fibonacci(int(input("Enter number:")))