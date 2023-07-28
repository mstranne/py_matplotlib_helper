import math

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

"""
    plot an coordinate system to visualize Pose (R|t)
    
    ax      : matplotlib axes to plot on
    R       : Rotation as roation matrix
    t       : translation as np.array (1, 3)
    scale   : Scale as np.array (1, 3)
    l_width : linewidth of axis
    text    : Text written at origin
"""
def plotPose(ax, R, t, scale = np.array((1,1,1)), l_width=2, text = None) :
    x_axis = np.array(([0, 0, 0], [1, 0, 0])) * scale
    y_axis = np.array(([0, 0, 0], [0, 1, 0])) * scale
    z_axis = np.array(([0, 0, 0], [0, 0, 1])) * scale

    x_axis += t
    y_axis += t
    z_axis += t

    x_axis = x_axis @ R
    y_axis = y_axis @ R
    z_axis = z_axis @ R

    ax.plot3D(x_axis[:, 0], x_axis[:, 1], x_axis[:, 2], color='red', linewidth=l_width)
    ax.plot3D(y_axis[:, 0], y_axis[:, 1], y_axis[:, 2], color='green', linewidth=l_width)
    ax.plot3D(z_axis[:, 0], z_axis[:, 1], z_axis[:, 2], color='blue', linewidth=l_width)

    if(text is not None):
        ax.text(x_axis[0, 0], x_axis[0, 1], x_axis[0, 2], "red")

    return None

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim3d([-2, 2])
ax.set_ylim3d([-2, 2])
ax.set_zlim3d([-2, 2])

R = np.eye(3)
t = np.zeros((1,3))
scale = np.array(([0.5, 0.5, 0.5]))

plotPose(ax, R, t, scale)

t = np.array(([1,1,1]))
plotPose(ax, R, t, scale)

R_rad = np.array((45.0,0.0,45.0)) * math.pi / 180
R = cv.Rodrigues(R_rad)[0]
t = np.array(([1,0.5,0]))
plotPose(ax, R, t, scale, l_width=3, text="pose 3")

plt.show()