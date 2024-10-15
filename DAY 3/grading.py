#Grading System with Extra Credit
#Question:
#Write a Python program that takes three inputs from the user:

#score (an integer representing the exam score between 0 and 100).
#attendance (a percentage representing attendance).
#extra_credit (a boolean input representing whether the student has extra credit or not).
#The program should determine the final grade based on the following conditions:

#If the score is above 90:
#If the attendance is above 85%, print "A+"
#If the attendance is between 75% and 85%, print "A"
#If the attendance is below 75%, print "A-"
#If the score is between 70 and 90:
#If extra_credit is True, add 5 points to the score.
#After adding the extra points:
#If the new score is above 90, print "A"
#If the new score is between 70 and 90, print "B+"
#If the new score is below 70, print "B"
#If the score is below 70:
#If extra_credit is True, print "C for effort"
#If extra_credit is False, print "C, needs improvement"

score = int(input('Enter the score: '))
attendance = int(input('Enter the attendance percentage: '))
extra_credit = input('Does the student have extra credit? Type Y or N: ').lower()

# Initialize new_score to the original score
new_score = score

if score > 90:
    if attendance > 85:
        print('A+')
    elif 75 <= attendance <= 85:
        print('A')
    elif attendance < 75:
        print('A-')
elif 70 <= score <= 90:
    if extra_credit == 'y':
        new_score = score + 5
    if new_score > 90:
        print('A')
    elif 70 <= new_score <= 90:
        print('B+')
    else:
        print('B')
elif score < 70:
    if extra_credit == 'y':
        print('C for effort')
    elif extra_credit == 'n':
        print('C, needs improvement')
