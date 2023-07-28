# py_matplotlib_helper

## 3D_pose_plot
Helper function to plot pose as coordinate system with orientation. Something one often needs when debug plotting calculated poses.

find it in src/3D_pose_plot.py

**plotPose(ax, R, t, scale = np.array((1,1,1)), l_width=2, text = None)**
    plot an coordinate system to visualize Pose (R|t)
    
    ax      : matplotlib axes to plot on
    R       : Rotation as roation matrix
    t       : translation as np.array (1, 3)
    scale   : Scale as np.array (1, 3)
    l_width : linewidth of axis
    text    : Text written at origin

![](imgs/pose_plot.png)