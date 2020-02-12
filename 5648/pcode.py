import sys
sys.stdin = open('sample_input.txt')

def move(xy, m):
    x, y = xy
    if m==0:
        return (x, y+1)
    elif m==1:
        return (x, y-1)
    elif m==2:
        return (x-1, y)
    else:
        return (x+1, y)
        
        

class Atom_list():
    def __init__(self):
        self.d = {}
        self.energy = 0

    def add_list(self, x, y, m, k):
        self.d[(x,y)] = [(m, k)]

    def step_half_sec(self):
        new_d = {}
        merge_keys = []
        for key, value in self.d.items():
            nkey = move(key, value[0][0])
            try:
                new_d[nkey].append(value[0])
                if nkey not in merge_keys:
                    merge_keys.append(nkey)
            except:
                new_d[nkey] = [value[0]]
        
        for key in merge_keys:
            for mk in new_d[key]:
                self.energy += mk[1]
            del new_d[key]
        self.d = new_d


T = int(input())
for test_case in range(1, T+1):
    
    atom_list = Atom_list()

    N = int(input())
    for n in range(N):
        x, y, m, k = map(int, input().split())
        atom_list.add_list(x*2,y*2,m,k)
        
    for _t in range(4000):
        atom_list.step_half_sec()


    print ('#{} {}'.format(test_case, atom_list.energy))
