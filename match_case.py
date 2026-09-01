# Match-case statement (switch) = An alternative to use many  'elif' statements, execute the code if the value match the 'case'
#                                 Benefits : cleaner and syntax is more readalbe 

day = int(input("Enter the day num : "))

def days_of_week(day):
    match day:
        case 1:
            return "It's a Sunday"
        case 2:
            return "It's a Monday"
        case 3:
            return "It's a Tuesday"
        case 4:
            return "It's a Wednesday"
        case 5:
            return "It's a Thrusday"
        case 6:
            return "It's a Friday"
        case 7:
            return "It's a Saturday"
        case _:
            return "Invalid number!"
        
print(days_of_week(day))