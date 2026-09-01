import random
low = 1
high = 100
options = ("rock", "paper", "scissors")     # tuple
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]   # list
# number = random.randint(low, high)   # for random integer number
# number = random.random()    # for random floating point number between 0 and 1
# option = random.choice(options)     # choice is used to select random element
# card = random.choice(cards)
random.shuffle(cards)
print(cards)