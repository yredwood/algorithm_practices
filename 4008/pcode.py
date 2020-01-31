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
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    assert len(numbers) == N

    max_value = -1e10
    min_value = 1e10

    # (n-1) Comb (len(op0)) (n-1-len(op0)) Comb len(op1) ...
    c0 = itertools.combinations(range(N-1), operators[0])
    for _c0 in c0:
        leftset0 = set(range(N-1)) - set(_c0)
        c1 = itertools.combinations(leftset0, operators[1])
        for _c1 in c1:
            leftset1 = leftset0 - set(_c1)
            c2 = itertools.combinations(leftset1, operators[2])
            for _c2 in c2:
                leftset2 = leftset1 - set(_c2)
                # loop starts here

                # _c0: (0,3,5) -> op0 index
                # _c1: (1,2) -> op1 index
                # _c2: (8,9) -> op2 index
                # leftset2: (6,7) -> op3 index
                current_ops = [0 for _ in range(N-1)]
                for c in _c1:
                    current_ops[c] = 1
                for c in _c2:
                    current_ops[c] = 2
                for c in leftset2:
                    current_ops[c] = 3

                output = calc(numbers, current_ops)
                if output > max_value:
                    max_value = output
                if output < min_value:
                    min_value = output
    print ('#{} {}'.format(test_case, max_value-min_value))
