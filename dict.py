student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.


# 🚨 Don't change the code above 👆

student_grades = dict()

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] in range(91,100):
        student_grades[key] = "Outstanding"
    elif student_scores[key] in range(81,90):
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] in range(71,80):
        student_grades[key] = "Acceptable"
    elif student_scores[key] in range(61,70):
        student_grades[key] = "Fail"
    


# 🚨 Don't change the code below 👇
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)

