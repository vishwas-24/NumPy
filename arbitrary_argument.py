# *args    = allows to you pass multiple non-key arguments  (tuple)
# **kwargs = allows to you pass multiple keyword arguments (unpackaing operator)    (dictinoary)
#            1. positional, 2, default, 3.keyword, 4.ARVITRARY
# ARGS
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Vishwas", "Parmar")

# KWARGS
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
    
# print_address(house_no="9", stree="JM", town="Dakor", state="Gujarat")

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for kwarg in kwargs.values():
        print(kwarg, end=" ")
    
shipping_lable("Dr.", "Spongbob", "Squarepants", "III",
               houseNo="9", stree="JM", town="Dakor", state="Gujarat")