# CSCI 1250 Python Practicum Exam
# Student Name: Charles Norris
# Date: 10/9/2025

# Score: _______/100 (max 105)

# Instructions:
# - Fill out each task below by writing Python code to answer the question.
# - Do not modify any existing code, pass is to be overwritten with your code below each function block.
# - Ensure your solutions work correctly by testing them.
# - There is a written answer section below be sure to write your answers in comments.
# - In the main() function, is available for you to call your functions.

# - When finished, please submit your .py file into the D2L Dropbox - "Midterm"


# Task 0: Ensure that your code adheres to a consistent style and coding recommendations discussed in class.
# You must use proper formatting, clear and descriptive variable names, and provide sufficient comments.
# Up to 20 points may be deducted for failing to meet these requirements.
# These 20 points are included in your total score, so no points will be lost if you follow the guidelines correctly.

#Task 1: Create a function that returns a string that answers "what is stored in a string variable?" (2 points)
def get_string():
    print("Data that can only be called back by that one varible even if the data is equal to another one.")

#Task 2: Print a string that would be an invalid name for a variable. (2 points)
def get_invalid_variable_name():
    # A variable name cannot start with a number, have spaces, or have symbols that aren't unberscores
    print("1 Bad variable!") 

#Task 3: Create a function that returns a list of integers from input from the user. (4 points)
def get_list():
    user_Input = input("Input numbers for a list (with spaces inbetween numbers). ")
    try:
        num_List = [int(x) for x in user_Input.split()]
        print(num_List)
        return num_List
    except ValueError:
        print("Only numbers.")
        return []
    

# Task 4: Collections and Loops (10 points)
# Write a function `sum_list(lst)` that takes a list of integers `lst` and returns the sum of all the elements in the list.
# Example: sum_list([1, 2, 3, 4, 5]) should return 15.
def sum_list(lst):
    sum_list([])
    user_Input = input("Input numbers for a list (with spaces inbetween numbers).")
    try:
        lst = [int(x) for x in user_Input.split()]
        print(sum(lst))
        return lst
    except ValueError:
        print("Only numbers.")
        return []

# Task 5: Decision Structures (10 points)
# Write a function `triangle_type(a, b, c)` that accepts three integer sides of a triangle.
# The function should return "equilateral" if all sides are equal, "isosceles" if only two sides are equal, 
# and "scalene" if all sides are different.
def triangle_type(a, b, c):
    if (a == b == c):
        print("Equilateral")
    elif (a == b or a == c or b == c):
        print("Isosceles")
    else:
        print("Scalene")

# Task 6: Functions (10 points)
# Write a function `factorial(n)` that returns the factorial of a number `n`. Use a loop (instead of recursion) to calculate it.
# Example: factorial(5) should return 120 (since 5 * 4 * 3 * 2 * 1 = 120).
def factorial(n):
    n = input()
    factor1 = 1
    for i in range(2, n +1):
        factor1 *=1
    print(factor1)

# Task 7: Input Validation (12.5 points)
# Write a function `get_valid_integer()` that repeatedly asks the user for an integer input between 1 and 100 (inclusive).
# If the user enters a value outside this range, the function should display an error message and continue asking for input
# until a valid number is entered. Once a valid number is entered, return the number.
# Example: If the user enters -5, 150, and then 50, the function should return 50.
def get_valid_integer():
    try: 
        userChoice = int(input("Input a number 1-100 "))
        if(userChoice > 1 or userChoice < 100):
            raise ValueError ("Invalid number lol ")
        return userChoice
    except ValueError:
        print("Number(s) have to be between 1 and 100 ")


# Task 8: Running Total with Input Validation (12.5 points)
# Write a function `running_total()` that continuously asks the user to enter a number.
# The function should keep a running total of all numbers entered and stop asking for input when the user enters -1.
# When -1 is entered, the function should return the total sum of all numbers entered (excluding -1).
# Example: If the user enters 5, 10, -1, the function should return 15.
def running_total():
    user_input = 0
    while (user_input !=-1):
        user_input = int(input("what numbers would you like to add together? -1 to stop adding numbers "))
        


#-------------------------------------------------------------------------------------------------------------------------------------
# Task 9: What is the difference between a syntax error and a logic error? (3 points)
# Answer in the comments below:

# Syntax Error: Where code doesn't follow the rules of the language it is coded in which causes the code to not run
# Logic Error: Where code works but doesn't reach the intended or correct result

# Logical Operator Evaluation (1.5 points each (9 points total))
# What are the results of the following logical expressions (True or False)?

# Task 10a: True or False and True
# Answer: True?

# Task 10b: not False or False and True
# Answer: True

# Task 10c: False or False and True or not True
# Answer: False?

# Task 10d: True and not False or False
# Answer: True

# Task 10e: not (True or False) and (False or True)
# Answer: False

# Task 10f: True and (False or not True)
# Answer: False (true and false do not look like words anymore)
#-------------------------------------------------------------------------------------------------------------------------------------

#Task 11: Write a function that does the following: (25 points)
# - Asks a user to enter the number of students.
# - For each student, ask for their name and three test scores.
# - Store this information in a list. Where the zero index is the student name, and the indices 1, 2, and 3 are the test scores.
# - Calculate the average score for each student.
# - Assign a letter grade based on the average (A = 90–100, B = 80–89, C = 70–79, D = 60–69, F = below 60).
# - Print each student’s name, their average score (rounded to 2 decimals), and their letter grade.
# - BONUS(5 points): Find the student with the highest average score, the lowest average score, and print their names at the end of the report.
def student_grades():
    pass #replace this line, including "pass" with your code


#You may test your code by calling the functions above in the main function below.
def main():
   pass #replace this line, including "pass" with your function calls. You can comment out the function calls if you wish after testing.
# Calls the main function (Don't Touch!!!)
if __name__ == "__main__":
    main()
