# for x in range(1, 10):
#     print(x, end=" ")   # prints on same line

rows = int(input("Enter number of rows : "))
columns = int(input("Enter number of columns : "))
symbol = input("Enter a symbol to use : ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()