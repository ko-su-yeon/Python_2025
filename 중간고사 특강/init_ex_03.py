class Student:
    def __init__(self, name, stu_id):
        # 생성자: 객체 생성 시 자동 실행됨
        self.name = name           # 학생 이름
        self.stu_id = stu_id  # 학번
        self.att = 0        # 출석 횟수 초기값

    def attend(self):
        # 출석 시 출석 횟수 1 증가
        self.att += 1

    def get_info(self):
        # 학생 정보 출력용 메서드
        return f"{self.stu_id} {self.name} - 출석 {self.att}회"


# 학생 객체 생성 (__init__ 자동 호출)
s1 = Student("김민수", "202501")
s2 = Student("이수정", "202502")

# 출석 체크
s1.attend()
s1.attend()
s2.attend()

# 학생 정보 출력
print(s1.get_info())  # 202501 김민수 - 출석 2회
print(s2.get_info())  # 202502 이수정 - 출석 1회