import pygame


class Menu():
    def __init__(self, spaceinvader):
        self.spaceinvader = spaceinvader
        self.mid_x, self.mid_y = self.spaceinvader.DISPLAY_X / 2, self.spaceinvader.DISPLAY_Y / 2
        self.run = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def print_cursor(self):
        self.spaceinvader.print_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.spaceinvader.window.blit(self.spaceinvader.display, (0, 0))
        pygame.display.update()
        self.spaceinvader.key_reset()


class TitlePage(Menu):
    def __init__(self, spaceinvader):
        Menu.__init__(self, spaceinvader)
        self.state = "Start"
        self.startx, self.starty = self.mid_x, self.mid_y + 30
        self.optionsx, self.optionsy = self.mid_x, self.mid_y + 50
        self.exitx, self.exity = self.mid_x, self.mid_y + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def show_menu(self):
        self.run = True
        while self.run:
            self.spaceinvader.event_ck()
            self.input_ck()
            self.spaceinvader.display.fill(self.spaceinvader.BLACK)
            self.spaceinvader.print_text('Main menu', 20, self.spaceinvader.DISPLAY_X / 2,
                                         self.spaceinvader.DISPLAY_Y / 2 - 20)
            self.spaceinvader.print_text('START!!', 20, self.startx, self.starty)
            self.spaceinvader.print_text('Option', 20, self.optionsx, self.optionsy)
            self.spaceinvader.print_text('EXIT', 20, self.exitx, self.exity)
            self.print_cursor()
            self.blit_screen()

    def cursor_move(self):
        if self.spaceinvader.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.spaceinvader.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def input_ck(self):
        self.cursor_move()
        if self.spaceinvader.START_KEY:
            if self.state == 'Start':
                self.spaceinvader.play = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Exit':
                pygame.quit()
            self.run = False
