#this is an app that makes one to deposit money and gamble to win
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {"A":2,"B":4,"c":6,"d":8}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    

def deposit():
    while True:# while loop to enable iteration until successful attempt
        amount = input("Enter Amount your want to deposit:$")
        if amount.isdigit():#checks if the amount is a digit
            amount = int(amount)#to convert into interger 
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")
    return amount
def get_number_of_lines():
    while True:# while loop to enable iteration until successful attempt
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)#to convert into interger 
            if 1<= lines <= MAX_LINES:#to check number of lines to be on
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number")
    return lines
def get_bet():
    while True:# while loop to enable iteration until successful attempt
        amount = input("Enter Amount your want to bet on each line:$")
        if amount.isdigit():
            amount = int(amount)#to convert into interger 
            if  MIN_BET<= amount <= MAX_BET :#to check if the amount is between the min or max amount needed
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number")
    return amount
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet > balance:
            print(f"You do not have enough amount to be on. Your current balance is:${balance}")
        else:
            break     
    print(f"You are betting ${bet} on {lines}.The total bet is: ${total_bet}")
    
main()#to call the main