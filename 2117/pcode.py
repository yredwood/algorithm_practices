import sys
sys.stdin = open('sample_input.txt')


def get_max_house_from_xy(a, b, city_map):

    # get every point of distance from point (a, b)
    # dist_map[i] refers the list of the points with the same distance i
    dist_map = [[] for _ in range(N*2)]
    for i in range(N):
        for j in range(N):
            # relative point from (a,b)
            ri, rj = (i-a), (j-b)
            if ri * rj > 0:
                dist = abs((j+i) - (b+a))
            else:
                dist = abs((j-i) - (b-a))

            if city_map[i][j] == 1:
                dist_map[dist].append((i,j))
    
    # given prev_num_houses, get current profit
    max_house = 0
    prev_num_houses = 0
    for d in range(N*2):
        k = d + 1
        cost = k**2 + (k-1)**2
        
        prev_num_houses = len(dist_map[d]) + prev_num_houses
        revenue = prev_num_houses * M

        profit = revenue - cost
        
        if profit > 0 and prev_num_houses > max_house:
            max_house = prev_num_houses

    return max_house       



T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    city_map = []
    for _ in range(N):
        city_map.append([int(_i) for _i in input().split()])
    
    # strategy : from the point (x,y), make a function that 
    # maximizes the profit
    max_house = 0
    for x in range(N):
        for y in range(N):
            p = get_max_house_from_xy(x, y, city_map)
            if p > max_house:
                max_house = p
    
    print ('#{} {}'.format(test_case, max_house))
