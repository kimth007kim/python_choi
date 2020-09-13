number =  int(input("정수를 입력하세요: "))

r = number //1000
first = r
new1 =number- r*1000

r= new1//100
second=r
new2 = new1- r*100

r= new2//10
third=r
new3 = new2- r*10
forth = new3


print("자리수의 합: ",first+second+third+forth)
