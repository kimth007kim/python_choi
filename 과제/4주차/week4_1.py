import datetime

now = datetime.datetime.now().year
age = int(input("나이를 입력해주세요: "))

future = 2040 - now + age

print(future)