
# Day01-Function-Python Project02

# In this project, we will define a function that takes a string and counts non-repeating letters.



# def count_non_repeating_letters() -> int:

#     string = (input("Enter a text: ").lower())

#     count = 0
#     list_of_letters = []

#     for i in string:

#         if i.isalpha():
#            if i not in list_of_letters:
#                count += 1
#                list_of_letters.append(i)        
#                                                              # another option:  list_of_words += [i]                                 
#                                                              # In general, It's wrong --> list_of_words +=  i                              
#                                                  # Concatenation only works when both sides are the same type (i is a string).   

#     return count


# print(count_non_repeating_letters())



# another option:

def count_non_repeating_letters() -> int:

    string = (input("Enter a text: ").lower())
    
    set_of_letters = set()
                                        # To creat an empty set, we can't use "set_of_letters = {}" because Python
                                        # interprets it as an empty dictionary. instead, we must use "set_of_letters = set()" to
                                        # creat an empty set.
    for i in string:

        if i.isalpha():
            set_of_letters.add(i)                                                

    return len(set_of_letters)
                                        # A set automatically removes duplicate values.

print(count_non_repeating_letters())




# ------------------------------------------------------------------------------------------------------------------------------


# If we wanna count non-repeating words.

# def count_non_repeating_words() -> int:

#     string = (input("Enter a text: ").lower())
#     string = string.replace(".", "")
#     string = string.replace(",", "")

#     count = 0
#     list_of_words = []
#     splitted_string = string.split()

#     for i in splitted_string:

#         if i.isalpha():
#             if i not in list_of_words:
#                 count += 1
#                 list_of_words += i             
                                                    
                                                    
#     return count        



# print(count_non_repeating_words())
