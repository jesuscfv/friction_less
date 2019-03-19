import numpy as np


class RungeKutta:
    def __init__(self, y_0, h=0.01, t_i=0, t_f=1):
        # Initial value
        self.y_0 = np.array(y_0)
        self.y_n = np.array(y_0)
        # Step size
        self.h = h
        self.t_i = t_i
        self.t_f = t_f
        # Time sequence
        self.t = np.arange(t_i, t_f, h)
        # Results
        self.y = []

    def solve(self, f):
        for _ in self.t:
            k_1 = self.h * np.array(f(self.y_n))
            k_2 = self.h * np.array(f(self.y_n + k_1 / 2))
            k_3 = self.h * np.array(f(self.y_n + k_2 / 2))
            k_4 = self.h * np.array(f(self.y_n + k_3))
            y_n1 = self.y_n + (k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6)
            self.y.append(y_n1)
            self.y_n = y_n1.copy()
            # print(i,': ', self.y[-1], self.y_n)
        # Reset the y_n value to the initial one
        self.y_n = self.y_0
        return self.y

    def step(self, f, dt):
        k_1 = dt * np.array(f(self.y_n))
        k_2 = dt * np.array(f(self.y_n + k_1 / 2))
        k_3 = dt * np.array(f(self.y_n + k_2 / 2))
        k_4 = dt * np.array(f(self.y_n + k_3))
        y_n1 = self.y_n + (k_1 / 6 + k_2 / 3 + k_3 / 3 + k_4 / 6)
        self.y_n = y_n1

        return y_n1
