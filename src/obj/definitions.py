import numpy as np

# Images' names
PENDULUM_IMAGE = "pendulum.png"

# Window properties
'''Use an almost 16/9 aspect ratio, with some pixels at the top for info'''
INFO_BAR_HEIGHT = 60
WINDOW_WIDTH = int(1920*0.7)  # px
WINDOW_HEIGHT = int(WINDOW_WIDTH*9/16 + INFO_BAR_HEIGHT)  # px

# Test area properties
'''These parameters are related with the WINDOW_WIDTH and WINDOW_HEIGHT values.
They will be used to define de scale matrix S'''
TEST_BED_WIDTH = 3.0  # m
TEST_BED_HEIGHT = TEST_BED_WIDTH*9/16  # m

# Scale matrix
X_SCALE = WINDOW_WIDTH/TEST_BED_WIDTH
Y_SCALE = (WINDOW_HEIGHT - INFO_BAR_HEIGHT)/TEST_BED_HEIGHT
S = np.array([[X_SCALE, 0.0, 0.0],
              [0.0, Y_SCALE, 0.0]])

# General homogeneous matrix
w_H_tb = np.array([[1.0, 0.0, TEST_BED_WIDTH/2.0],
                   [0.0, 1.0, TEST_BED_HEIGHT/2.0],
                   [0.0, 0.0, 1.0]])

# Physic constants
g = 9.81  # ms^⁻2
