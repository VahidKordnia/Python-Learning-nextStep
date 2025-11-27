
# Day01-Function-Python Project08

# In this project, we will write a function that takes a person's name and job title, and returns a sentence
# like "Amir is a teacher". If the job title is not provided, the default value should be "programmer".


# def info() -> str:

#     name = input("Enter person's name: ")
#     job_title = input("Enter person's job title: ")

#     if job_title == "":
#         return f"{name} is a programmer."
#     else:
#         return f"{name} is a {job_title}."
    

# print(info())


# ------------------------------------------------------------------------------


# def info(name: str, job_title: str) -> str:

#     if job_title == "":
#         return f"{name} is a programmer."
#     else:
#         return f"{name} is a {job_title}."
    

# print(info("Amir", "teacher"))
# print(info("Amir",""))

    
# ------------------------------------------------------------------------------


def info(name: str) -> str:
    job_title = input(f"Enter {name}'s job title: ")
    if job_title == "":
        return f"{name} is a programmer."
    else:
        return f"{name} is a {job_title}."
    
print(info("Amir"))
