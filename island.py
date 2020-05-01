# created by Sijmen van der Willik
# 02/02/2018 17:28

import numpy as np
import random
import simplejson


class Constants(object):
    EMPTY = -1
    WATER = 0
    SAND = 1
    ROCK = 2
    TREE = 3

    WATER_COLOR = [153, 204, 255]
    SAND_COLOR = [255, 255, 153]


class Island(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.island = np.array([[-1 for x in range(width)] for y in range(height)])

        self.build_island()

    def build_island(self):
        # coordinates are [Y, X], also the way they are accessed in self.island
        coordinates = [[[y, x] for x in range(self.width)] for y in range(self.height)]
        coordinates = np.array(coordinates)
        coordinates = np.concatenate(coordinates, axis=0)
        np.random.shuffle(coordinates)

        for coordinate in coordinates:
            self.fill_coordinate(coordinate)

    def fill_coordinate(self, coordinate):
        """This holds the actual logic for deciding the value on the map

        WATER: 100% with context size < 15

        :param coordinate:
        :return:
        """
        context = self.get_context(coordinate)

        x = context.shape[0] * context.shape[1]
        a = -0.08
        b = 2.20
        p = a * x + b

        if random.uniform(0, 1) < p:
            self.island[coordinate[0]][coordinate[1]] = Constants.WATER
        else:
            self.island[coordinate[0]][coordinate[1]] = Constants.SAND

    def get_context(self, coordinate, padding=2):
        x1 = max(coordinate[1]-padding, 0)
        x2 = min(coordinate[1]+padding+1, self.width)
        y1 = max(coordinate[0]-padding, 0)
        y2 = min(coordinate[0]+padding+1, self.height)

        return self.island[y1:y2, x1:x2]

    def print_island(self):
        for row in self.island:
            print(row)

    def load_island_from_file(self, path):
        pass

    def write_island_map(self, path):
        with open(path, "w+") as f:
            simplejson.dump(self.island.tolist(), f)


if __name__ == "__main__":
    Island(40, 30).write_island_map("island/island.txt")
