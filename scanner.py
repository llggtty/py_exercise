import numpy as np
n = 10
r = 2
np.linspace(r, n-r, num = n+1-2*r, dtype = int)
board = np.zeros((n,n),dtype=int)
def draw_circle(n,r):
    x0, y0 = np.random.choice(np.linspace(r, n - r, num = n+1-2*r, dtype = int), size = 2)
