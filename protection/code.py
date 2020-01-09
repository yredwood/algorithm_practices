import sys
import itertools


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def unique(seq):
    new_list = []
    for s in seq:
        if s not in new_list:
            new_list.append(s)
    return new_list

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

def sort_by_priority(input_tuples, score_a, score_b):
    scores = []
    for itup in input_tuples:
        s = 0
        for t in itup:
            if t>0:
                s+=score_a[t-1]
            else:
                s+=score_b[-t-1]
        scores.append(s)
    idx = argsort(scores)
    output_tuples = [input_tuples[i] for i in idx]
    return output_tuples


def get_complementary_set(input_list, D):
    input_abs = [abs(i) for i in input_list]
    output_list = []
    for i in range(-D,D):
        if (abs(i) not in input_abs) and (i!=0):
            output_list.append(i)
    return output_list


def step(prt, prev_result, k, score_a, score_b):

    D = len(prt)
    W = len(prt[0])

    tuples = prev_result['tuples']
    states = prev_result['states']
#    priority = prev_result['priority']

    if len(tuples)==0:
        exclude_list = [i for i in range(-D,D) if i!=0]
        output_result = {}
        output_result['tuples'] = [[e] for e in exclude_list] # exclude idx list
        output_result['states'] = [] # excluded cell state

        for e in exclude_list:
            new_prt = prt.copy()
            if e > 0:
                new_prt[e-1] = '0'*W
            else:
                new_prt[-e-1] = '1'*W

            score = count_pass_vertical(transpose(new_prt), k)
            if score == len(prt[0]):
                return output_result, True
            output_result['states'].append(new_prt)

    else:
        output_result = {}
        output_result['tuples'] = [] # exclude idx list
        output_result['states'] = [] # excluded cell state

        tuples = sort_by_priority(tuples, score_a, score_b)
        for i in range(len(tuples)):
            tup = tuples[i]
            exclude_list = get_complementary_set(tup, D)

            for e in exclude_list:
                new_prt = states[i].copy()
                if e > 0:
                    new_prt[e-1] = '0'*W
                else:
                    new_prt[-e-1] = '1'*W

                score = count_pass_vertical(transpose(new_prt), k)
                if score == len(prt[0]):
                    return output_result, True
                output_result['tuples'].append(tup + [e])
                output_result['states'].append(new_prt)

    return output_result, False
            
            
    

if __name__ == '__main__':
    
#    sys.stdin = open('newsample.txt', 'r')
    sys.stdin = open('sample_input.txt', 'r')
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
        
        score_a, score_b = get_priority_idx(prt, K)
        out_result = {'tuples': [], 'states': [], 'priority': []}
        for _step in range(1, K):

            out_result, exit_cond = step(prt, out_result, K, score_a, score_b)
            if exit_cond:
                break

        if not exit_cond:
            _step = K

        print ('#{} {}'.format(test_case, _step))

        




















    #
