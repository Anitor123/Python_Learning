for item in ["Josh", "Sarah", "John"]:
    print(item)
for item in [1, 2, 3, 4]:
    print(item)
for item in range(14):
    print(item)
for item in range(5,10):
    print(item)
for item in range(5,14,2):
    print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total+=price
print(f"Total = {total}")

# Printing out coordinates
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


# Printing an L using x
numbers = [1,1,1,1,5]
for x_count in numbers:
    l_shape =""
    for count in range(x_count):
        l_shape +="x "
    print(l_shape)

# Program to find largest number in List
numbers = [1,5,3,7,66,7,45,7,898,356,5667,78789]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


# 2D Lists
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]    
print(matrix[0])
print(matrix[0][0])
matrix[0][0]= 20
print(matrix[0][0])
for row in matrix:
    print(row)
    for item in row:
        print(item)


# Program to remove duplicates in a list
numbers =[2,2,4,6,3,4,6,1]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)        


# Program to find the descending order of the list using a loop
numbers = [1,4,50,80,12]

for i in range(0, len(numbers)):    
    for j in range(i+1, len(numbers)):    
        if(numbers[i] < numbers[j]):    
            temp = numbers[i]   
            numbers[i] = numbers[j];    
            numbers[j] = temp 

print(numbers)


# Python program to find the list of words that are longer than n from a given list of words.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))



page =" sreing is here broo"
txt = str.split(page)# splits sting into separate substrings in a list
print(txt)



# Tuples
numbers = (1,2,3)
print(numbers[0])

coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# OR!!!!!!!!!!!!!!!!!
# It can also be used in lists
x,y,z = coordinates


# Dictionaries