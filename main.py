import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 3,
  "B": 6,
  "C": 9,
  "D": 12
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    # get a copy of all_symbols
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    
    columns.append(column)
  
  return columns

def display(columns):
  # A B C
  # -----
  # A B C
  # -----
  # A B C
  # to
  # A | A | A
  # B | B | B
  # C | C | C

  for row in range(len(columns[0])):
    for i, column in enumerate( columns ):
      if i != len(columns) -1:
        print(column[row], end=" | ")
      else:
        print(column[row])

def deposit():
  while True:
    amount = input("Please put money in the machine! $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please enter a positive number")
    else:
      print("Invalid amount! Try again")
  
  return amount

def get_number_of_line():
  while True:
    amount = input("Please enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
    if amount.isdigit():
      amount = int(amount)
      if 0 < amount and amount <= MAX_LINES:
        break
      else:
        print("The number must be from 1 to " + str(MAX_LINES))
    else:
      print("Invalid amount! Try again")
  
  return amount

def get_user_bet():
  while True:
    amount = input("How much would you like to bet on each line? $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount and amount <= MAX_BET:
        break
      else:
        print("The bet must be between $" + str(MIN_BET) + " to $" + str(MAX_BET))
    else:
      print("Invalid amount! Try again")
  
  return amount

def check_winnings(columns, lines, bet, values):
  winning = 0
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winning += values[symbol] * bet
  
  return winning

def spin(balance):
  line = get_number_of_line()
  while True:
    bet = get_user_bet()
    total = line * bet

    if total > balance:
      print(f"You do not have enough to bet, your current balance is ${balance}")
    else:
      break
  
  print(f"You are betting ${bet} on {line} lines. Total bet is ${total}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  display(slots)
  winnings = check_winnings(slots, line, bet, symbol_value)
  print(f"You won ${winnings}")
  return winnings - total

def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    answer = input("Press enter to play, x to exit.")
    if answer == "x":
      break
    balance += spin(balance)
  
  print(f"You left with ${balance}")


main()