#Q1
def add (number , another_number):
    return number + another_number
answer = add(24,5)
print(answer)

#Q2
import random
random_number= random.randint(0 ,-99)
print(random_number)

#Q3
number = 0
while(number < 4):
    print("Today, I am outstanding in every way")
    number = number +1

#Q4
for number in range(200):
    print("I become what I think about most of the time")

#Q5
user_name = input("Enter your name:  ")
print( "You look great today", user_name)

#Q6
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_length = len(alphabet)
print(alphabet_length)

#Q7
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_j = alphabet.find("j")
print(alphabet_j)

#Q8
from array import array
final_exam = array("i",[98,99,100,89])

#Q9
final_exam = final_exam.append(100)

#Q10
final_exam_length = len(final_exam)
print(final_exam_length)

#Q11
IGCSE_computer_science_student_names = ["Yujing","Barbie","Angelina","Howard","Arsalon"]

#Q12
IGCSE_computer_science_student_names.remove("Arsalon")

#Q13
computer_science_sort_list =IGCSE_computer_science_student_names.sort()

print(computer_science_sort_list)

#Q14
three_exam_score = {
    "Angelina":[99,98,98],
    "Yujing":[99,98,98],
    "Barbie":[99,98,98],
    "Arsalon":[99,100,99]
}

#Q15
Arsalon_three_exam_score = three_exam_score.get("Arsalon")
print(Arsalon_three_exam_score)