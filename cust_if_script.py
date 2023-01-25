#!/usr/bin/env python3


# Develop if elif logic to check the logic


#If logic for grading a student

attainedscore = int(input("Please enter the score got in the exam : "))

if attainedscore <= 59: # Grading (59 and below) F
    print("Your grade is : ", "F")
elif attainedscore <= 69 and attainedscore > 59: # Grading (69 to 60) D
    print("Your grade is ", "D")
elif attainedscore <= 79 and attainedscore > 69: # Grading (79 to 70) C
    print("Your grade is ", "C")
elif attainedscore <= 89 and attainedscore > 79: # Grading (89 to 80) B
    print("Your grade is ", "B")
elif attainedscore <= 100 and attainedscore > 89: # Grading (100 to 90) A
    print("Your grade is ", "A")
else: # unabel to grade hence displaying Warning
    print(" WARNING !!! Unable to grade the Score")
print ("********************Reached the end")

