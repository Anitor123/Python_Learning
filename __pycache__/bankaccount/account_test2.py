import bankaccount2

def main():
    start_bal = float(input("Enter your starting balance: "))
    savings = bankaccount2.BankAccount(start_bal)
    pay = float(input("How much were you paid this week? "))
    savings.deposit(pay)

    print(savings)

   

    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account. ")
    savings.withdraw(cash)

    print(savings)


main()
