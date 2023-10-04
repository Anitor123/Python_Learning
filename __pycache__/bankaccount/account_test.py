import bankaccount

def main():
    start_bal = float(input("Enter your starting balance: "))

    savings = bankaccount.BankAccount(start_bal)

    pay = float(input("How much were you paid ths week? "))
    print("I will deposit that into your account. ")
    savings.deposit(pay)

    print(f"Your account balance is $ {savings.get_balance()}")

    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account. ")
    savings.withdraw(cash)

    print(f"Your account balance is ${savings.get_balance()}")


main()    