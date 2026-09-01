# default arguments = A default values for certain parameters default is used when that argument is omitted make your function more 
#                     fexible, reduce # of the arguments 1. positional, 2, DEFAULT, 3.keyword, 4.arbitrary
def net_price(list_price, dicsout = 0, tax = 0.05):
    return list_price * (1 - dicsout) * (1 + tax)

print(net_price(500))