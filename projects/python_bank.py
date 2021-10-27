running = True
money_in_account = 0.00
while running:
    
    user_input = input("Please select from the following menu options: \n (B)alance \n (D)eposit \n (W)ithdraw \n (Q)uit\n").lower()

    def withdraw(amount):
        global money_in_account
        money_in_account = float(money_in_account - amount)
        money = "{:.2f}".format(money_in_account)
        print(f"Here is your ${amount}. You have ${money} left in your account.")


    def deposit(amount):
        global money_in_account
        money_in_account = float(money_in_account + amount)
        money = "{:.2f}".format(money_in_account)
        print(f"You have deposited ${amount} to your account. Your account has ${money}.")

    def balance(money):
        global money_in_account
        money = "{:.2f}".format(money_in_account)
        print(f"You have ${money} in your account.")

    if user_input == "b":
        balance(money_in_account)

    elif user_input == "d":
        deposit_amount = float(input("How much money would you like to deposit? "))
        deposit(deposit_amount)

    elif user_input == "w":
        withdraw_amount = float(input("How much money would you like to withdraw? "))
        if money_in_account - withdraw_amount < 0:
            money = "{:.2f}".format(money_in_account)
            print(f"You only have ${money} in your account. You cannot withdraw ${withdraw_amount}.")
        else:
            withdraw(withdraw_amount)

    elif user_input == "q":
        print("Have a nice day!")
        running = False

    else:
        user_input

