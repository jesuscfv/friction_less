import pyglet


# Tell pyglet where to find the resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


def get_resource(image_name):
    object_image = pyglet.resource.image(image_name)
    center_image(object_image)
    return object_image
