### 1. What is a function? 

```python

# function is a set of instructions that is resuable and can be used repeatedly.
```
---

### 2. What is a function definition? Give an example 

```python
# function is a named section of code and function definition is the code that defines the function.

def greet():            # This is a function definition
    print("Hello world")
```
---

### 3. What is a function call? Give an example. 

```python
# Function call is the line of code that starts the execution of the function.

def greet():            # This is a function definition
    print("Hello world")

greet() #This is a function call.
```

## Output
```python
Hello world
```
---

### 4. Write a python program that finds the factorial of a number, N (N>2). Please note that the code to find the factorial of the number, N is to be written in a function. 

```python
def fact(n):
    if n==1 or n==0:
        return n
    elif n<0:
        return -1
    
    return n * fact(n-1)
n = int(input("Enter number for factorial:"))
print(fact(n))
```

## Output
```python
Enter number for factorial: 
2
```
---

### 5. Write a python program that displays the Fibonacci series until the number, N (N>2). Please note that the code to display the Fibonacci series until the number, N is to be written in a function. 

```python
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
```

## Output
```python
Enter number: 

```
---

### 6. Write a python program that determines whether the number entered by the user, N (N>2) is a palindrome or not and display a message accordingly. Please note that the code to check whether a number is a palindrome or not is to be written in a function. 

```python
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

```

## Output
```python
Is palindrome
```
---

### 7. Write a python program to find the maximum of three numbers. Please note that the code to find the maximum of three numbers is to be written in a function. 

```python
def find_max_of_three(a, b, c):
    big = a if a>b else b
    big = big if  big>c else c
    print("Maximum of three is ", big)

find_max_of_three(4,23,5)
```

## Output
```python
Maximum of three is  23
```
---

### 8. Write a python program that accepts a string (lowercase) and displays the same string in uppercase. Please note that the code to convert a lowercase string to uppercase is to be written in a function.  

```python
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
```

## Output
```python
HELLO WORLD
```
---

### 9. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: (1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128. Use a function to determine whether a number entered by the user, N is a perfect number or not. 

```python
def is_perfect_number(n):
    copy = n
    total = 0
    while n>1:
        n-=1
        if (copy % n == 0):
            print(n, end=" ")
            total+=n
    print()

    return copy == total

print(is_perfect_number(8128))
```

## Output
```python
4064 2032 1016 508 254 127 64 32 16 8 4 2 1 
True
```
---

### 10. Write a Python program that displays a Floyd’s triangle until the number, N. An example of Floyd’s triangle for the number, N = 5 is given below. Please note that the code is to be written within a function. Flow chart for a Floyd’s triangle is given below: 

```python
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
```

## Output
```python
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 32 33 34 35 36 
37 38 39 40 41 42 43 44 45 
46 47 48 49 50 51 52 53 54 55 
```
---

### 11. What is meant by arguments with respect to a function? Give an explanation with an example. 

```python
# Arguments are variables that can be passed into functions
# They are specified after the function name

def greet(name):         # Greet function takes an argument named name
    print("Hello ",name)
```
---

### 12. What is meant by returning a value from a function? Give an explanation with an example. 

```python
# returning a value from a function is returning a peiece of data
# after the function execution is finished to function call

def greet(name):
    return "Hello " + name

text = greet("world")
print(text)
```

## Output
```python
Hello world
```
---

### 13. Write an algorithm for finding the factorial of a number. 

```python
# input a number n
# initilize a variable total with value 1
# loop through 1,n
#   for each value 
#       set the value of variable total to be total * value
# print total

```
---

### 14.Write a python program that finds the factorial of a number, N (N>2). Return the value to the line of code which called the function and display the value. Please note that the code to find the factorial of the number, N is to be written in a function 

```python
def fact(n):
    if n==1 or n==0:
        return n
    elif n<0:
        return -1
    
    return n * fact(n-1)

print(fact(10))
```

## Output
```python
3628800
```
---

### 15. Write a python program to find the maximum of three numbers. Please note that the code to find the maximum of three numbers is to be written in a function. Also note that the maximum number has to be returned from the function and displayed. 

```python

def find_max_of_three(a, b, c):
    big = a if a>b else b
    big = big if  big>c else c
    print("Maximum of three is ", big)

find_max_of_three(4,23,5)
```

## Output
```python
Maximum of three is  23
```