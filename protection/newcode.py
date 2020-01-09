import sys
import itertools


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def count_pass_vertical(pT, k):
    cnt = 0
    for w in range(len(pT)):
        if ('0'*k in pT[w]) or ('1'*k in pT[w]):
            cnt += 1
    return cnt

def transpose(prt):
    pT = []
    for w in range(len(prt[0])):
        pT.append(''.join([p[w] for p in prt]))
    return pT

def get_priority_idx(p, k):
    
    index_cnt = count_pass_vertical(transpose(p), k)
    scores_a, scores_b = [], []
    for _d in range(len(p)):
        changed_p = p.copy()
        changed_p[_d] = '0'*len(p[0])
        score = count_pass_vertical(transpose(changed_p), k)
        scores_a.append(score)

        changed_p[_d] = '1'*len(p[0])
        score = count_pass_vertical(transpose(changed_p), k)
        scores_b.append(score)

    return scores_a, scores_b


def step(prt, n_step, scores_a, scores_b, k):
    
    D = len(prt)
    W = len(prt[0])
    
    # a-> change all to 0, b->change all to 1
    a_list = [i+1 for i in range(D)]
    b_list = [-i-1 for i in range(D)]
    tuples = itertools.combinations(a_list + b_list, n_step)
    
    # get sorted tuples
    scores = []; sorted_tuples = []
    for tup in tuples:
        s = 0
        for t in tup:
            if t > 0:
                s += scores_a[t-1]
            else:
                s += scores_b[-t-1]
        scores.append(s)
        sorted_tuples.append(tup)

    idx = argsort(scores)[::-1]
    sorted_tuples = [sorted_tuples[i] for i in idx]
    
    for tup in sorted_tuples:

        # remove tuples with same idx
        positive_tup = []
        flag = 0
        for t in tup:
            if t > 0:
                _t = t-1
            else:
                _t = -t-1
            if _t in positive_tup:
                flag = 1
            positive_tup.append(_t)
        if flag:
            continue

        new_p = prt.copy()
        for t in tup:
            if t > 0:
                assert len(new_p[t-1]) == W
                new_p[t-1] = '0'*W
            else:
                assert len(new_p[-t-1]) == W
                new_p[-t-1] = '1'*W
        score = count_pass_vertical(transpose(new_p), k)
        if score == len(prt[0]):
            return True
    return False
    

if __name__ == '__main__':

    sys.stdin = open('newsample.txt', 'r')
    T = int(input())
    for test_case in range(1, T+1):

        D, W, K = map(int, input().split(' '))
    
        # horizontal view
        prt = []
        for d in range(D):
            prt.append(input().replace(' ', ''))
        
        # vertical view
        prt_T = transpose(prt)

        # check if it is pass
        cnt = count_pass_vertical(prt_T, K)
        if cnt == W:
            print ('#{} {}'.format(test_case, 0))
            continue

        # get depth priority 
        scores_a, scores_b = get_priority_idx(prt, K)

        for _step in range(1, K):
            result = step(prt, _step, scores_a, scores_b, K)
            if result:
                break
        if not result:
            _step = K

        print ('#{} {}'.format(test_case, _step))

        




















    #
