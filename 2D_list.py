# 2Dlist = [list1, list2, list3,...]
# fruits =     ["apple", "banana", "orange", "coconut"]   
# vegetables = ["celery", "carrots", "potatos"]
# meats =      ["chicken", "fish", "turkey"]

groceries = [["apple", "banana", "orange", "coconut"], ["celery", "carrots", "potatos"], ["chicken", "fish", "turkey"]]

# print(groceries[2][0])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()