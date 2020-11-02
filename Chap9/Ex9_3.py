contracts = { }

while True:
    name = input("(입력모드)이름을 입력하시오: ")
    if not name:
        break
    tel = input("전화번호를 입력하시오: " )
    contracts[name] =tel
while True:    
    name2= input("(검색모드)이름을 입력하시오: ")
    if name2 in contracts:
        print(name2,"의 전화번호는 ", contracts[name2])
    else:
        print("존재하지 않음")