
# Day01-Function-Python Project03

# In this project, we will define a function that takes numbers and returns their product.



# def product() -> int:
#     count = int(input("How many numbers are you going to multiply: "))
#     product = 1

#     for i in range(count):
#         product *= int(input(f"Enter number {i + 1}: "))

#     return product


# print(product())



# another option:

def product(*arg):
                            # *args collects any number of positional arguments into a "tuple".
    product = 1

    for i in arg:
        product *= i

    return product

print(product(1, 3, 4))
                            # Here 1, 2, 3 are positional arguments which are collected into a tuple.
                            