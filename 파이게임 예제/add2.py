#Enemy 객체 여러개 생성 (위아래 이동)

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Collision (Multi Enemy)")

clock = pygame.time.Clock()

# ----------------------------
#             Player
# ----------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed

        # 화면 밖으로 못 나가게
        self.rect.clamp_ip(screen.get_rect())


# ----------------------------
#           Enemy (여러 개)
# ----------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, left_limit, right_limit):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect = self.image.get_rect(topleft=(x, y))

        # 위아래 이동 속도
        self.speed_y = 2

        # 이동 제한 범위
        self.min_y = y
        self.max_y = y + 100   # y + 100만큼 아래까지 움직임

    def update(self):
        # y축으로 이동 (위아래)
        self.rect.y += self.speed_y

        # 범위에서 튕기기
        if self.rect.top < self.min_y or self.rect.bottom > self.max_y:
            self.speed_y *= -1



# ----------------------------
#            그룹 생성
# ----------------------------
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 🔥 적 여러 개 생성 (땅 위에 일정 간격으로 배치)
enemy_positions = [
    (50, 260, 50, 200),
    (220, 260, 220, 350),
    (380, 260, 380, 540)
]

for x, y, left, right in enemy_positions:
    enemy = Enemy(x, y, left, right)
    all_sprites.add(enemy)
    enemy_group.add(enemy)

# ----------------------------
#        코인(초록 원)
# ----------------------------
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

        # 1) 플레이어 vs 코인 충돌
        if player.rect.colliderect(coin_rect):
            score += 1
            # 코인 위치 토글
            coin_rect.x = 430 if score % 2 == 0 else 350

        # 2) 플레이어 vs 적(여러 개)
        if pygame.sprite.spritecollide(player, enemy_group, False):
            print("적과 충돌! 게임 오버")
            game_over = True

    # ---------------- 그림 그리기 ----------------
    screen.fill((170, 200, 255))  # 하늘색 배경

    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))  # 땅

    pygame.draw.circle(
        screen, (0, 255, 0),
        (coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2),
        20
    )

    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    # 점수 표시
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # 게임 오버 표시
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
