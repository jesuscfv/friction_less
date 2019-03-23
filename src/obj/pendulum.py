import numpy as np
import math
from . import physicalobject, definitions as defs, resources, rungekutta


class Pendulum(physicalobject.PhysicalObject):

    def __init__(self, phi=0.7854, length=1.0, x_h=1.0, y_h=1.0, *args, **kwargs):
        image = resources.get_resource(defs.PENDULUM_IMAGE)
        super(Pendulum, self).__init__(img=image, *args, **kwargs)

        # Pendulum parameters
        self.length = length

        self.gl = float(defs.g)/1.0
        if length > 0.0:
            self.gl = float(defs.g)/float(length)

        # Initial 2-D homogeneous matrix
        self.a_H_p = np.array([[1.0, 0.0, 0.0],
                               [0.0, 1.0, 0.0],
                               [0.0, 0.0, 1.0]])

        # Initial 2-D homogeneous matrix for the rotation axis
        self.tb_H_a = np.array([[1.0, 0.0, float(x_h)],
                                [0.0, 1.0, float(y_h)],
                                [0.0, 0.0, 1.0]])

        # Initial screen coordinates

        self.s = np.array([[0.0], [0.0]])
        #self.x, self.y = int(self.s[0]), int(self.s[1])

        # Pendulum state
        self.Y = np.array([[float(phi)], [0.0]])

        self.update_a_H_p(phi)

        # Initial conditions for the Runge-Kutta solver
        self.rg = rungekutta.RungeKutta(y_0=self.Y)

    def update(self, dt):
        # Physics stuff (update position)
        super(Pendulum, self).update(dt)

        # Update pendulum state
        self.Y = self.rg.step(self.dynamics, dt)

        self.update_a_H_p(self.Y[0][0])
        '''self.s = defs.S.dot(self.tb_H_a.dot(self.a_H_p[:3, 2:]))
        self.x, self.y = int(self.s[0]), int(self.s[1])
        self.rotation = math.degrees(self.Y[0][0]) + 90'''

    def dynamics(self, Y):
        # The dynamics uses local coordinates
        return [[Y[1][0]], [-self.gl*np.sin(Y[0][0])]]

    def update_a_H_p(self, phi):

        c_phi = np.cos(phi)
        s_phi = np.sin(phi)

        self.a_H_p = np.array([[c_phi, -s_phi, -self.length * s_phi],
                               [s_phi, c_phi, -self.length*c_phi],
                               [0.0, 0.0, 1.0]])

        self.s = defs.S.dot(defs.w_H_tb.dot(self.tb_H_a.dot(self.a_H_p[:3, 2:])))

        # Update sprite position and orientation
        self.x, self.y = self.s[0], self.s[1]
        self.rotation = math.degrees(self.Y[0][0]) + 90
