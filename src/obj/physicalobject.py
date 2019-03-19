import pyglet


class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        # Velocities
        self.v_x, self.v_y = 0.0, 0.0
        # Positions
        # self.x, self.y = 0.0, 0.0

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.v_x * dt
        self.y += self.v_y * dt
