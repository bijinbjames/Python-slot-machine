MAX_LINES = 10

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print ("Enter a number grater than 0")
        else:
            print ("Please enter a number.")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Enter a valid number of lines")
        else:
            print ("Please enter a number.")
    return lines





def main():
    balance = deposit()
    lines = number_of_lines()
    print(balance, lines)

main()


