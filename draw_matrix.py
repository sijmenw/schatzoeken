# created by Sijmen van der Willik
# 03/02/2018 17:35

import imageio
import numpy as np
import island


class DrawMatrix(object):
    def __init__(self, matrix, color_scheme, res_per_cell=10):
        self.matrix = matrix
        self.color_scheme = color_scheme
        self.res = res_per_cell

    def create_png(self, output_path="matrix.png"):
        height, width = self.matrix.shape
        image = np.zeros([height, width, 3])

        for row_idx in range(height):
            for col_idx in range(width):
                color = self.color_scheme[self.matrix[row_idx][col_idx]]
                image[row_idx, col_idx] = color

        imageio.imwrite(output_path, image)


isle = island.Island(40, 30)

draw = DrawMatrix(isle.island, {island.Constants.WATER: island.Constants.WATER_COLOR,
                                island.Constants.SAND: island.Constants.SAND_COLOR, })

draw.create_png()
