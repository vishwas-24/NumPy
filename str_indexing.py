credit_no = "1234-5678-9012-3456"
# print(credit_no[0])
# print(credit_no[4])
# print(credit_no[0 : 4]) # 1234
# print(credit_no[5 : 9])
# print(credit_no[5:])
# print(credit_no[-5:])
# print(credit_no[::3])
# last_dig = credit_no[-4:]
# print(f"XXXX-XXXX-XXXX-{last_dig}")
credit_no =credit_no[::-1]  # reverse the string
print(credit_no)