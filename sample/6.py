#-q
# 6. Write a python program that determines whether the number entered by the user, N (N>2)
# is a palindrome or not and display a message accordingly. Please note that the code to
# check whether a number is a palindrome or not is to be written in a function.
#-q
def is_palindrome(n):
    copy = n
    reverse = 0
    while(n>0):
        reverse = (reverse * 10) + (n % 10)
        n//=10

    if copy == reverse:
        print("Is palindrome")
        return
    print("Not a palindrome")

is_palindrome(101)

