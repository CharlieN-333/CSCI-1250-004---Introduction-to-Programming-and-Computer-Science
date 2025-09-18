name = "name"
name2 = "name"

print(name == name2)  #True despite the data being 2 different things and in 2 different places

age = 15        # Most of the below hinges on this integer

if(age > 15):   # if age is 15 this would be false
    print("You can ride.")

name = name.lower()     # Nothing would run if this was false without and else
if(name.islower()):
    print("Name is lower.")

if(age >= 15):
    print("You can ride.")
else:
    print("You can't ride.")

allowed = True
parent = True
if(age >= 15):
    print("You can ride.")
elif(age < 10 and parent or allowed):  # parent is true so automatically it applies here, if parent was false it would go to the else part. 
    print ("You can ride with a parent.")   #the "or" makes it that regardless if "allowed" nothing else would matter so it would print this line
else:
    print("You can't ride.")

x = 9
while(x > 0):
    print(x)    # Most infinite loops will crash your computer so don't do it unless it is required or intentional.
    x -= 1

total = 0
count = 0   # all of these need be be outside the loop for it to function
userInput = 0
while(userInput >=0):
    userInput = int(input("enter any number numbers to average and -1 to exit "))
    if(userInput != -1):
        total += userInput
        count += 1

print(f"Your average is {total/count}. ") 

numbers = [100, 90, 80, 70, 60, 50]
total2 = 0
for n in numbers:   # Counts down the list
    total2 += n

for i in range(5):
    print("Hello.")     # Prints hello until i = 5?

