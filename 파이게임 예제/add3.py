import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Random Move Enemies")

clock = pygame.time.Clock()

# ==========================
# Player 클래스
# ==========================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())


# ==========================
# Enemy (랜덤 이동)
# ==========================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 적 형태는 단순 빨간 네모로 표시 (원하면 이미지로 변경 가능)
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 80, 80))
        self.rect = self.image.get_rect()

        # 랜덤 위치 생성
        self.rect.x = random.randint(0, WIDTH - 40)
        self.rect.y = random.randint(0, HEIGHT - 40)

        # 랜덤 속도 (-3~3)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 벽에 닿으면 튕기기
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1


# ==========================
# 스프라이트 그룹
# ==========================
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 적 여러 개 생성
for _ in range(7):  # 원하면 숫자 변경
    e = Enemy()
    all_sprites.add(e)
    enemy_group.add(e)

running = True

# ==========================
# 게임 루프
# ==========================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # 충돌 체크 → 플레이어가 적에 닿으면 종료
    if pygame.sprite.spritecollide(player, enemy_group, False):
        print("Game Over!")
        running = False

    # 배경
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
    pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))
    pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20)
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    # 스프라이트 그리기
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
