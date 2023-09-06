import random

should_continue =True
list_num = [11,2,3,4,5,6,7,8,9,10,10,10,10]
first_user_choice = random.choice(list_num)
second_user_choice = random.choice(list_num)
first_comp_choice = random.choice(list_num)
second_comp_choice = random.choice(list_num)
user_list =  [first_user_choice ,second_user_choice]
comp_list = [first_comp_choice, second_comp_choice]

user_total = sum(user_list)
comp_total = sum(comp_list)
print(f"{user_total} {comp_total}")
print(user_list)
print(comp_list)

while user_total < 21 or comp_total < 21:
    user_list = user_list + [random.choice(list_num)]
    comp_list = comp_list + [random.choice(list_num)]
    user_total = sum(user_list)
    comp_total = sum(comp_list)

print(user_list)
print(comp_list)

if user_total >= 21:
    print("Computer Wins!!!")
elif user_total == comp_total:
    print("Draw")
elif comp_total >= 21:
    print("User Wins")    
  

    


                       

    

