enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 2


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
player_strength = 10

def drink_potion():
    global player_strength
    potion_strength = player_strength + 2
    print(potion_strength)
    print(player_strength)


drink_potion()
