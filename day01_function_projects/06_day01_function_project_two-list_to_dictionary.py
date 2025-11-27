
# Day01-Function-Python Project06

# In this project, we want to write a function that takes two lists of equal length and returns a dictionary created from them.



# def key_value_lists_to_dict(keys: list, values: list) -> dict:

#     dict = {}

#     if len(keys) == len(values):
#         for i in range(len(keys)):
#             dict.update({keys[i]: values[i]})
#         return dict
    
#     else:
#         return "The lists you provided must be the same length. Please correct them."
    

# keys = ["first name", "last name", "city"]
# values = ["Vahid", "Kordnia", "Babol"]   
# print(key_value_lists_to_dict(keys, values))


# another option:

def key_value_lists_to_dict(**kwargs) -> dict:
    return kwargs
    

print(key_value_lists_to_dict(name="Vahid", last_name= "kordnia", city = "Babol"))


# -----------------------------------------------------------------------------------------------------------------------


# When we want to define a function that takes keys and values one by one (not as lists of keys and values).

# def dict() -> dict:

#     dict_items_count = int(input("How many items is your dictionary going to have: "))
    
    
#     dict = {}

#     for i in range(dict_items_count):
#         key = input(f"Enter input {i + 1} as the key {i + 1}: ")
#         value = input(f"Enter input {i + 1} as the value {i + 1}: ")
#         dict.update({key: value})

#     return dict


# print(dict())    
