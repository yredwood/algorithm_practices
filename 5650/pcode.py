import sys
sys.stdin = open('sample_input.txt')

def move(xy, d):
    x, y = xy
    if d=='u':
        x = x - 1
    elif d=='d':
        x = x + 1
    elif d=='l':
        y = y - 1
    elif d=='r':
        y = y + 1
    return x,y



def get_score(xy, d, start_points, maps):
    # it must at least set start_points[xy][d]
    nx, ny = xy
    nd = d
    black_hole = False
    score = 0
    sp_stacks = {(nx, ny): (d, score)}
    while True:
        nx, ny = move((nx,ny), nd)
        # 1. return start ending
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        if maps[nx][ny] == 5:
            break
        if maps[nx][ny] == 1 and (nd == 'r' or nd == 'u'):
            break
        if maps[nx][ny] == 2 and (nd == 'r' or nd == 'd'):
            break
        if maps[nx][ny] == 3 and (nd == 'd' or nd == 'l'):
            break 
        if maps[nx][ny] == 4 and (nd == 'l' or nd == 'u'):
            break

        # 2. black hole ending
        if maps[nx][ny] == -1 or (nx,ny)==xy:
            black_hole = True
            break
        
        # 3. if meets diagonal
        if maps[nx][ny] == 1:
            if nd == 'd':
                nd = 'r'
            else:
                assert nd == 'l'
                nd = 'u'
            score += 1
            continue
        if maps[nx][ny] == 2:
            if nd == 'l':
                nd = 'd'
            else:
                assert nd == 'u'
                nd = 'r'
            score += 1
            continue
        if maps[nx][ny] == 3:
            if nd == 'r':
                nd = 'd'
            else:
                assert nd == 'u'
                nd = 'l'
            score += 1
            continue
        if maps[nx][ny] == 4:
            if nd == 'd':
                nd = 'l'
            else:
                assert nd == 'r'
                nd = 'u'
            score += 1
            continue

        # 4. worm hole
        if maps[nx][ny] > 5 and maps[nx][ny] <= 10:
            idx = worm_holes[maps[nx][ny]][0] != (nx,ny)
            nx, ny = worm_holes[maps[nx][ny]][int(idx)]
            continue

        # 5. else
        sp_stacks[(nx,ny)] = (d, score)

    # set start_points scores
    if black_hole:
        for _xy, _ds in sp_stacks.items():
            start_points[_xy][_ds[0]] = score - _ds[1]
    else:
        for _xy, _ds in sp_stacks.items():
            start_points[_xy][_ds[0]] = (score - _ds[1]) * 2 + 1
    return start_points
#    if black_hole:
#        start_points[xy][d] = score 
#    else:
#        start_points[xy][d] = score * 2 + 1



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = []
    for n in range(N):
        maps.append(
            [int(i) for i in input().split()]
        )
        
    directions = ['u', 'd', 'l', 'r']
    start_points = {}
    worm_holes = {}
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0:
                start_points[(i,j)] = {'u': -2, 'd': -2, 'l': -2, 'r': -2}
            if maps[i][j] > 5 and maps[i][j] <= 10:
                try:
                    worm_holes[maps[i][j]].append((i,j))
                except:
                    worm_holes[maps[i][j]] = [(i,j)]
    
    # for every start_point, get score
    for xy, score in start_points.items():
        for d in directions:
            if score[d] == -2:
                start_points = get_score(xy, d, start_points, maps)

        
    max_score = -2
    for xy, score in start_points.items():
        for d in directions:
            s = score[d]
            if s > max_score:
                max_score = s

    print ('#{} {}'.format(test_case, max_score))
