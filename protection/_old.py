import sys
import itertools
import time


class Protection():
    def __init__(self, prt_list, K):
        
        self.D = len(prt_list)
        self.W = len(prt_list[0])
        self.K = K
        self.p = prt_list
        #assert len(self.p) == D
        
        self.p_T = []
        self.cnt = 0
        for w in range(self.W):
            ver = ''.join([p[w] for p in prt_list])
            if '0'*self.K in ver or '1'*self.K in ver:
                self.cnt+=1
            self.p_T.append(
                ver
            )
        #assert len(self.p_T) == W
        # a: 0, b: 1

    def count_pass(self):
        return self.cnt


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)
            
def _step(prt_list, K, n_step):
    D = len(prt_list)
    W = len(prt_list[0])
    
    a_list = [i+1 for i in range(D)]
    b_list = [-i-1 for i in range(D)]
    pairs = itertools.combinations(a_list + b_list, n_step)
    
    for i, tup in enumerate(pairs):
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

def step(prt_list, K, n_step):
    D = len(prt_list)
    W = len(prt_list[0])

    pairs = itertools.combinations([i+1 for i in range(D)], n_step)
    for tup in pairs:
        # theres len(tup)**2 subtuples
#        if K > 2 * n_step:
        if True:
            subtuples = []
            msign_idx = itertools.combinations([0,1], len(tup))
            for m in msign_idx:
                # m: (0,1,0,0)
                _sub = []
                for _i, _m in enumerate(m):
                    if _m:
                        _sub.append(tup[_i])
                    else:
                        _sub.append(-tup[_i])
                subtuples.append(_sub)
        else:
            subtuples = []
            _sub = list(tup)
            subtuples.append(_sub)
            subtuples.append([-s for s in _sub])
        
        print (subtuples)
        for _t in subtuples:
            new_prt = prt_list.copy()
            for t in _t:
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

#    sys.stdin = open('newsample.txt', 'r')
    sys.stdin = open('sample_input.txt', 'r')
    T = int(input())
    T = 10
    for test_case in range(1, T+1):
        #t0 = time.time()
        D, W, K = map(int, input().split(' '))
        
        prt_list = []
        for d in range(D):
            prt_list.append(input().replace(' ', ''))

        W = len(prt_list[0])

        p = Protection(prt_list, K)
        if p.count_pass() == W:
            print ('#{} {}'.format(test_case, 0))
            continue

        #scores_a, scores_b = get_priority_idx(prt_list, K)
        #print ('{} / {}'.format(p.count_pass(), p.W))
        
        for s in range(1, K):
            result = step(prt_list, K, s)
            if result:
                break
        if not result:
            s = K

        #print (s, time.time() - t0)
        print ('#{} {}'.format(test_case, s))



    #
