# print("\n줄 바꿈\n 연습 ")
# print("\t탭 키 \t연습")
# print("글자가 \"강조되는\"되는 효과1")
# print("글자가 \'강조되는\'되는 효과2")
# print("\\\\\\ 역슬래시 세 개 출력")
# print(r"\n\t \" \\를 그대로 출력")
# print("\n\t \" \\를 그대로 출력")
# print("'그대로 출력")
# print('"그대로 출력')

sel = int(input("입력 진수 결정(16/10/8/2): "))
if sel != 16 and sel != 10 and sel != 8 and sel != 2:
    print('16 10 8 4 2중에 하나 적으라고 쫌!')
    exit()
num = input("값 입력: ")

if(sel == 16):
    num10 = int(num,16)
if(sel == 10):
    num10 = int(num,10)
if(sel == 8):
    num10 = int(num,8)
if(sel == 2):
    num10 = int(num,2)

print("16진수 ==> ",hex(num10))
print("10진수 ==> ",num10)
print("8진수 ==> ",oct(num10))
print("2진수 ==> ",bin(num10))