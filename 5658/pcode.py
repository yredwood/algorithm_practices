import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for test_case in range(1,T+1):
    
    N, K = map(int, input().split())
    numbers = input()
    
    sums = []
    numbers += numbers
    for i in range(N):
        _num = numbers[i:i+N//4]
        dec = int((_num, 16)
        if dec not in sums:
            sums.append(dec)

    sorted_sums = [hex(i) for i in sorted(sums)[::-1]]
    print ('#{} {}'.format(test_case, sorted(sums)[::-1][K-1]))
