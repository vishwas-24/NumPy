# Exception = An event that intrruptes the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number : "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by Zero, IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something Went Wrong!")
finally:
    print("Do some cleanup here")