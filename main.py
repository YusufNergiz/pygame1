import pygame
import random


pygame.init()


screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("First Pygame Game")

icon = pygame.image.load("spaceship32.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")


playerImage = pygame.image.load("spaceship64.png")
playerY = 480
playerX = 370
playerX_change = 0
playerY_change = 0

alienImage = pygame.image.load("space alien.png")
alienY = random.randint(50, 150)
alienX = random.randint(0, 736)

yusufImage = pygame.image.load("bneyusuf.jpeg")
scaled_yusuf = pygame.transform.scale(yusufImage, (75, 75))

bulletImage = pygame.image.load("bullet.png")
bulletY = 480
bulletX = 0
bullet_state = "ready"
bulletx_change = 0
bulletY_change = 10


main_font = pygame.font.SysFont("comicsans", 50)
lives = 0


def bullet_fired(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def alien(x, y):
    screen.blit(scaled_yusuf, (360, 100))


def player(x, y):
    screen.blit(playerImage, (x, y))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change += -3
            elif event.key == pygame.K_RIGHT:
                playerX_change += 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_fired(bulletX, bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    screen.fill(("#114e60"))
    screen.blit(background, (0, 0))


    lives_label = main_font.render(f"lives: {lives}", True, (255,255,255))
    screen.blit(lives_label, (10, 10))


    playerX += playerX_change
    player(playerX, playerY)
    alien(alienX, alienY)


    if bullet_state == "fire":
        bullet_fired(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY == 0:
            bullet_state = "ready"
            bulletY = 480




    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    pygame.display.update()