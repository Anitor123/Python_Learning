programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

empty_dicitionary = {}

#programming_dictionary ={}
#print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) 


caiptals ={
    "France": "Paris",
    "Germany": "Berlin",
}    

# Nesting a list in a dicitonary
travel_log = {
    "France":{"cities_visited":["Paris","Lille","Djion"], "total_visits": 12},
    "Germany":{"cities_visited": ["Berlin","Hamburg","Stuttgart"], "total_visits": 5,},
}

#["A","B",["C",'D']]
# Nesting a Dictionary in a Dictionary is above
# Nesting Dicitionary in a list
travel_log = [
    {"country":"France", 
     "cities_visited":["Paris","Lille","Djion"],
     "total_visits": 12,
    },
    {"country":"Germany",
     "cities_visited": ["Berlin","Hamburg","Stuttgart"],
     "total_visits": 5,
    },
]
