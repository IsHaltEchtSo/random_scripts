import matplotlib.pyplot as plt
from numpy import sin, cos, pi, outer, ones, size, linspace
from mpl_toolkits.mplot3d import axes3d

# Define x, y, z lists for sphere
x = 10 * outer(cos(linspace(0, 2 * pi)), sin(linspace(0, pi)))
y = 10 * outer(sin(linspace(0, 2 * pi)), sin(linspace(0, pi)))
z = 10 * outer(ones(size(linspace(0, 2 * pi))), cos(linspace(0, pi)))

# The amount of frames in the animation
frames = 26

# Generate each frame
for n in range(frames):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color=('b'))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlim(-8, 8)
    ax.set_xlim(-8, 8)
    ax.set_xlim(-8, 8)
    plt.savefig(str(n) + '.png')
    plt.close()

    # Add 1 to the x so the sphere moves right by 1
    x += 1
# Use pillow to save all frames as an animation in a gif file
from PIL import Image, ImageFilter

images = []
for n in range(frames):
    exec('a' + str(n) + '=Image.open("' + str(n) + '.png")')
    images.append(eval('a' + str(n)))
images[0].save('ball.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop=0)