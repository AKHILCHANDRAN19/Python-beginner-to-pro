#University Admission System
#Question: A university has different criteria for admitting students based on their scores in Math, Science, and English:

#The student must have an average score of at least 70 to be considered.
#If the average score is between 70 and 85, the student is admitted if they have scored at least 75 in Math.
#If the average score is above 85, they are admitted directly unless they have scored below 60 in any subject.
#If a student scores above 90 in all three subjects, they receive a scholarship.


# Solution
math_score = int(input("Enter Math score: "))
science_score = int(input("Enter Science score: "))
english_score = int(input("Enter English score: "))

# Calculate the average score.
average_score = (math_score + science_score + english_score) / 3

# Check if the average score is at least 70.
if average_score >= 70:
    # Check if the average is between 70 and 85.
    if 70 <= average_score <= 85:
        if math_score >= 75:
            print("Student is admitted based on average and Math score.")
        else:
            print("Student is not admitted due to low Math score.")
    
    # Check if the average is above 85.
    elif average_score > 85:
        if math_score >= 60 and science_score >= 60 and english_score >= 60:
            print("Student is admitted with high average score.")
        else:
            print("Student is not admitted due to a score below 60 in a subject.")
    
    # Check if the student qualifies for a scholarship.
    if math_score > 90 and science_score > 90 and english_score > 90:
        print("Student is awarded a scholarship.")
else:
    print("Student is not admitted due to low average score.")

