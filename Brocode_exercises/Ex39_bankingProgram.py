#Banking Program

def show_balance(balance):
    print(f"current balance is : ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount :$"))
    if amount < 0:
        print("Invalid number!")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("How much You want to withdraw :$"))

    if amount > balance:
        print("Insufficient balance!")
        return 0
    elif amount < 0:
        print("Must be greater than 0")
        return 0
    else:
        return amount


balance =0
is_running =True

while is_running:
    print("----------------------------")
    print("      Banking Program       ")
    print("----------------------------")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Ext")
    print("----------------------------")
    choice = input("Enter your choice(1-4) :")

    if choice =="1":
        show_balance(balance)
    elif choice=="2":
        balance += deposit()
    elif choice=="3":
        balance -= withdraw(balance)
    elif choice=="4":
        is_running=False
        print("----------------------------")
        print("Have a nice day sir/mam")
    else:
        print("Invalid input!")
