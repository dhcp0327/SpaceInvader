from spaceinvader import spaceinvader

g = spaceinvader()

while g.run:
    g.title_page.show_menu()
    g.game_run()