#사과 여러개 생성

# 1. 사과 여러 개 버전
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기 - 사과여러개")

clock = pygame.time.Clock()

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# ---------------- Player ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

# ---------------- Enemy ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = 3
        self.speed_y = 2

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1


# ---------------- Groups ----------------
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)
all_sprites.add(enemy)
enemy_group.add(enemy)

# ---------------- 사과 여러개 생성 ----------------
coins = []
coin_speeds = []

for _ in range(5):   # ← 사과 개수 조절
    rect = pygame.Rect(
        random.randint(0, WIDTH-40),
        random.randint(0, HEIGHT-40),
        40, 40
    )
    coins.append(rect)
    coin_speeds.append([random.choice([-2,2]), random.choice([-2,2])])

score = 0
running = True
game_over = False

# ---------------- Game Loop ----------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    if not game_over:
        all_sprites.update()

        # 사과 이동
        for i in range(len(coins)):
            coins[i].x += coin_speeds[i][0]
            coins[i].y += coin_speeds[i][1]

            if coins[i].left < 0 or coins[i].right > WIDTH:
                coin_speeds[i][0] *= -1
            if coins[i].top < 0 or coins[i].bottom > HEIGHT:
                coin_speeds[i][1] *= -1

            if player.rect.colliderect(coins[i]):
                score += 1
                coins[i].x = random.randint(0, WIDTH-40)
                coins[i].y = random.randint(0, HEIGHT-40)

    screen.fill((170,200,255))
    pygame.draw.rect(screen, (80,170,80), (0,HEIGHT-60,WIDTH,60))

    for rect in coins:
        screen.blit(apple_img, rect)

    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
