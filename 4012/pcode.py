import sys
sys.stdin = open('sample_input.txt')


import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    food_mat = []
    for _ in range(N):
        food_mat.append([int(i) for i in input().split()])

    for i in range(N):
        for j in range(N):
            food_mat[i][j] += food_mat[j][i]


    comb1 = itertools.combinations(range(N), N//2)
    # selecting (1,2) == selecting (0,3)
    min_diff = 10000
    for c1 in comb1:
        # c1: (1,2,3,4,5)

        # remove complement case
        complement = [n for n in range(N) if n not in c1]

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

    print ('#{} {}'.format(test_case, min_diff))
