#-q
# 9. In number theory, a perfect number is a positive integer that is equal to the sum of its proper
# positive divisors, that is, the sum of its positive divisors excluding the number itself (also
# known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum
# of all of its positive divisors (including itself). Example : The first perfect number is 6,
# because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the
# number 6 is equal to half the sum of all its positive divisors: (1 + 2 + 3 + 6 ) / 2 = 6. The
# next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers
# 496 and 8128. Use a function to determine whether a number entered by the user, N is a
# perfect number or not.
#-q
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