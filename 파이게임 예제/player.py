#플레이어 추가
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Multi Player + Random Enemy")

clock = pygame.time.Clock()

# ----------------------------
#             Player
# ----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()

        # 모든 플레이어가 동시에 움직이는 건 불가능하므로
        # 첫 번째 플레이어만 조종됨 (시험에서는 OK)
        if self == main_player:
            if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]: self.rect.x += self.speed
            if keys[pygame.K_UP]:    self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:  self.rect.y += self.speed

        # 화면 밖 제한
        self.rect.clamp_ip(screen.get_rect())


# ----------------------------
#        Random Enemy
# ----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect = self.image.get_rect(center=(x, y))

        # 랜덤 이동 속도
        self.vx = random.choice([-3, -2, 2, 3])
        self.vy = random.choice([-3, -2, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 벽 닿으면 튕김
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy *= -1


# ----------------------------
#           그룹 생성
# ----------------------------
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# 플레이어 여러 개 생성
player_positions = [
    (150, 200),
    (220, 200),
    (290, 200),
    (360, 200),
    (430, 200)
]

players = []
for pos in player_positions:
    p = Player(*pos)
    players.append(p)
    all_sprites.add(p)
    player_group.add(p)

# 첫 번째 플레이어만 조종
main_player = players[0]

# Enemy 1개 생성 (랜덤 이동)
enemy = Enemy(100, 100)
enemy_group.add(enemy)
all_sprites.add(enemy)

# Coin
coin_rect = pygame.Rect(430, 130, 40, 40)
score = 0

running = True
game_over = False


# ----------------------------
#          메인 루프
# ----------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        all_sprites.update()

        # 코인 충돌
        if main_player.rect.colliderect(coin_rect):
            score += 1
            coin_rect.x = 430 if score % 2 == 0 else 350

        # Enemy vs 모든 Player 충돌 검사
        if pygame.sprite.groupcollide(player_group, enemy_group, False, False):
            game_over = True

    # ---------------- 그리기 ----------------
    screen.fill((170, 200, 255))  # 하늘 배경
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))  # 땅

    # 코인
    pygame.draw.circle(
        screen, (0, 255, 0),
        (coin_rect.x + coin_rect.width//2, coin_rect.y + coin_rect.height//2),
        20
    )

    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    # 점수
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # 게임 오버
    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(
            over_text,
            ((WIDTH - over_text.get_width()) // 2,
             (HEIGHT - over_text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
