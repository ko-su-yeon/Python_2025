#스페이스바로 총알 생성
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Shooting")

clock = pygame.time.Clock()

# 이미지 로드
player_img = pygame.image.load("dukbird.png")
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.image.load("poop.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.Surface((10, 5))
bullet_img.fill((255, 255, 0))  # 노란색 총알

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
        self.speed_x = random.choice([2, 3])
        self.speed_y = random.choice([2, 3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

# ---------------- Bullet ----------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()  # 화면 밖이면 제거

# ---------------- Groups ----------------
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 적 여러 개
for pos in [(100,100),(300,150),(500,200)]:
    e = Enemy(*pos)
    all_sprites.add(e)
    enemy_group.add(e)

score = 0
running = True
game_over = False

# ---------------- Main Loop ----------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # 총알 발사 (스페이스)
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet)
                bullet_group.add(bullet)

            # 게임오버 시 재시작
            if game_over and event.key == pygame.K_RETURN:
                game_over = False
                score = 0
                player.rect.center = (WIDTH//2, HEIGHT//2)
                for e in enemy_group:
                    e.rect.topleft = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

    if not game_over:
        all_sprites.update()

        # 총알 vs 적 충돌
        hits = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
        for hit in hits:
            score += 1
            # 새로운 적 생성
            new_enemy = Enemy(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
            all_sprites.add(new_enemy)
            enemy_group.add(new_enemy)

        # 플레이어 vs 적 충돌
        if pygame.sprite.spritecollide(player, enemy_group, False):
            game_over = True

    # ---------------- Drawing ----------------
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT-60, WIDTH, 60))  # 땅

    all_sprites.draw(screen)

    # 점수
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(text, (10,10))

    if game_over:
        over_text = font.render("GAME OVER (Press Enter)", True, (255,0,0))
        screen.blit(over_text, ((WIDTH-over_text.get_width())//2, (HEIGHT-over_text.get_height())//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
