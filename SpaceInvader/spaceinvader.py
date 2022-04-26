import pygame
from menu import TitlePage

SpaceShip = pygame.image.load('space-invaders.png')
SpaceShip = pygame.transform.scale(SpaceShip, (64, 64))

shipX = 370
shipY = 480
shipX_move = 0
point_val = 0


class spaceinvader():
    pygame.display.set_caption("CS361 Space Invaders")
    icons = pygame.image.load('alien.png')
    pygame.display.set_icon(icons)

    def __init__(self):
        pygame.init()
        self.run, self.play = True, False
        self.START_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE_KEY, self.EXIT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False, False, False, False
        self.DISPLAY_X, self.DISPLAY_Y = 800, 600
        self.display = pygame.Surface((self.DISPLAY_X, self.DISPLAY_Y))
        self.window = pygame.display.set_mode(((self.DISPLAY_X, self.DISPLAY_Y)))
        self.font_title = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.title_page = TitlePage(self)

    def show_point(self, x, y):
        font = pygame.font.Font(self.font_title, 32)
        point = font.render("Score : " + str(point_val), True, self.WHITE)
        self.window.blit(point, (x, y))

    def ship(self, x, y):
        self.window.blit(SpaceShip, (x, y))

    def game_run(self):
        while self.play:
            self.event_ck()
            if self.EXIT_KEY:
                self.play = False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0, 0))
            self.ship(shipX, shipY)
            self.show_point(10, 10)
            pygame.display.update()
            self.key_reset()

    def event_ck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run, self.play = False, False
                self.title_page.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.EXIT_KEY = True
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

    def key_reset(self):
        self.START_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SPACE_KEY, self.EXIT_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False, False, False, False, False

    def print_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_title, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
