
# Day01-Function-Python Project07

# In this project, we will define a function that takes grades and their corresponding weights and returns weighted average.



def weighted_average() -> int:

    grades_count = int(input("How many grades do you want to calculate the weighted average for: "))
    sum = 0
    sum_weights = 0

    for i in range(grades_count):
        grade = int(input(f"Enter grade {i + 1}: "))
        weight = int(input(f"Enter the weight of the grade {i + 1}: "))
        sum_weights += weight
        sum += grade * weight

    return sum / sum_weights


print(weighted_average())    
