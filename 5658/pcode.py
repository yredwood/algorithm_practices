import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1,T+1):
    
    N, K = map(int, input().split())
    numbers = input()
    
    sums = []
    print (numbers*2)
    for i in range(N):
        _num = (numbers*2)[i:i+N//4]
        dec = int(_num, 16)
        if dec not in sums:
            sums.append(dec)
        print (_num)

    print ('#{} {}'.format(test_case, sorted(sums)[::-1][K-1]))
    exit()
