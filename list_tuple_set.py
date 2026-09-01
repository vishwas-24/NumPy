# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but add/remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# LIST :
# fruits = ["apple", "banana", "orange", "coconut"]
# print(fruits)
# print(fruits[0])
# print(fruits[0:3])  #[:3] is also valid
# print(fruits[::2])
# print(fruits[::-1]) # revere list
# print(dir(fruits))   # bunch of different methods for List
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")  # add element in end of list
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# print(fruits)

# for x in fruits:
    # print(x, end=" ")


# SET :
# fruits = {"apple", "banana", "orange", "coconut"}
# print(dir(fruits))   # bunch of different methods for List
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits[0])   # Error : 'set' object is not subscriptable (because they are unordered)
# fruits.add("pineapple")   # there is no inserte method in set
# fruits.remove("apple")
# fruits.clear()
# print(fruits)


# TUPLE :
fruits = ("apple", "banana", "orange", "coconut", "coconut")
# print(dir(fruits))   # bunch of different methods for List
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("coconut"))
# print(fruits.count("coconut"))
print(fruits)

for x in fruits:
    print(x, end=" ")