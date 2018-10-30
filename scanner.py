import numpy as np

def draw_circle(n,r,x0,y0):
    board = np.zeros((n, n), dtype=int)
    for i in range(0,n):
        for j in range(0,n):
            d = np.sqrt((i-x0)**2 + (j-y0)**2)
            if d<r:
                board[i][j] = 1
    return board

def draw_random(n, p = 0.4):
    board = np.zeros((n, n), dtype=int)
    for i in range(0,n):
        board[i] = np.random.choice([0,1],size=n, p = p)
    return board

def mass_center(board):
    n = board.shape[0]
    x,y,count = 0,0,0
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == 1:
                x = x+i
                y = y+j
                count = count + 1
    return [x/count, y/count, count]

def points_in_circle(x0,y0,r, board):
    count_in = 0
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == 1:
                if (i-x0)**2 +(j-y0)**2 < r**2:
                    count_in = count_in + 1
    return count_in

n = 20
r = 4
pi = 3.1415926
x0, y0 = np.random.randint(r, n-r, 2)

board = draw_circle(n,r,x0,y0)
board = draw_random(n)
print(board)
x_est, y_est, count = mass_center(board)
guess_r = np.sqrt(count/pi)
count_in = points_in_circle(x_est,y_est,guess_r, board)
if count_in > 0.9*count:
    print("it's likely to be a circle")
    print(draw_circle(n,guess_r,x_est,y_est))
else:
    print("doesn't look like a circle")
