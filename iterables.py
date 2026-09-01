# # Iterables = An object/collection that can return its elements one at a time, allowing it to be iterable over in a loop
# numbers = [1, 2, 3, 4, 5]
# for number in reversed(numbers):
#     print(number)

my_dictinoary = {"A":1, "B":2, "C":3}
for key, value in my_dictinoary.items():
    print(f"{key}: {value}")