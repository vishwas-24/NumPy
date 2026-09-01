#   1. Rectangle area calculation
#print("CALCULATE AREA OF RECTANGLE")
#length = float(input("Enter lenght : "))
#width = float(input("Enter width : "))
#area = length * width
#print(f"Area of Rectangle having length {length} and width {width} is {area}")  

#   2. Shopping cart program
item = input("What item would you like to buy : ")
price = float(input("What is the price? : "))
quantity = int(input("How many would you like to buy? : "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")