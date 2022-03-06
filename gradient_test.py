import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from threading import Thread
import time
from computators import NewtonComputator
from optimization_plotter import plot_computator


f = lambda x: (x[0]+1)**4 + x[0]*x[1] + (x[1]+1)**4
starting_point = (0,1)

# Ploting parameters
step = 0.1 # distance for every point of the function
extra_space = 1 # epsilon between the first point and the last point

# Computation parameters
extra_time_between_iteration = 0.1 # 0.1 seconds

def print_function(f, computator):
    input()
    computator.stop_computation()
    its_points = computator.points
    final_point = computator.last_point
    f0 = final_point[0]
    f1 = final_point[1]
    s0 = starting_point[0]
    s1 = starting_point[1]
    
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
    out = f((X0, X1))

    points_x0 = list(map(lambda x: x[0], its_points))
    points_x1 = list(map(lambda x: x[1], its_points))
    out_points = list(map(f, its_points))
    fig = plt.figure()
    ax = Axes3D(fig)
    print(its_points) 

    ax.scatter3D(
        points_x0,
        points_x1,
        out_points,
        c='red', zorder=2, alpha=.5, s=10
    )
    ax.plot(
        points_x0,
        points_x1,
        out_points, zorder=2
    )
    ax.plot_surface(X0, X1, out, alpha=.3, zorder=3)
    ax.scatter3D(
        f0, f1, f(final_point), c='#00ff00', zorder=1, s=30, marker='x',
        label = f'({round(f0, 2)}, {round(f1, 2)},'
        + f' f({round(f0, 2)}, {round(f1, 2)}))'
        + f'\n= ({round(f0, 2)}, {round(f1, 2)}, {round(f(final_point), 2)})'
    )
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    newton_computator = NewtonComputator(f, starting_point)
    computation_thread = Thread(
        target=newton_computator.start_computation,
        args=(extra_time_between_iteration,)
    )
    computation_thread.start()
    print_function(f, newton_computator)


