import sys
sys.stdin = open('sample_input.txt')


import itertools

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append([int(i) for i in input().split()])

    possible_xys = [(x,y) for x in range(N) for y in range(N)]
    combs = itertools.combinations(possible_xys, 2)
    max_len = 0
    for comb in combs:
        # comb ((x1,y1), (x2,y2))
        x1, y1 = comb[0]
        x2, y2 = comb[1]
        
        # case 1: if direct distance % 2 =! 1 then not included
        dist = (x2 - x1) + (y2 - y1)
        if dist % 2 == 1:
            continue

        # case 2: if slope==1 or -1 then not included
        slope = (x2-x1) / (float(y2-y1)+1e-10)
        if slope == 1 or slope == -1:
            continue 

        # calculate coordinates of p3, p4 and if out of box, then continue
        x3 = (x1 + x2 - y1 + y2) // 2
        y3 = (x2 - x1 + y1 + y2) // 2
        
        x4 = (x1 + x2 + y1 - y2) // 2
        y4 = (x1 - x2 + y1 + y2) // 2
        
        def inbox(x):
            if x < 0 or x >= N:
                return False
            else:
                return True
        cond1 = inbox(x3) and inbox(y3) and inbox(x4) and inbox(y4)
        if not cond1:
            continue
        cond2 = (x3, y3) in comb or (x4, y4) in comb
        if cond2:
            continue
        
        # calculate full path
        path = []; contents = []
        # p1 -> p3 -> p2 -> p4 -> p1           
        def go(x1, y1, x2, y2):
            direction1 = 1 if x1 < x2 else -1
            direction2 = 1 if y1 < y2 else -1    
            for n in range(1, N):
                _x = x1 + n * direction1
                _y = y1 + n * direction2
                content = maps[_x][_y]
                
                if content not in contents:
                    contents.append(content)
                    path.append((_x, _y))
                else:
                    return False
                
                if _x==x2:
                    return True

        if not go(x1,y1,x3,y3):
            continue
        if not go(x3,y3,x2,y2):
            continue
        if not go(x2,y2,x4,y4):
            continue
        if not go(x4,y4,x1,y1):
            continue
        
        if len(path) > max_len:
            max_len = len(path)

    if max_len == 0:
        max_len = -1
    print ('#{} {}'.format(test_case, max_len))
    

