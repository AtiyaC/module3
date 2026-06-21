try:
    x = int(input("Enter a number"))
    print("The number entered is", x)
except ValueError as e:
    print("exception", e)