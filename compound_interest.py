# PYTHON COMPOUND INTEREST CALCULATOR
principle = 0
rate = 0
time = 0    # in years

while principle <= 0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Principle can't be negative or zero!")

while rate <= 0:
    rate = float(input("Enter the interest rate : "))
    if rate <= 0:
        print("Interest rate can't be negative or zero!")

while time <= 0:
    time = int(input("Enter the time (in years) : "))
    if time <= 0:
        print("Time can't be negative or zero!")

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s : ${total:.2f}")