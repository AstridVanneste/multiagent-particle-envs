import pygame as pg
import sys

class Renderer:
    def __init__(self, resx, resy):
        self.screen = pg.display.set_mode((resx, resy))
        self.screen.fill([255, 255, 255])
        self.resx = resx
        self.resy = resy

        self.clock = pg.time.Clock()

    def render(self, entities):
        print("RENDER")
        self.screen.fill([255, 255, 255])
        for entity in entities:
            state = entity.state

            scaled_pos = [state.p_pos[0] * 700, state.p_pos[1] * 700]

            pos = [int(round(scaled_pos[0])), int(round(scaled_pos[1]))]

            print(pos)

            size = int(round(entity.size * 500))

            color = entity.color * 255

            for i in range(len(color)):
                color[i] = int(round(color[i]))

            assert(type(size) is int)
            assert(type(pos[0]) is int)
            assert (type(pos[1]) is int)

            pg.draw.circle(self.screen, (color[0], color[1], color[2]), pos, size)

        pg.display.update()
        self.clock.tick(5)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
