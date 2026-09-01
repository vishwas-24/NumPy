# DICTINOARY = A collection of {key:value} pairs ordered and changable. No duplicates

capitals = {"India": "New Delhi", 
            "USA": "Washington D.C.",
            "China": "Beijing",
            "Russia": "Mascow"}
# print(dir(capitals))

# print(capitals.get("India"))

# if capitals.get("Russia"):
#     print("That capital exists.")
# else:
#     print("That capital doesn't exists.")

# capitals.update({"Germany": "Berlin"})

# capitals.pop("China")

# keys = capitals.keys()
# print(keys)

# for keys in capitals.keys():
#     print(keys)

# values = capitals.values()
# print(values)

# for values in capitals.values():
#     print(values)

# items = capitals.items()
# print(items)

# for items in capitals.items():
#     print(items)
for keys, values in capitals.items():
    print(f"{keys}: {values}")
# print(capitals)