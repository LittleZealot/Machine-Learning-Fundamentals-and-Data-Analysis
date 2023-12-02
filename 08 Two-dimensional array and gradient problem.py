import numpy as np
import matplotlib.pyplot as plt

# Problem 1: Linear function
def linear_func(x):
    y = 1/2*x + 1
    return y

# Generate x values and compute y values
x = np.arange(-50, 50.1, 0.1)
y = linear_func(x)

# Print and plot the linear function
print('Problem 1: Y values for the linear function:', y)
plt.plot(y)
plt.title('Problem 1: Linear function')
plt.show()

# Problem 2: Array combination
xy = np.concatenate([np.expand_dims(x, axis=1),
                     np.expand_dims(y, axis=1)], axis=1)
print('Problem 2: Concatenated array (x, y):', xy)

# Problem 3: Find the gradient
def get_gradient(xy):
    delta_x = np.diff(xy[:, 0])
    delta_y = np.diff(xy[:, 1])
    grad = delta_y / delta_x
    return grad

grad = get_gradient(xy)
print('Problem 3: Gradient values:', grad)

# Problem 4: Draw a graph for the gradient
plt.plot(x[1:], grad)
plt.xlabel('x')
plt.ylabel('Gradient')
plt.title('Problem 4: Graph of the Gradient')
plt.show()

# Problem 5: Python functionalization
def function1(x, name=None):
    print(x)
    if name == 'sq':
        y = x**2
    elif name == 'pow':
        y = 2*(x**2) + 2**x
    elif name == 'sin':
        y = np.sin(np.sqrt(x))
    return y

def compute_gradient(function, x_range=(-50, 50.1, 0.1), name='sq'):
    x = np.arange(x_range[0], x_range[1], x_range[2])
    y = function(x, name=name)
    array_xy = np.concatenate([np.expand_dims(x, axis=1),
                         np.expand_dims(y, axis=1)], axis=1)
    gradient = get_gradient(array_xy)
    return array_xy, gradient

# Example usages and plotting
print('Problem 5: Square function:', function1(x, name='sq'))
print('Problem 5: Power function:', function1(x, name='pow'))
print('Problem 5: Sin function:', function1(x, name='sin'))

array_xy_sq, gradient_sq = compute_gradient(function1, name='sq')
array_xy_pow, gradient_pow = compute_gradient(function1, name='pow')
array_xy_sin, gradient_sin = compute_gradient(function1, name='sin')

plt.plot(array_xy_sq[1:, 0], gradient_sq, label='Gradient of y = x^2')
plt.plot(array_xy_pow[1:, 0], gradient_pow, label='Gradient of y = 2x^2 + 2^x')
plt.plot(array_xy_sin[1:, 0], gradient_sin, label='Gradient of y = sin(sqrt(x))')

plt.xlabel('x')
plt.ylabel('Gradient')
plt.title('Problem 5: Gradients of Different Functions')
plt.legend()
plt.grid(True)
plt.show()

# Problem 6: Find the minimum value and its index
print('Problem 6: Minimum value and its index for the Square function:', np.min(function1(x, name='sq')), np.argmin(function1(x, name='sq')))
print('Problem 6: Minimum value and its index for the Power function:', np.min(function1(x, name='pow')), np.argmin(function1(x, name='pow')))
print('Problem 6: Minimum value and its index for the Sin function:', np.min(function1(x, name='sin')), np.argmin(function1(x, name='sin')))
