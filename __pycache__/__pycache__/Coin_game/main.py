import coin

def main():
    my_coin = coin.Coin()

    print("This side is up:", my_coin.get_sideup())

    print("I am goiing to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())



main()        