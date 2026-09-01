# keyword arguments = an argument preceded after an identifier help with readibility order of arguments don't matter 
#                     1. positional, 2, default, 3.KEWORD, 4.arbitrary
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
# hello(greeting="Hello", title="Mr.", first="Vishwas", last="Parmar")

def get_phone(country, area, first, last):
    return f"{country}--{area}-{first}-{last}"
phone_num = get_phone(country="+91", area="966", first="48333", last="93")
print(phone_num)