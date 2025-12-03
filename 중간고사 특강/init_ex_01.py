#__init__있을 때
class Counter:
    def __init__(self):
        self.count = 0  # 객체 생성 시 자동 초기화

    def increment(self):
        self.count += 1

    def get(self):
        return self.count


a = Counter()  # 생성자 자동 호출 → a.count = 0
b = Counter()  # 생성자 자동 호출 → b.count = 0

a.increment()
a.increment()
b.increment()

print("a의 count:", a.get())  # 2
print("b의 count:", b.get())  # 1