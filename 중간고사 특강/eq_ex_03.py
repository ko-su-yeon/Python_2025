#중복 이메일 체크
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __eq__(self, other):
        return self.email == other.email  # 이메일이 같으면 같은 회원

u1 = User("jane", "jane@korea.korea")
u2 = User("jennie", "jane@korea.korea")

if u1 == u2:  # True
    print("중복된 이메일 입니다")