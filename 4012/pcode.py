import sys
sys.stdin = open('sample_input.txt')


import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    food_mat = []
    for _ in range(N):
        food_mat.append([int(i) for i in input().split()])


    comb1 = itertools.combinations(range(N), N//2)
    # selecting (1,2) == selecting (0,3)
    unique_comb = []
    min_diff = 10000
    for c1 in comb1:
        # c1: (1,2,3,4,5)

        # remove complement case
        complement = [n for n in range(N) if n not in c1]
        if complement in unique_comb:
            continue
        unique_comb.append(list(c1))

        # sum synergy
        comb2 = itertools.combinations(c1, 2)
        recipe1 = 0
        for c2 in comb2:
            recipe1 += food_mat[c2[0]][c2[1]] + food_mat[c2[1]][c2[0]]

        comb2 = itertools.combinations(complement, 2)
        recipe2 = 0
        for c2 in comb2:
            recipe2 += food_mat[c2[0]][c2[1]] + food_mat[c2[1]][c2[0]]
        
        diff = abs(recipe1 - recipe2)
        if diff < min_diff:
            min_diff = diff

    print ('#{} {}'.format(test_case, min_diff))
