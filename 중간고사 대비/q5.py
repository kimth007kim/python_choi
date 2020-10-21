while True:
    money = int(input("액수를 입력해주세요"))

    coin500= money // 500
    result= money %500
    print("500원: ",coin500,"개")
    # print(result)
    coin100 = result //100
    result= money %100
    print("100원: ",coin100,"개")
    # print(result)
    coin50 = result //50
    result = money % 50
    print("50원: ",coin50,"개")
    coin10 = result //10
    result = money % 10
    print("10원: ",coin10,"개")
