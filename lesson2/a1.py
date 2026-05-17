def total_calc(bill_amount,tip_percentage):
    tip_amount = (tip_percentage/100)*bill_amount
    total_amount = bill_amount+tip_amount
    print("please pay",total_amount)

total_calc(100,20)
total_calc(150,15)