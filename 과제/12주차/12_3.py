# TV 객체를 생성하는 프로그램을 작성하시오.

class TV:
    def __init__(self,channel,volume,on):
        self.channel=1
        self.volume=volume
        self.on=on

    def turnOn(self):
        self.on= "on"

    def turnOff(self):
        self.on= "off"
   
    def setChannel(self):
        self.channel = 11

    def setVolume(self):
        self.volume = 6

    def __str__(self):
        msg = "채널:"+str(self.channel)+" 채널:"+ str(self.volume)+ " 전원:"+str(self.on)
        return msg

newTV = TV(1,1,"off")
print("메소드 실행전")
print(newTV)
newTV.setChannel()
newTV.setVolume()
newTV.turnOn()
print("메소드 실행후")
print(newTV)
