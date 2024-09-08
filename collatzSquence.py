def collatz(number):
    if number % 2:
        newNumber = 3 * number + 1
    else:
        newNumber = number // 2
    print(newNumber)
    return newNumber

while True:
    try:
        inputNumber = int(input("Please enter an interger number: "))
        break
    except ValueError:
        print("User didn't enter an interger.")
        continue

while inputNumber != 1:
    inputNumber = collatz(inputNumber)