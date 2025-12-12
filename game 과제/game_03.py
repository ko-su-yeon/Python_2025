# + 본인의 아이디어 아무거나 추가 (주석달기)
# 난이도 선택 버튼 추가 (easy, normal, hard)

from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1) 

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

#난이도별 공 속도를 저장하는 변수
#기본 normal 속도
ball_speed = 3

class Ball:
    def __init__(self, canvas, paddle, color): 
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100)

        #공이 시작할 때 x방향 랜덤 속도
        starts = [-ball_speed, ball_speed]
        self.x = random.choice(starts)

        #y 시작  속도 (위로 올라감)
        self.y = -ball_speed

        self.canvas_height = self.canvas.winfo_height() 
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False  

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) 

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      

        if pos[1] <= 0:
            self.y = 3 
        if pos[3] >= self.canvas_height:  
            self.hit_bottom = True 

        
        if not self.hit_bottom:
            if self.hit_paddle(pos):
                self.y = -ball_speed

        if pos[0] <= 0: 
            self.x = 3
        if pos[2] >= self.canvas_width: 
            self.x = -3

class Paddle: 
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0 
        self.canvas_width = self.canvas.winfo_width() 
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) 
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2   

    def turn_right(self, evt):
        self.x = 2   

    def draw(self): 
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

def restart_game():
    global ball, paddle
    canvas.delete("all")
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
    game_loop()

def game_loop():
    global ball, paddle

    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
        else:
            canvas.create_text(250, 150, text="GAME OVER", fill="black", font=("Arial",40))
            restart_btn = Button(tk, text="Restart", command=restart_game)
            canvas.create_window(250, 250, window=restart_btn)
            break

        tk.update_idletasks() 
        tk.update() 
        time.sleep(0.01)

#난이도 선택 화면
def set_difficulty(speed):
    global ball_speed
    ball_speed = speed #선택된 속도로 설정

    #난이도 버튼 화면 제거
    canvas.delete("all")

    #게임 시작
    start_game()

def start_game():
    global ball, paddle
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
    game_loop()

# 첫 화면: 난이도 선택 UI
canvas.create_text(250, 100, text="Select Difficulty", font=("Arial", 28))

easy_btn = Button(tk, text="EASY", width=10, command=lambda: set_difficulty(2))
normal_btn = Button(tk, text="NORMAL", width=10, command=lambda: set_difficulty(3))
hard_btn = Button(tk, text="HARD", width=10, command=lambda: set_difficulty(5))

canvas.create_window(250, 170, window=easy_btn)
canvas.create_window(250, 220, window=normal_btn)
canvas.create_window(250, 270, window=hard_btn)

tk.mainloop()