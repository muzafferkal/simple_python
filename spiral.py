import numpy as np
N=3
arr = [ [0]*N for _ in range(N)]
r = 1
c = 1
# direction stores 0=right, 1=down, 2=left, 3=up
dir = 0

def inc():
    global r, c, dir
    match dir:
        case 0:
            if c < N and arr[r-1][c] == 0:
                c = c + 1  
            else: 
                r = r + 1
                dir = (dir + 1) % 4
        case 1:
            if r < N and arr[r][c-1] == 0:
                r = r + 1  
            else: 
                c = c - 1
                dir = (dir + 1) % 4
        case 2:
            if c > 1 and arr[r-1][c-2] == 0:
                c = c - 1  
            else: 
                r = r - 1
                dir = (dir + 1) % 4
        case 3:
            if r > 1 and arr[r-2][c-1] == 0:
                r = r - 1  
            else: 
                c = c + 1  
                dir = (dir + 1) % 4
#print(arr)

for r in range(N):
    for c in range(N):
        arr[r][c] = r*N+c

for r in range(N):
    for c in range(N):
        arr[r][c] = 0

print(np.matrix(arr))
r = 1
c = 1

for x in range(1, N*N+1):
    print(f"r:c {r}:{c} x: {x} dir: {dir}")
    arr[r-1][c-1] = x
    #print(arr)
    inc()

print(np.matrix(arr))