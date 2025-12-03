# 부모 클래스
class Animal:
    def __init__(self, age: int, gender: str):
        self.age = age
        self.gender = gender

    def isMammal(self) -> None:
        print("이 동물이 포유류인지 확인합니다.")

    def introduce(self, name: str) -> None:
        print(f"이름:{name}, 나이:{self.age}, 성별:{self.gender}")

# 자식 클래스 1 : Duck
class Duck(Animal):
    def __init__(self, age: int, gender: str, beakColor: str = "yellow"):
        # 부모 클래스 생성자 호출
        super().__init__(age, gender)
        self.beakColor = beakColor

    def swim(self) -> None:
        print("첨벙첨벙")

    def quak(self) -> None:
        print("꽥꽥!")

# 자식 클래스 2 : Fish
class Fish(Animal):
    def __init__(self, age: int, gender: str, sizeInFt: int):
        super().__init__(age, gender)
        self.sizeInFt = sizeInFt

    def swim(self) -> None:
        print("물고기가 헤엄치고 있습니다.")

# 객체 생성 및 실행
duck = Duck(2, "암컷")
fish = Fish(1, "수컷", 3)

duck.introduce("오리")
duck.quak()
duck.swim()

fish.introduce("물고기")
fish.swim()