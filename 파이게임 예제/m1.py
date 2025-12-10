#플레이어 한명 적 여러명 사과 여러개

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player 1, Multiple Enemies & Apples")

clock = pygame.time.Clock()

# 이미지 로드
player_img = pygame.image.load("dukbird.png")
player_img = pygame.transform.scale(player_img, (50, 50))
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))
enemy_img = pygame.image.load("poop.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 40))

# ---------------- Player ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

# ---------------- Enemy ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = random.choice([2,3])
        self.speed_y = random.choice([2,3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

# ---------------- Apple ----------------
class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = apple_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = random.choice([2,3])
        self.speed_y = random.choice([2,3])

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
apple_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 적 여러 개
for pos in [(50,50),(200,100),(400,150)]:
    e = Enemy(*pos)
    all_sprites.add(e)
    enemy_group.add(e)

# 사과 여러 개
for pos in [(100,300),(300,50),(500,200)]:
    a = Apple(*pos)
    all_sprites.add(a)
    apple_group.add(a)

score = 0
running = True
game_over = False

# ---------------- Main Loop ----------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_RETURN:
            # 재시작
            game_over = False
            score = 0
            player.rect.center = (WIDTH//2, HEIGHT//2)

    if not game_over:
        all_sprites.update()

        # 사과 충돌
        hits = pygame.sprite.spritecollide(player, apple_group, False)
        for apple in hits:
            score += 1
            # 랜덤 위치
            apple.rect.x = random.randint(0, WIDTH-apple.rect.width)
            apple.rect.y = random.randint(0, HEIGHT-apple.rect.height)
            # 랜덤 이동 방향
            apple.speed_x = random.choice([-3,-2,2,3])
            apple.speed_y = random.choice([-3,-2,2,3])

        # 적 충돌
        if pygame.sprite.spritecollide(player, enemy_group, False):
            game_over = True

    # ---------------- Drawing ----------------
    screen.fill((170, 200, 255))  # 배경
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT-60, WIDTH, 60))  # 땅

    all_sprites.draw(screen)

    # 점수
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(text, (10,10))

    # 게임오버
    if game_over:
        over_text = font.render("GAME OVER (Press Enter)", True, (255,0,0))
        screen.blit(over_text, ((WIDTH-over_text.get_width())//2, (HEIGHT-over_text.get_height())//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
