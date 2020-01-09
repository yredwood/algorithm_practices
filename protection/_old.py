import sys
import itertools


class Protection():
    def __init__(self, prt_list, K):
        
        self.D = len(prt_list)
        self.W = len(prt_list[0])
        self.K = K
        self.p = prt_list
        #assert len(self.p) == D
        
        self.p_T = []
        for w in range(self.W):
            self.p_T.append(
                ''.join([p[w] for p in prt_list])
            )
        #assert len(self.p_T) == W
        # a: 0, b: 1

    def count_pass(self):
        cnt = 0
        for w in range(len(self.p_T)):
            if '0'*self.K in self.p_T[w] or '1'*self.K in self.p_T[w]:
                cnt+=1
        return cnt

def get_priority_idx(prt_list, K):
    D = len(prt_list)
    W = len(prt_list[0])

    p = Protection(prt_list, K)
    control_cnt = p.count_pass()
    
    # to a
    scores_a = []; scores_b = []
    for d in range(len(prt_list)):
        control_prt = prt_list.copy()
        control_prt[d] = '0'*W
        pc = Protection(control_prt, K)
        score = pc.count_pass() - control_cnt
        scores_a.append(score)

        control_prt = prt_list.copy()
        control_prt[d] = '1'*W
        pc = Protection(control_prt, K)
        score = pc.count_pass() - control_cnt
        scores_b.append(score)
        
    return scores_a, scores_b

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)
            
def step(prt_list, K, n_step, scores_a, scores_b):
    D = len(prt_list)
    W = len(prt_list[0])
    
    a_list = [i+1 for i in range(D)]
    b_list = [-i-1 for i in range(D)]
    pairs = itertools.combinations(a_list + b_list, n_step)
    
    scores = []; pair_list = []
    for tup in pairs:
        s = 0
        for t in tup:
            if t > 0:
                s += scores_a[t-1]
            else:
                s += scores_b[-t-1]
        scores.append(s)
        pair_list.append(tup)


    idx = argsort(scores)[::-1]
    sorted_pairs = [pair_list[i] for i in idx]
    sorted_scores = [scores[i] for i in idx]
    
    for i, tup in enumerate(sorted_pairs):
        #print (tup, sorted_scores[i])

        positive_tups = []
        flag = 0
        for t in tup:
            if t > 0:
                _t = t-1
            else:
                _t = -t-1
            if _t in positive_tups:
                flag = 1 

            positive_tups.append(_t)
        if flag:
            continue


        new_prt = prt_list.copy()
        for t in tup:
            if t > 0:
                new_prt[t-1] = '0'*W
            else:
                new_prt[-t-1] = '1'*W

        p = Protection(new_prt, K)
        score = p.count_pass()
        if score == W:
            return True
    
    return False


if __name__=='__main__':

    sys.stdin = open('newsample.txt', 'r')
    T = int(input())
    for test_case in range(1, T+1):

        D, W, K = map(int, input().split(' '))
        
        prt_list = []
        for d in range(D):
            prt_list.append(input().replace(' ', ''))

        W = len(prt_list[0])

        p = Protection(prt_list, K)
        if p.count_pass() == W:
            print ('#{} {}'.format(test_case, 0))
            continue

        scores_a, scores_b = get_priority_idx(prt_list, K)
        #print ('{} / {}'.format(p.count_pass(), p.W))
        
        for s in range(1, K+1):
            result = step(prt_list, K, s, scores_a, scores_b)
            if result:
                break
        if not result:
            s = K

        print ('#{} {}'.format(test_case, s))




    #
