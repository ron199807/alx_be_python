#prompt user to enter a number
number = int(input("Enter a number to see its multiplication table:"))
for i in range(1, 11):
    numbers = number * i
    print(f"{number} * {i} = {numbers}")


