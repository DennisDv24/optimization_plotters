import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pylab import imshow, colorbar, cm

def plot_computator(
    computator,
    extra_space=10,
    step=0.1
):
    its_points = computator.points
    final_point = computator.last_point
    starting_point = computator.starting_point
    f0 = final_point[0]
    f1 = final_point[1]
    s0 = starting_point[0]
    s1 = starting_point[1]
    
    # TODO look how could I include all computator.points into the range that will be
    # used as input to computator.f to plot it
    x0 = np.arange(
        min(s0, f0) - extra_space,
        max(s0, f0) + extra_space,
        step
    )
    x1 = np.arange(
        min(s1, f1) - extra_space,
        max(s1, f1) + extra_space,
        step
    )
    X0, X1 = np.meshgrid(x0, x1)
    f = computator.f
    out = f((X0, X1))

    points_x0 = list(map(lambda x: x[0], its_points))
    points_x1 = list(map(lambda x: x[1], its_points))
    out_points = list(map(f, its_points))
    print('Generating final plot')
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    # print(its_points) 

    ax.scatter3D(
        points_x0,
        points_x1,
        out_points,
        c='red', zorder=2, alpha=.75, s=10
    )
    ax.plot(
        points_x0,
        points_x1,
        out_points, zorder=2
    )
    ax.plot_surface(X0, X1, out, alpha=.5, zorder=3)
    ax.scatter3D(
        f0, f1, f(final_point), c='#00ff00', zorder=1, s=30, marker='x',
        label = f'({round(f0, 2)}, {round(f1, 2)},'
        + f' f({round(f0, 2)}, {round(f1, 2)}))'
        + f'\n= ({round(f0, 2)}, {round(f1, 2)}, {round(f(final_point), 2)})'
    )
    plt.legend(loc='upper left')
    plt.show()
    # TODO make also contour lines plot


