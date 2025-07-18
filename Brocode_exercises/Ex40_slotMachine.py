# Slot machine
import random
import time

def spin_row():
    symbol = ["🍒","🍉","🍋","🔔","⭐"]
    result = [random.choice(symbol) for _ in range(3)]
    return result

def print_row(row):
    print("---------------------")
    print(" | ".join(row))
    print("---------------------")


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0] == "🍒":
            return 2 * bet
        elif row[0] == "🍉":
            return 5 * bet
        elif row[0] == "🍋":
            return 10 * bet
        elif row[0] == "🔔":
            return 15 * bet
        elif row[0] == "⭐":
            return 20 * bet
    return  0
def main():
    balance = 100
    print("*********************************")
    print("-----Welcome to Python Slots-----")
    print("   Symbols : 🍒 🍉 🍋 🔔 ⭐     ")
    print("*********************************")
    while balance >0:
        bet = input("Enter how much you want to bet :")
        if not bet.isdigit():
            print("Please enter the valid amount ")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficiant balance!!")
            continue

        elif bet <= 0:
            print("Amount must be greater than zero!!")
            continue
        balance -= bet
        print(f"Available balance :${balance}")
        row = spin_row()
        print("(Spinning........)")
        time.sleep(0.5)
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You won {payout}")
        else:
            print("Lost your bet")
        balance += payout
        play_again = input("You want to play again (Y/N) :").upper()
        if not play_again=="Y":
            print("--------------------------------------------")
            print(f"Game over,Your final balance is :${balance}")
            print("--------------------------------------------")
            break



if __name__ == "__main__":
    main()

