from threading import Thread
import time
from computators import NewtonComputator, GradientDescentComputator
from optimization_plotter import plot_computator

f = lambda x: (x[0]+1)**4 + x[0]*x[1] + (x[1]+1)**4
starting_point = (2,3)

# Ploting parameters
distance_between_every_function_point = 0.1 
extra_space = 5 # epsilon between the first point and the last point

# Computation parameters
extra_time_between_iteration = 0.1 # 0.1 seconds
gradient_step = 0.01 # gradient descent step per iteration

def optimize_in_parallel(computator):
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


if __name__ == '__main__':
    print('OPTIMIZING WITH NEWTON METHOD')
    print('-----------------------------')
    computator = NewtonComputator(f, starting_point)
    optimize_in_parallel(computator)
    plot_computator(
        computator,
        extra_space,
        distance_between_every_function_point
    )

    print('\nOPTIMIZING WITH GRADIENT DESCENT METHOD')
    print(f'Step for every iteration: {gradient_step}')
    print('---------------------------------------')

    computator = GradientDescentComputator(
        f, starting_point, gradient_step
    )
    optimize_in_parallel(computator)
    plot_computator(
        computator,
        extra_space,
        distance_between_every_function_point
    )



