import numpy as np
import math
from . import definitions as defs


class References():
    def __init__(self, step):
        self.step = step
        self.grid_points = self.generate_grid_points(self.step)
        self.axes_points = self.generate_axes(self.step)

    def generate_grid_points(self, step):
        # Unit vectors
        e_1 = np.array([[step], [0.0], [0.0]])
        e_2 = np.array([[0.0], [step], [0.0]])
        p = np.array([[0.0], [0.0], [1.0]])
        # Calculate the number of division in each axis
        number_x_divs = math.floor(defs.TEST_BED_WIDTH / (2.0 * step))
        number_y_divs = math.floor(defs.TEST_BED_HEIGHT / (2.0 * step))

        points = []
        for x in range(-number_x_divs, number_x_divs + 1, 1):
            for y in range(-number_y_divs, number_y_divs + 1, 1):
                s = defs.S.dot(defs.w_H_tb.dot(x * e_1 + y * e_2 + p))
                if s[0] > 0.0:
                    points.append(int(s[0]))
                    points.append(int(s[1]))

        points_tuple = tuple(points)
        return points_tuple

    def generate_axes(self, step):
        e_1 = np.array([[step], [0.0], [0.0]])
        e_2 = np.array([[0.0], [step], [0.0]])
        p = np.array([[0.0], [0.0], [1.0]])

        s_x = defs.S.dot(defs.w_H_tb.dot(e_1 + p))
        s_y = defs.S.dot(defs.w_H_tb.dot(e_2 + p))
        o = defs.S.dot(defs.w_H_tb.dot(p))

        axes_tuple = (int(o[0]), int(o[1]), int(s_x[0]+1), int(s_x[1]+1),
                      int(o[0]), int(o[1]), int(s_y[0]+1), int(s_y[1]+1))
        return axes_tuple
