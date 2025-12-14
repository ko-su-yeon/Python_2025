# 파이썬 프로그래밍2 기말과제

#기본 설정
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clean the Ocean") #폰트 설정

clock = pygame.time.Clock() #게임의 프레임 속도 조절하는 도구
font = pygame.font.SysFont(None, 30)

#색상 정의
blue = (0, 150, 200)
white = (255, 255, 255)

#게임 상태 변수
score = 0
pollution = 0
running = True

#플레이어 클래스 (바다 거북)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #바다거북 이미지 가져오기
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        #이미지의 사각형 영역 설정
        self.rect = self.image.get_rect()
        #화면 아래쪽 중앙에 바다거북 배치
        self.rect.center = (WIDTH // 2, HEIGHT -  80)
        #이동 속도
        self.speed = 5

    def update(self):
        #키보드 입력 상태 확인
        keys = pygame.key.get_pressed()

        #좌우 이동
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        #상하 이동
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        #화면 밖으로 나가지 않도록 제한
        self.rect.clamp_ip(screen.get_rect())

#공기 방울 클래스
class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #투명한 surface 생성
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)
        #surface 위에 원 그리기
        pygame.draw.circle(self.image, white, (6,6),6)
        #공기 방울 위치 설정하기
        self.rect = self.image.get_rect(center=(x,y))

        #공기 방울 이동 속도
        self.speed = 8

    def update(self):
        #공기 방울이 위로 이동함
        self.rect.y -= self.speed
        #화면 위로 나가면 자동으로 삭제하기
        if self.rect.bottom < 0:
            self.kill()

#쓰레기 클래스
class Trash(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()

        #쓰레기 종류별 정보
        self.trash_data = {
            "plasticbag" : {"score": 10, "pollution": -2, "image": "plasticbag.png"},
            "plastic" : {"score": 15, "pollution": -3, "image": "plastic.png"},
            "can" : {"score": 20, "pollution": -4, "image": "can.png"},
            "paper" : {"score": 5, "pollution": -1, "image": "paper.png"}
        }

        #쓰레기들 중에 랜덤으로 하나 선택
        self.type = random.choice(list(self.trash_data.keys()))
        data = self.trash_data[self.type]

        self.score_value = data["score"]
        self.pollution_value = data["pollution"]

        self.image = pygame.image.load(data["image"])
        self.image = pygame.transform.scale(self.image, (35, 35))

        self.rect = self.image.get_rect(
            center = (random.randint(20, WIDTH - 20), 0) #x:화면 가로 범위 내에서 랜덤 위치, y:화면 맨 위에서 시작
        )

        self.speed = speed

    def update(self):
        #쓰레기들이 아래로 이동함
        self.rect.y += self.speed

        #바닥에 닿으면 오염도 증가
        if self.rect.top > HEIGHT:
            global pollution
            pollution += 2
            self.kill()

#물고기 클래스
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #물고기 이미지 생성
        self.image = pygame.image.load("fish.png")
        self.image = pygame.transform.scale(self.image, (40, 25))
        
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH - 20), 0)
        )
        #이동 속도
        self.speed = 3

    def update(self):
        #쓰레기들이 아래로 이동함
        self.rect.y += self.speed

        #화면 아래로 나가면 제거
        if self.rect.top > HEIGHT:
            self.kill()

#스프라이트 그룹
all_sprites = pygame.sprite.Group() #화면에 등장하는 모든 스프라이트를 관리하는 그룹
bubbles = pygame.sprite.Group()
trashes = pygame.sprite.Group()
fishes = pygame.sprite.Group()

player = Player() #플레이어(바다거북) 객체 생성
all_sprites.add(player) #플레이어를 전체 스프라이트 그룹에 추가

#게임 종료 메시지 함수
def show_end_message(text):
    screen.fill(blue)
    message = font.render(text, True, white)
    rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, rect)
    pygame.display.update()
    pygame.time.delay(3000) #3초간 화면 유지

#게임 루프
while running:
    clock.tick(60) #초당 최대 60번 루프가 돌도록 제한
    screen.fill(blue)

    #오염도 기반 난이도
    if pollution <= 30:
        trash_speed = 2
        trash_rate = 70
    elif pollution <= 60:
        trash_speed = 4
        trash_rate = 50
    else:
        trash_speed = 6
        trash_rate = 30

    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bubble = Bubble(player.rect.centerx, player.rect.top) #공기 방울이 바다거북 머리 위에서 발사되는 것 처럼 보임
                all_sprites.add(bubble)
                bubbles.add(bubble)

    #쓰레기와 물고기 생성
    if random.randint(1,50) == 1: #1/50 확률로 쓰레기 생성
        trash = Trash(trash_speed)
        all_sprites.add(trash)
        trashes.add(trash)

    if random.randint(1, 120) == 1: #1/120 확률로 물고기 생성
        fish = Fish()
        all_sprites.add(fish)
        fishes.add(fish)

    #업데이트
    all_sprites.update()

    #충돌 처리
    #공기방울과 쓰레기 충돌
    trash_hits = pygame.sprite.groupcollide(trashes, bubbles, True, True)
    for trash in trash_hits:
        score += trash.score_value
        #현재 오염 수치에 쓰레기가 가진 오염 값을 더함
        #계산된 값과 0을 비교하여 더 큰 값을 반환 (오염 수치가 0보다 작아질 수 없음)
        pollution = max(0, pollution + trash.pollution_value)

    #공기방울과 물고기 충돌
    fish_hits = pygame.sprite.groupcollide(fishes, bubbles, True, True)
    if fish_hits:
        score -= 25
        pollution += 5

    #화면 그리기
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, white)
    pollution_text = font.render(f"Pollution: {pollution}", True, white)

    screen.blit(score_text, (10, 10))
    screen.blit(pollution_text, (10, 40))

    #승리, 패배 조건
    if score >= 300 and pollution <= 30:
        show_end_message("Clear!")
        running = False

    if pollution >= 100 or score < 0:
        show_end_message("Game Over")
        running = False

    pygame.display.update()

pygame.quit()