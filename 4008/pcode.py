import sys
sys.stdin = open('sample_input.txt')

import itertools

def calc(nums, ops):
    def operation(op, num1, num2):
        if op==0:
            return num1+num2
        elif op==1:
            return num1-num2
        elif op==2:
            return num1*num2
        else:
            a = num1/num2
            return int(a)

    nums = nums.copy()
    for i, op in enumerate(ops):
        out = operation(op, nums[i], nums[i+1])
        nums[i+1] = out
    return out


T = int(input())
for test_case in range(1,T+1):
    
    N = int(input())
    _operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    assert len(numbers) == N

    # change operators to [2, 3, 0, 0] to [0, 0, 1, 1, 1]
    operators = []
    for i, ops in enumerate(_operators):
        operators += [i] * ops

    max_value = -1e10
    min_value = 1e10
    # operator comb 4
    combs = itertools.permutations(operators, N-1)
    uniq = {}
    for c in combs:
        try:
            _ = uniq[c]
        except:
            # (c[0], c[1], ...)
            output = calc(numbers, c)
            if output == 0.1:
                continue
            if output > max_value:
                max_value = output
            if output < min_value:
                min_value = output

        uniq[c] = 1

    print ('#{} {}'.format(test_case, max_value-min_value))
