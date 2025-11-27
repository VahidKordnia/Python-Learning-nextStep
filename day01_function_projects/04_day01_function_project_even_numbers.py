
# Day01-Function-Python Project04

# In this project, we will define a function that takes a list of numbers and returns the list of even numbers.



# def even_numbers(a: list) -> list:

#     even_numbers = []

#     for i in a:
#         if round(i / 2) == i / 2:
#             even_numbers.append(i)         # another option --->  even_numbers += [i]

#     return even_numbers


# numbers = [1, 2, 3, 4 ,5, 6, 7, 8 ,9]
# print(even_numbers(numbers))



# another option:

# def even_numbers(a: list) -> list:

#     even_numbers = []

#     for i in a:
#         if i % 2 == 0:
#             even_numbers.append(i)

#     return even_numbers


# numbers = [1, 2, 3, 4 ,5, 6, 7, 8 ,9]
# print(even_numbers(numbers))



# another option:

# def even_numbers(*args):

#     even_numbers = []

#     for i in args:
#         if i % 2 == 0:
#             even_numbers.append(i)

#     return even_numbers

# print(even_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2))   
                                                                         # Output is a list.


# another option:

def even_numbers(*args):

    even_numbers = ()

    for i in args:
        if i % 2 == 0:
            even_numbers = even_numbers + (i,)

    return even_numbers

print(even_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2))
                                                                         # Output is a tuple.
                                                                        