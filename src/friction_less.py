import pyglet
import math
from obj import pendulum, definitions as defs

# Setup a window
main_window = pyglet.window.Window(defs.WINDOW_WIDTH, defs.WINDOW_HEIGHT)
main_batch = pyglet.graphics.Batch()

pen = pendulum.Pendulum(x=defs.WINDOW_WIDTH/2, y=defs.WINDOW_HEIGHT/2, phi=0.7854, length=20.0, batch=main_batch)

angle_label = pyglet.text.Label(text="", x=10, y=defs.WINDOW_HEIGHT-20, batch=main_batch)

screen_objects = [pen]


@main_window.event
def on_draw():
    main_window.clear()
    main_batch.draw()


def update(dt):
    angle_label.text = "phi = %-6.3f" % math.degrees(pen.Y[0][0])
    for obj in screen_objects:
        obj.update(dt)


if __name__ == "__main__":
    # Update the game 120 times per second 1 / 120.0
    pyglet.clock.schedule_interval(update, 1/120.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
