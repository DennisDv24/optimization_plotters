import numdifftools as nd
import numpy as np
import time

class NewtonComputator:
    def __init__(self, f, starting_point):
        self.starting_point = starting_point
        self.last_point = starting_point
        self.points = [starting_point]
        self.f = f
        
        self.gradient = nd.Gradient(f)
        self.hessian = nd.Hessian(f)
    
    def start_computation(self, sleep_time=None):
        self.should_compute = True 
        self.compute(sleep_time)

    def stop_computation(self):
        self.should_compute = False
    
    def _get_newton_move(self, point):
        return np.matmul(
            np.linalg.inv(self.hessian(point)),-self.gradient(point)
        )

    def newton_iteration(self):
        p0 = self.last_point
        newton_move = self._get_newton_move(p0)
        p = (p0[0] + newton_move[0], p0[1] + newton_move[1])
        print(f'Current point: {p}, iteration: {self.i}')
        self.points.append(p) 
        self.last_point = p
        self.i += 1

    def compute(self, sleep_time = None):
        self.i = 0
        while self.should_compute:
            if sleep_time: time.sleep(sleep_time)
            self.newton_iteration()


class GradientDescentComputator:
    def __init__(self, f, starting_point, step=0.1):
        self.starting_point = starting_point
        self.last_point = starting_point
        self.points = [starting_point]
        self.f = f
        
        self.gradient = nd.Gradient(f)
        # TODO make an dynamic changing step
        self.step = step
    
    def start_computation(self, sleep_time=None):
        self.should_compute = True 
        self.compute(sleep_time)

    def stop_computation(self):
        self.should_compute = False
    
    def _get_gradient_move(self, point):
        return -self.gradient(point)

    def newton_iteration(self):
        p0 = self.last_point
        gradient_move = self._get_gradient_move(p0)
        p = (
            p0[0] + self.step * gradient_move[0],
            p0[1] + self.step * gradient_move[1]
        )
        print(f'Current point: {p}, iteration: {self.i}')
        self.points.append(p) 
        self.last_point = p
        self.i += 1

    def compute(self, sleep_time = None):
        self.i = 0
        while self.should_compute:
            if sleep_time: time.sleep(sleep_time)
            self.newton_iteration()
