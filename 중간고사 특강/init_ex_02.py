class Counter:
    # 생성자가 없음
    def increment(self):
        self.count += 1

    def get(self):
        return self.count

a = Counter()
b = Counter()

a.count = 0 # 직접 속성을 만들어야 함
b.count = 0

a.increment()
a.increment()
b.increment()

print("a의 count:", a.get())  # 2
print("b의 count:", b.get())  # 1