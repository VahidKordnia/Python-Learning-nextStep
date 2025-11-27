
# Day01-Function-Python Project05

# In this project, we will defind a function that takes a string and checks whether it is a palindrome.



# def is_palindrome() -> bool:

#     string = input("Enter your string: ").replace(" ", "").lower()
#     is_palindrome = True
#     i = 0
#     j = len(string) - 1

#     while j >= 0:
#         if string[i] == string[j]:
#             i += 1
#             j -= 1
#         else:
#             is_palindrome = False
#             break

#     if is_palindrome:
#         return "Your string is a palindrome."
#     else:
#         return "Your string is not a palindrome."    
    

# print(is_palindrome())

# ----------------------------------------------------------------------------------------------

# another option:

def is_palindrome() -> bool:

    string = input("Enter your string: ").replace(" ", "").lower()
    reversed_string = string[::-1]
    is_palindrome = True
    i = 0

    while i <= len(string) - 1:
        if string[i] == reversed_string[i]:
            i += 1
        else:
            is_palindrome = False
            break

    if is_palindrome:
        return "Your string is a palindrome."
    else:
        return "Your string is not a palindrome."    
    

print(is_palindrome())
