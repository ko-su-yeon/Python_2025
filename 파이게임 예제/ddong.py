#똥 여러개 생성

# 2. 똥 여러 개 버전
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥 여러개 버전")

clock = pygame.time.Clock()

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = random.choice([-3,3])
        self.speed_y = random.choice([-2,2])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

# Groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 똥 7개 생성
for _ in range(7):
    e = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(e)
    enemy_group.add(e)

# 고정된 사과 1개
coin_rect = pygame.Rect(430,130,40,40)

score = 0
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False

    if not game_over:
        all_sprites.update()
        
        if player.rect.colliderect(coin_rect):
            score += 1
            coin_rect.x = random.randint(0, WIDTH-40)
            coin_rect.y = random.randint(0, HEIGHT-40)

        # 어느 똥이든 닿으면 끝
        if pygame.sprite.spritecollide(player, enemy_group, False):
            game_over = True

    screen.fill((170,200,255))
    pygame.draw.rect(screen, (80,170,80), (0,HEIGHT-60,WIDTH,60))
    screen.blit(apple_img, coin_rect)
    all_sprites.draw(screen)

    font = pygame.font.SysFont(None,24)
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(text,(10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
