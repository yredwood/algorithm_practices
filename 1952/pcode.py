import sys
import itertools

sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    
    # get inputs
    day, month, month3, year = map(int, input().split())
    plans = [int(i) for i in input().split()]

    # strategy 
    #  0 month3 to maximum 4 month3, 
    #      if 0-> find optimal (year and day+month)
    #      else-> for all possible start points, calc total price

    start_points = [i for i in range(12)]
    for i3 in range(5):
        if i3==0:  # no month3 case
            yearly_cost = year
            monthly_cost = sum([min(month, day*plans[_i]) for _i in range(12)])
            # set initial min_cost
            min_cost = min(yearly_cost, monthly_cost) 

        elif i3==4:  # all month3 case
            cost = 4*month3
            if cost < min_cost:
                min_cost = cost

        else:
            comb = itertools.combinations(start_points, i3)
            for c in comb:
                # c: (1, 3, 7, ...), sorted tuple
                if len(c) > 1:
                    diffs = [c[_ci] - c[_ci-1] for _ci in range(1, len(c))]
                    if min(diffs) <= 2:
                        continue

                mon3_cover = list(c) + [_c+1 for _c in list(c)] + [_c+2 for _c in list(c)]
                other_months = [i for i in range(12) if i not in mon3_cover]
                cost = i3 * month3 + sum([min(month, day*plans[_i]) for _i in other_months])
                if cost < min_cost:
                    min_cost = cost
    
    print ('#{} {}'.format(test_case, min_cost))
