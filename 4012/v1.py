import sys
sys.stdin = open('sample_input.txt')

import time
import itertools


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    food_mat = []
    for _ in range(N):
        food_mat.append([int(i) for i in input().split()])

    comb1 = itertools.combinations(range(N), N//2)
    comb1 = list(comb1)
    # selecting (1,2) == selecting (0,3)
    unique_comb = []
    min_diff = 10000
    t_comp = 0
    t_rest = 0
    t_all = 0
    ta0 = time.time()
    
    for i in range(N):
        for j in range(N):
            _k = food_mat[j][i]
            food_mat[i][j] += _k

    for c1 in comb1:
        # c1: (1,2,3,4,5)
        t0 = time.time()
        # remove complement case
        complement = [n for n in range(N) if n not in c1]
#        comb1.remove(complement)

        t1 = time.time()
        t_comp += t1-t0

        # sum synergy
        comb2 = itertools.combinations(c1, 2)
        recipe1 = 0
        for c2 in comb2:
            recipe1 += food_mat[c2[0]][c2[1]] 

        comb2 = itertools.combinations(complement, 2)
        recipe2 = 0
        for c2 in comb2:
            recipe2 += food_mat[c2[0]][c2[1]] 
        
        diff = abs(recipe1 - recipe2)
        if diff < min_diff:
            min_diff = diff

        t2 = time.time()
        t_rest += t2-t1
    t_all = time.time() - ta0
    
    print (t_comp, t_rest, t_all)
    print ('#{} {}'.format(test_case, min_diff))
