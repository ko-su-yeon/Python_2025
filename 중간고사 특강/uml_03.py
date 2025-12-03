# 부모 클래스
class User:
    def __init__(self, user_id: int, name: str):
        self.__id = user_id       # private 속성
        self.__name = name        # private 속성

    def getTodo(self):
        return print("ToDo 객체를 반환하는 메서드") 

    def write(self, text: str) -> None:
        print(f"{self.__name}이(가) 글 작성: {text}")

# 자식 클래스 1: Student
class Student(User):
    def study(self) -> None:
        print("학생 공부")

# 자식 클래스 2: Teacher
class Teacher(User):
    def teach(self) -> None:
        print("선생님 수업")

student = Student(1, "김민수")
teacher = Teacher(2, "이수정")

student.write("열심히 공부해야지!") 
student.study()

teacher.write("오늘은 상속 개념을 가르쳤습니다.")
teacher.teach()