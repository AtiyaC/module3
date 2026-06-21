try:
    num1,num2 = eval(input("Enter 2 numbers seperated by comma"))
    result = num1/num2 
    print("result is", result)
except ZeroDivisionError:
    print("division of 0 is error")
except SyntaxError:
    print("you forget a comma")
except:
    print("invalid input")
else:
    print("0 errors founs")
finally:
    print("this will execute no matter what")