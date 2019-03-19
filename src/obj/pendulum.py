import numpy as np
import math
from . import physicalobject, definitions as defs, resources, rungekutta


class Pendulum(physicalobject.PhysicalObject):

    def __init__(self, phi=0.7854, length=1.0, *args, **kwargs):
        image = resources.get_resource(defs.PENDULUM_IMAGE)
        super(Pendulum, self).__init__(img=image, *args, **kwargs)

        # Pendulum state
        self.Y = np.array([[float(phi)], [0.0]])

        # Initial conditions for the Runge-Kutta solver
        self.rg = rungekutta.RungeKutta(y_0=self.Y)

        self.gl = float(defs.g)/1.0
        if length > 0.0:
            self.gl = float(defs.g)/float(length)

    def update(self, dt):
        # Physics stuff (update position)
        super(Pendulum, self).update(dt)

        # Update pendulum state
        self.Y = self.rg.step(self.dynamics, dt)
        self.rotation = math.degrees(self.Y[0][0])

    def dynamics(self, Y):
        return [[Y[1][0]], [-self.gl*np.sin(Y[0][0])]]
