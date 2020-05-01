# created by Sijmen van der Willik
# 03/02/2018 18:08

import random


class TreasureMap(object):
    def __init__(self, width, height, length=10, max_step_size=10):
        self.width = width
        self.height = height
        self.no_instructions = length
        self.max_step_size = max_step_size
        self.starting_point = self.get_starting_point()
        self.map = str(self.starting_point)
        self.generate_list()

    def generate_list(self):
        for i in range(self.no_instructions):
            instruction = "\n" + \
                          random.choice(['x', 'y']) + \
                          random.choice(['-', '+']) + \
                          str(random.randint(1, self.max_step_size))

            self.map += instruction

    def get_starting_point(self):
        y = random.randint(0, self.height)
        x = random.randint(0, self.width)

        return [y, x]

    def write_treasure_map(self, path):
        with open(path, "w+") as f:
            f.write(self.map)


if __name__ == "__main__":

    for i in range(1000):
        TreasureMap(40, 30).write_treasure_map("treasure_maps/map" + str(i) + ".txt")
