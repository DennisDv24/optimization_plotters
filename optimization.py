from threading import Thread
import time
from computators import NewtonComputator
from optimization_plotter import plot_computator
from optimization_plotter import plot_computator

f = lambda x: (x[0]+1)**4 + x[0]*x[1] + (x[1]+1)**4
starting_point = (0,1)

# Ploting parameters
step = 0.1 # distance for every point of the function
extra_space = 1 # epsilon between the first point and the last point

# Computation parameters
extra_time_between_iteration = 0.1 # 0.1 seconds

if __name__ == '__main__':
    computator = NewtonComputator(f, starting_point)

    computation_thread = Thread(
        target=computator.start_computation,
        args=(extra_time_between_iteration,)
    )
    computation_thread.start()
    

    print('Press Intro to stop iterating')
    input()
    computator.stop_computation()
    print('Computating last iteration...')
    time.sleep(extra_time_between_iteration)

    plot_computator(computator, extra_space, step)



