# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(P,Q):
    result = P+Q
    return result
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def subtract(P,Q):
    result = P-Q
    return result
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def multiply(P,Q):
    result = P*Q
    return result
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def divide(P,Q):
    result = P/Q
    return result
# 5) Display a menu to the user showing the available operations:
#    a) Add
#    b) Subtract
#    c) Multiply
#    d) Divide
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")
# 6) Take the user's choice as input and store it in `choice`.
choice = input("Enter a choice, a, b, c, d").lower()

# 7) Take two integer inputs from the user:
#    a) Store the first number in `num_1`
#    b) Store the second number in `num_2`
num_1 = int(input("Enter the first number"))
num_2 = int(input("Enter the second number"))
# 8) Use conditional statements to perform the chosen operation:
#    a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
#    b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
#    c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
#    d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.
if choice == "a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == "b":
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice == "c":
    print(num_1,"x",num_2,"=",multiply(num_1,num_2))
elif choice == "d":
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
# 9) If the user enters anything other than a/b/c/d, print an invalid input message.
else:
    print("Invalid input")