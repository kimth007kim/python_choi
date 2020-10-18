name = input("생일인 사람 이름: ")

def birthday(name):
    cnt = 1
    for i in range(4):
        if cnt==3:
            print("Happy Birthday, dear",name)
        else:    
            print("Happy Birthday to you!")
        cnt= cnt+1
birthday(name)