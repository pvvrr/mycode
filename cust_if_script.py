#!/usr/bin/env python3


# Develop if elif logic to check the logic


#If logic for grading a student

attainedscore = int(input("Please enter the score got in the exam : "))

if attainedscore <= 59:
    print("Your grade is : ", "F")
elif attainedscore <= 69 and attainedscore > 59:
    print("Your grade is ", "D")
elif attainedscore <= 79 and attainedscore > 69:
    print("Your grade is ", "C")
elif attainedscore <= 89 and attainedscore > 79:
    print("Your grade is ", "B")
elif attainedscore <= 100 and attainedscore > 89:
    print("Your grade is ", "A")
else:
    print(" WARNING !!! Unable to grade the Score")
print ("********************Reached the end")

