import sys
sys.stdin = open('sample_input.txt')


def get_points(mags):
    p = 0
    for i in range(4):
        if mags[i][0] > 0:
            p += 2**i
    return p

def rotate(row, n):
    return row[-n:] + row[:-n]

def step(mags, move_info):
    k, direction = move_info
    k = k - 1

    # get directions of mags
    move_dirs = [0 for _ in range(4)]
    move_dirs[k] = direction
    for i in range(k-1, -1, -1):
        connected = mags[i+1][6] != mags[i][2]
        if connected:
            move_dirs[i] = direction if (k - i) % 2 == 0 else -1 * direction
        else:
            break
    for i in range(k+1, 4):
        connected = mags[i-1][2] != mags[i][6]
        if connected:
            move_dirs[i] = direction if (k - i) % 2 == 0 else -1 * direction
        else:
            break
    
    new_mags = []
    for i in range(4):
        new_mags.append(rotate(mags[i], move_dirs[i]))
    
    return new_mags

T = int(input())
for test_case in range(1, T+1):
    
    K = int(input())
    mags = []
    for _ in range(4):
        mags.append([int(i) for i in input().split()])
    
    move_infos = []
    for _ in range(K):
        move_infos.append([int(i) for i in input().split()])

    for move_info in move_infos:
        mags = step(mags, move_info)
    
    points = get_points(mags)
    print ('#{} {}'.format(test_case, points))
