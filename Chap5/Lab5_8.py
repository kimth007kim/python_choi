import random

options=["왼쪽","중앙","오른쪽"]
keep = random.choice(options)

kick=  input("어디를 찰래요? (왼쪽,중앙,오른쪽)")

print("키퍼는 ",keep," 으로 뛰었다!.")
if keep == kick:
    print(" 선방! ")
else:
    print(" 골! ")