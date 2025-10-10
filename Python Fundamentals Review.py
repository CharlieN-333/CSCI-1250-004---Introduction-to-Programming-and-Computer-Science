def showStudents(students):
    c = 1
    for student in students:
        print(f"{c}. {student}")
        c += 1

#def showStudentsOtherWay(students):
#    for student in range(len(students)):
#        print(f"{student + 1}. {students[student]}")

def showMenu():
    print("1. Add a student.")
    print("2. Ki- Delete a student.")
    print("3. Show all students. ")
    print("4. Exit")
    try: 
        userChoice = int(input("Make your selection. "))
        if(userChoice > 4 or userChoice < 1):
            raise ValueError ("Invalid choice you idiot. ")
        return userChoice
    except ValueError:
        showMenu()
        print("Just 1, 2, 3, or 4 none of us have enough time to keep wasting it like this")

def main():
    courseName = "Introduction to Programming"
    instructor = "Mathew Desjardins"

    print(f"Welcome to {courseName}")
    print(f"Instructor: {instructor}")

    students = []
    students.append("Alice")
    students.append("Bob")
    students.append("Chris")

    menuChoice = showMenu()
    while (menuChoice != 4):
        if(menuChoice == 1):
            userInput = input("Give me student names to add to the roster, type \"Done\" to quit adding names.")

            while(userInput.upper() != "DONE"):
                students.append(userInput.title())
                userInput = input("Give me student names to add to the roster, type \"Done\" to quit adding names. ")
            menuChoice = showMenu()

        elif(menuChoice == 2):
            showStudents(students)
            deleteChoice = int(input("Which student do you want to... Delete? "))
            students.pop(deleteChoice - 1)

            valuidationChoice = input(input("Are you sure you want to... eliminate... from this list I mean {temp}? (Y/N) "))
            if(valuidationChoice.upper() == "N"):
                students.insert(deleteChoice - 1, temp) # type: ignore

            showStudents(students)
            menuChoice = showMenu()
        
        elif(menuChoice == 3):      
             showStudents(students)
             menuChoice = showMenu()

        elif(menuChoice == 4):
            showStudents(students)
            menuChoice = showMenu()

        print("Don't come back, this is terrible. ")
main()