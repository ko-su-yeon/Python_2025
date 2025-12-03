#접근자/설정자 사용(정상적인경우)
class Friend:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age >= 0:           # 유효성 검사
            self.__age = age
        else:
            print("나이는 음수가 될 수 없습니다.")

x = Friend("홍길동", 20)
x.setAge(-5)   # 잘못된 값 방지
print(x.getAge())  # 20 (변경되지 않음)