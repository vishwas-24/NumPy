# List comparishension = A concise way to create list in python, compact and easier to read than traditional loops 
#                        [expression for value in itrable if condition]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(doubles)
# print(triples)
# print(squares)

# fruits = ["apple", "banana", "orange", "coconut"]
# fruits = [fruit.capitalize

numbers = [1, -2, 3, -4, 5, -6, 7, 8]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num <= 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0]
print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)