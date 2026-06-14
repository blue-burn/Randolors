#!/usr/bin/env python3
import pygame 
import random
pg=pygame 
pg.init()
screen=pg.display.set_mode((400, 300))
pg.display.set_caption("click or press space for random colors")
r,g,b=0,0,0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            pg.display.set_caption(f"RGB: ({r}, {g}, {b})")
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pg.display.set_caption(f"RGB: ({r}, {g}, {b})")

    screen.fill((r, g, b))
    pg.display.flip()

pg.quit()
