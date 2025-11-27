
# Day01-Function-Python Project01

# In this project, we will define a function that takes an integer and returns the sum of its digits.



def sum_digit() -> int:
    integer = (input("Enter an integer: "))
    sum = 0
    for i in integer:
        sum += int(i)
    return sum
    


print(sum_digit())



# Note:
# Integers are not iterable. Therefore, we can not use a for loop on them.

# wrong code:
# def sum_digit() -> int:
#     integer = int(input("Enter an integer: "))
#     sum = 0
#     for i in integer:           # An integer like 123 is not iterable as 1, 2 and 3.
#         sum += (i)
#     return sum
