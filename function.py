# # function = A block of reusable code place () after the function name to invoke it
# def happy_birthday(name):
#     print(f"Happy Birthday to {name}")
#     print("You are old!")  
#     print("Happy Birthday to you")
#     print()
# happy_birthday("Bro")
# happy_birthday("STeve")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill is ${amount:.2f} is due: {due_date}")
    print()
display_invoice("Vishwas", 190, "15/12/25")
display_invoice("STeve", 210, "12/1/25")