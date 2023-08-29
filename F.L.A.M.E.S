# F.L.A.M.E.S
def calculate_flames_count(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    flames = ["f", "l", "a", "m", "e", "s"]

    for char in name1:
        if char in name2:
            name2 = name2.replace(char, "", 1)
            name1 = name1.replace(char, "", 1)

    count = len(name1) + len(name2)
    return count


def get_relationship(count):
    relationship = [
        "Friends",
        "Lovers",
        "Acquaintances",
        "Married",
        "Enemies",
        "Siblings",
    ]
    index = (count % 6) - 1
    return relationship[index]


def play_flames():
    print("Welcome to the FLAMES game!")
    print("Please enter two names to check their relationship.")
    name1 = input("Your Name: ")
    name2 = input("Crush's Name: ")

    count = calculate_flames_count(name1, name2)
    relationship = get_relationship(count)

    print(f"\n{name1} and {name2} are {relationship}!")


play_flames()
