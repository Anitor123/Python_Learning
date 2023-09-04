travel_log = [
    {"country": "France", 
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
    },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5,
    },
]

def add_new_country():
    new_country = {}
    new_country["country"] = input("Enter the name of the country: ")
    new_country["cities_visited"] = input("Enter the cities visited (separated by commas): ").split(", ")
    new_country["total_visits"] = int(input("Enter the number of times you visited the country: "))
    travel_log.append(new_country)

add_new_country()
print(travel_log)