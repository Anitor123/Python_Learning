dictionary = {
    "apple": "A fruit with red or green skin and a crisp texture.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice.",
    "python": "A high-level programming language known for its readability and simplicity.",
    "book": "A written or printed work consisting of pages glued or sewn together along one side and bound in covers.",
    "sun": "The star around which the earth orbits, providing light and heat to the planet.",
    "tree": "A woody perennial plant typically having a single trunk growing to a considerable height.",
    "ocean": "A very large expanse of sea, in particular, each of the main areas into which the sea is divided geographically.",
    "music": "Vocal or instrumental sounds combined in such a way as to produce beauty of form, harmony, and expression of emotion.",
    "computer": "An electronic device that is capable of accepting data, performing operations on that data, and presenting the results.",
    "journey": "An act of traveling from one place to another, especially when involving a considerable distance."
}

favorites = []

def search_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found in dictionary."

def add_to_favorites(word):
    if word in dictionary and word not in favorites:
        favorites.append(word)
        return "Word added to favorites."
    elif word in dictionary and word in favorites:
        return "Word is already in favorites"
    else:
        return "Word not found in dictionary."

# Main loop
while True:
    print("Dictionary App")
    print("1. Search for word")
    print("2. Add word to favorites")
    print("3. View favorites")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        search_word_input = input("Enter word to search: ")
        definition = search_word(search_word_input)
        print(definition)
    
    elif choice == "2":
        add_fav_input = input("Enter word to add to favorites: ")
        result = add_to_favorites(add_fav_input)
        print(result)
    
    elif choice == "3":
        print("Favorites:")
        for word in favorites:
            print(word)
    
    elif choice == "4":
        print("Exiting the Dictionary App. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a valid option.")