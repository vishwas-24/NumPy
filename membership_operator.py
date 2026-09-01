# Membership operator = used to test wheter a value or variable is found in a sequence (string, list, tuple, set or dicnoary) 
#                       1.in    2.not in    
# word = "APPLE"
# letter = input("Guess a letter in the secret word : ").upper()

# if letter in word:
#     print(f"There is a {letter} in secret word.")
# else:
#         print(f"{letter} was not found in secret word.")

# students = {"Steve", "Vishwas", "Jeet", "Jay", "Jainish", "Deep"}
# student = input("Enter name of student : ").capitalize()

# if student in students:
#     print(f"{student} is a student.")
# else:
#     print(f"{student} is not a student.")

email = "vishwas@gmailcom"
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")