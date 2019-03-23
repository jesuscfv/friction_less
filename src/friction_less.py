import pyglet
import math
import numpy as np
from obj import pendulum, definitions as defs, references as refs

# Setup a window
main_window = pyglet.window.Window(defs.WINDOW_WIDTH, defs.WINDOW_HEIGHT)
main_batch = pyglet.graphics.Batch()

# Main object
pen = pendulum.Pendulum(phi=3.1416/4, x_h=0.0, y_h=defs.TEST_BED_HEIGHT/2, length=1.5, batch=main_batch)

# Example of info
angle_label = pyglet.text.Label(text="", x=10, y=defs.WINDOW_HEIGHT-20, batch=main_batch)

# Add to the main_batch the line that divides the test area from the info bar
info_line = main_batch.add(2, pyglet.gl.GL_LINES, None,
                           ('v2i', (0, defs.WINDOW_HEIGHT-defs.INFO_BAR_HEIGHT,
                                    defs.WINDOW_WIDTH, defs.WINDOW_HEIGHT-defs.INFO_BAR_HEIGHT)))

# Grid points each 10cm and reference axes
references = refs.References(0.1)
# Add the points to the main_batch
grid_points = main_batch.add(int(len(references.grid_points)/2), pyglet.gl.GL_POINTS, None,
                             ('v2i', references.grid_points))

# Objects to update
screen_objects = [pen]


@main_window.event
def on_draw():
    main_window.clear()
    main_batch.draw()


def update(dt):
    angle_label.text = "phi = %-6.3f \t x = %-6.3f \t y = %-6.3f" % (math.degrees(pen.Y[0][0]), pen.x, pen.y)
    for obj in screen_objects:
        obj.update(dt)


if __name__ == "__main__":

    # Update the game 120 times per second 1 / 120.0
    pyglet.clock.schedule_interval(update, 1/120.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
