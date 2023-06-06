#this is an app that makes one to deposit money and gamble to win
import random
import tkinter as tk# this module facilitates the creation for a GUI(graphical user interface )
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {"A":2,"B":4,"c":6,"d":8}
symbol_value = {"A":5,"B":4,"c":3,"d":2}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break#this checks if someone did not win then a loop start again,,because the symbol chosen must the same with the one in the column for someone to win
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)#give the line which the gamer won on
    return winnings, winning_lines    
def get_slot_machine_spin(rows,cols,symbol):
    all_symbols = []
    for symbol,symbol_count in symbol.items(): #the loop to iterate through the dictionary created
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []#this formulates values in the columns which is initially empty
    for _ in range(cols):# the _ is used to enable unlimited iterations of values
        column = []#this is empty list for generation of the columns in the slot machine for the values being picked
        current_symbols = all_symbols[:]#the slice operator (:) is used to ensure that the contents are not overwritten
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)#to remove the firts instance so that the value cannot be choosen again
            column.append(value)#to add the value to the column
        columns.append(column)#adds the column to the columns list that exists alread
    return columns
def print_slot_machine(columns):#this functions aid in fliping the raws to colums while printing or outputing it because the columns are initially printed in a row format
    for row in range(len(columns[0])):#zero is added to ensure there is always one colume before iteration otherwise it will crush
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],end=" | ")#the last column to be printed will not be separated by the column
            else:
                print(column[row],end="")
        print()#this is empty print statement to takes us to next new line 
    
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
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet > balance:
            print(f"You do not have enough amount to be on. Your current balance is:${balance}")
        else:
            break     
    print(f"You are betting ${bet} on {lines}.The total bet is: ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)#function that show how the columns should be printed out
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You have won ${winnings}")
    print(f"You have won on lines:", *winning_lines)#the * is used to give all the lines that the gamer won on
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"The current balance is ${balance}")
        answer = input("Press enter to spin again(and q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")

main()#to call the main
# The following codes helps in creation of the GUI - Graphical User Interface
def spin_button_clicked():
    balance_var.set(spin(int(balance_var.get())))

def deposit_button_clicked():
    amount = deposit()
    balance_var.set(amount)

# Create the main window
window = tk.Tk()
window.title("Slot Machine App")

# Create and position the GUI elements
balance_label = tk.Label(window, text="Current Balance:")
balance_label.pack()

balance_var = tk.StringVar()
balance_var.set("0")
balance_display = tk.Label(window, textvariable=balance_var)
balance_display.pack()

spin_button = tk.Button(window, text="Spin", command=spin_button_clicked)
spin_button.pack()

deposit_button = tk.Button(window, text="Deposit", command=deposit_button_clicked)
deposit_button.pack()

# Run the main GUI event loop
window.mainloop()
