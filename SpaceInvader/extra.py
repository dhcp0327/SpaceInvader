import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("CS361 Space Invaders")
icons = pygame.image.load('alien.png')
pygame.display.set_icon(icons)

SpaceShip = pygame.image.load('space-invaders.png')
SpaceShip = pygame.transform.scale(SpaceShip, (64, 64))

shipX = 370
shipY = 480
shipX_move = 0

point_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_point(x, y):
    point = font.render("Score : " + str(point_val), True, (255, 255, 255))
    screen.blit(point, (x, y))

def ship(x, y):
    screen.blit(SpaceShip, (x, y))


programrun = True
while programrun:
    screen.fill((85, 56, 56))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programrun = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipX_move = -0.5
            if event.key == pygame.K_RIGHT:
                shipX_move = 0.5
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipX_move = 0

    shipX += shipX_move
    if shipX <= 0:
        shipX = 0
    if shipX >= 736:
        shipX = 736

    ship(shipX, shipY)
    show_point(10, 10)
    pygame.display.update()
