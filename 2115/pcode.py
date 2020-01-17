import sys
sys.stdin = open("sample_input.txt", "r")

import itertools

def get_profit_from_block(mblock, M):
    max_profit = 0
    for m in range(1, M+1):
        selected = itertools.combinations(mblock, m)
        for sel in selected:
            if sum(sel) > C:
                continue
            profit = sum([i**2 for i in sel])
            if profit > max_profit:
                max_profit = profit
    return max_profit
            

T = int(input())
for test_case in range(1, T+1):

    # get data
    N, M, C = map(int, input().split())
    honey_map = []
    for _ in range(N):
        honey_map.append([int(i) for i in input().split()])

    max_profit = 0
    # strategy: split case with differnt row / same row
    # 1. different row
    line_max_profits = [0 for _ in range(N)]
    for n, line in enumerate(honey_map):
        
        # get line max profit
        for start_point in range(N-M+1):
            mblock = [line[i] for i in range(start_point, start_point+M)]
            p = get_profit_from_block(mblock, M)
            if p > line_max_profits[n]:
                line_max_profits[n] = p
    
    profit = sum(sorted(line_max_profits)[-2:])

    # 2. same row
    line_max_profit = 0
    for n, line in enumerate(honey_map):
        line_paded = [0]*(M-1) + line + [0]*(M-1)
        start_points = itertools.combinations(range(len(line_paded)-M+1), 2)
        for sp in start_points:
            # sp: (0,1) or (0,4) .. 
            if sp[1] - sp[0] < M:
                continue

            mblock0 = [line_paded[i] for i in range(sp[0], sp[0]+M)]
            mblock1 = [line_paded[i] for i in range(sp[1], sp[1]+M)]
            profit0 = get_profit_from_block(mblock0, M)
            profit1 = get_profit_from_block(mblock1, M)
            p = profit0 + profit1
            if p > line_max_profit:
                line_max_profit = p
#        start_points = itertools.combinations(range(len(line) - M + 1), 2)
#        for sp in start_points:
#            if sp[1] - sp[0] < M:
#                continue
#            mblock0 = [line[i] for i in range(sp[0], sp[0]+M)]
#            mblock1 = [line[i] for i in range(sp[1], sp[1]+M)]
#            profit0 = get_profit_from_block(mblock0, M)
#            profit1 = get_profit_from_block(mblock1, M)
#            p = profit0 + profit1
#            if p > line_max_profit:
#                line_max_profit = p
#

    p = max(profit, line_max_profit)
    print ('#{} {}'.format(test_case, p))
