def greet():
    print("Hello Again")

def main ():
    #greet()
    #number = int(input("Give me a number 1-10. "))
    #number = int(number) #same as above

    name = input("Give me your name. ")
    print(name.__len__())  #counts length
    print(name.count())    #counts number of letters Both include spaces
    name = name.capitalize()

    singleLetterString = name[0]   #0 being the 1st letter of the name but inputing 
    lastLetterString = name[-1]    #-1 and whatever positive number for the last letter are 2 different things.

    print (singleLetterString)
    print(name[0])

    #numberOfLetters = name.count()
    #isADigit = name.isdigit()
    ##power = math.pow(numberOfLetters, 2)

    ##math.count

    #name.isidentifier()

    
main()