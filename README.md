### An python script that optimizes 2 variable functions and shows the resul using matplotlib
To change the function and the initial point change `f` and `starting_point` at `gradient_test.py`.
Note that the function must have an tuple as argument.
For example:
```python3
f = lambda x: x[0]**2 + x[1]**2
starting_point = (1,1)
```
will optimize f(x,y) = x²+y² using the Newton method starting at the point (1, 1, f(1)).
The optimizers should work for any n-dimensional function (check `computators.py`),
but the plotter will only work for 2-dimensional ones.
