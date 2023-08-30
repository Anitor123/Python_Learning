fruits = ['Apple','Peach','Pear']
for fruit in fruits:
    print(fruit)


student_heights = input("Input the list of students heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)    

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_student = 0
for students in student_heights:
    number_of_student += 1
print(number_of_student)

average = total_height/number_of_student
round_average = round(average)
print(f"This is the average height of students {round_average}")



student_scores = input("Input the list of students heights: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score is {max_score}")       

for number in range(1,11):
    print(number)



total = 0
for number in range(2,101,2):
    total += number
print(total)    
# OR!!!!!!!!!!!!
total2 =0
for num in range(1,101):
    if num % 2 == 0:
        total += num
print(total)        


for no in range(1,101):
    if no % 5 == 0 and no % 3 == 0:
        print("fizzbuzz")
    elif no % 5 == 0:
        print("buzz")
    elif no % 3 == 0:
        print("fizz")        
    else:
        print(no)     