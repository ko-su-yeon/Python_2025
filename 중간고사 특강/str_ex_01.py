class Car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self): # __str__ : 객체를 문자열로 표현할 때 자동 호출됨
        return f"속도: {self.__speed}\n기어: {self.__gear}\n색상: {self.__color}"

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.setColor("red")

print(myCar) # 출력