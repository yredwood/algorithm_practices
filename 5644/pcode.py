import sys
sys.stdin = open('sample_input.txt')

import itertools

def add_dict(d, key, value):
    if key[0] <= 0 or key[0] > 10:
        return d
    if key[1] <=0 or key[1] > 10:
        return d
    try:
        d[key].append(value)
    except:
        d[key] = [value]
    return d

def move(coord, num):
    if num == 0:
        return coord
    if num == 1:
        return (coord[0], coord[1]-1)
    if num == 2:
        return (coord[0]+1, coord[1])
    if num == 3:
        return (coord[0], coord[1]+1)
    if num == 4:
        return (coord[0]-1, coord[1])

class ApMap():
    def __init__(self, aps):
        d = {}
        performance = []
        for idx, ap in enumerate(aps):
            (x,y), c, p = ap
            performance.append(p)
            
            for i in range(c+1):
                if i == 0:
                    for j in range(-c, c+1):
                        d = add_dict(d, (x+i, y+j), idx)
                else:
                    for j in range(-c+i, c-i+1):
                        d = add_dict(d, (x+i, y+j), idx)
                        d = add_dict(d, (x-i, y+j), idx)

        self.d = d
        self.p = performance

    def get_val(self, key):
        try:
            out = self.d[key]
            return max([self.p[o] for o in out])
        except:
            return 0

    def calc(self, p1, p2):
        xy1 = (1,1)
        xy2 = (10,10)
        
        out = self.get_val(xy1) + self.get_val(xy2)

        for t in range(len(p1)):
            xy1 = move(xy1, p1[t])
            xy2 = move(xy2, p2[t])
            
            shared = False
            try:
                k1 = self.d[xy1]
                k2 = self.d[xy2]
                for _k in k1:
                    if _k in k2:
                        shared = True
            except:
                pass

            if shared:
                _maxval = 0
                for _k1 in k1:
                    for _k2 in k2:
                        if _k1 == _k2:
                            val = self.p[_k1]
                        else:
                            val = self.p[_k1] + self.p[_k2]
                        if val > _maxval:
                            _maxval = val

                out += _maxval
            else:
                out += self.get_val(xy1) + self.get_val(xy2)

        return out

T = int(input())
for test_case in range(1, T+1):
    M, A = map(int, input().split())
    
    p1 = [int(i) for i in input().split()]
    p2 = [int(i) for i in input().split()]

    aps = []
    for i in range(A):
        x, y, c, p = map(int, input().split())
        aps.append([(x,y),c,p])
        
    apmap = ApMap(aps)
    out = apmap.calc(p1, p2)
    print ('#{} {}'.format(test_case, out))
