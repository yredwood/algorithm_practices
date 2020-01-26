import sys
sys.stdin = open('sample_input.txt')


def check_if_constructable(row):
    # given one row, check if the slope can be constructed
    prev_height = row[0]
    builded = [0 for _ in range(N)]

    for n in range(N):
        if row[n] - prev_height == 1:
            k_flat = 0
            for k in range(n-1, n-X-1, -1):
                if k >= 0 and row[k] == row[n] - 1 and builded[k]==0:
                    k_flat += 1
                    builded[k] = 1
                else:
                    break
            if k_flat < X:
                return False

        elif row[n] - prev_height == -1:
            k_flat = 0
            for k in range(n, n+X):
                if k <= N-1 and row[k] == row[n] and builded[k]==0:
                    k_flat += 1
                    builded[k] = 1
                else:
                    break
            if k_flat < X:
                return False
        else:
            if abs(row[n] - prev_height) > 1:
                return False

        prev_height = row[n]
    return True


T = int(input())
for test_case in range(1, T+1):

    N, X = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append([int(i) for i in input().split()])

    maps_T = []
    for n in range(N):
        maps_T.append([maps[i][n] for i in range(N)])

    cnt = 0
    for row in maps:
        if check_if_constructable(row):
            cnt += 1
    for row in maps_T:
        if check_if_constructable(row):
            cnt += 1

    print ('#{} {}'.format(test_case, cnt))
