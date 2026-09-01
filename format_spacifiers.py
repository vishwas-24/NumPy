price1 = 3.14159
price2 = -9870.65
price3 = 12.34
print(f"Price 1 is ${price1: ,.2f}")   # .2f (format spacifier) digits after decimal point 
print(f"Price 2 is ${price2: ,.2f}")   # 10 is spacec to be print 
print(f"Price 3 is ${price3: ,.2f}")   # 010 is same but padded with 0s
                                   # <10 is all the num are left justifed same (>10 for right) and (^ for center)
                                   # , each thousands place will print , 