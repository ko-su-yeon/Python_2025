class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id   # 학번
        self.name = name       # 이름

    def __eq__(self, other):
        # Student 객체끼리만 비교
        if isinstance(other, Student):
            return self.stu_id == other.stu_id  # 학번이 같으면 같은 학생
        return False

# 학생 객체 생성
s1 = Student("202501", "김민수")
s2 = Student("202502", "이수정")
s3 = Student("202503", "박지훈")
s4 = Student("202501", "홍길동")  # 학번이 s1과 같음 (이름 다름)

students = [s1, s2, s3]

print(s1 in students)  # True
print(s2 in students)  # True
print(s3 in students)  # True
print(s4 in students)  # True? False?