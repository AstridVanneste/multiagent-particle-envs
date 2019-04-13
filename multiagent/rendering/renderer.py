import pygame as pg
import numpy as np
import math
import sys
import multiagent


class Renderer:
    def __init__(self, resx, resy):
        pg.init()
        pg.font.init()

        self.screen = None
        self.resx = resx
        self.resy = resy

        self.font = pg.font.SysFont('Arial', 24)

    def render(self, entities):
        if self.screen is None:
            self.screen = pg.display.set_mode((self.resx, self.resy))

        self.screen.fill([255, 255, 255])

        self.draw_entities(entities)
        self.draw_connections(entities)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def draw_entities(self, entities):
        for entity in entities:

            pos = self.get_pos(entity)

            size = int(round(entity.size * 350))

            color = []

            for i in range(len(entity.color)):
                color.append(int(round(entity.color[i] * 255)))

            if type(entity) == multiagent.core.Agent:
                pg.draw.circle(self.screen, color, pos, size)

            else:
                pg.draw.rect(self.screen, color, (pos[0] - size, pos[1] - size, 2 * size, 2 * size))

    def draw_connections(self, entities):
        agents, landmarks = self.filter_entities(entities)

        for agent in agents:
            for landmark in landmarks:
                if np.array_equal(agent.color, landmark.color):
                    agent_pos = self.get_pos(agent)
                    landmark_pos = self.get_pos(landmark)

                    pg.draw.line(self.screen, (128, 128, 128), agent_pos, landmark_pos, 2)

                    textsurface = self.font.render(str(self.calc_distance(agent_pos, landmark_pos)), False, (128, 128, 128))
                    self.screen.blit(textsurface, self.calc_middle(agent_pos, landmark_pos))

    def calc_distance(self, pos1, pos2):
        x = pos1[0] - pos2[0]
        y = pos1[1] - pos2[1]

        return int(math.sqrt((x ** 2) + (y ** 2)))

    def calc_middle(self, pos1, pos2):
        x = (pos1[0] + pos2[0])/2
        y = (pos1[1] + pos2[1])/2

        return (x, y)

    def filter_entities(self, entities):
        agents = [entities[i] for i in range(len(entities)) if type(entities[i]) == multiagent.core.Agent]
        landmarks = [entities[i] for i in range(len(entities)) if type(entities[i]) != multiagent.core.Agent]

        return agents, landmarks

    def get_pos(self, entity):
        state = entity.state

        scaled_pos = [(state.p_pos[0] + 1) * self.resx / 2, (state.p_pos[1] + 1) * self.resy / 2]

        pos = [int(round(scaled_pos[0])), int(round(scaled_pos[1]))]

        return pos


