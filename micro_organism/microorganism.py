import sys

class Colony():
    def __init__(self, x,y,n,d):
        self.x = x
        self.y = y
        self.n = n
        self.d = d

        self.dead = 0

    def move(self):
        self.x += direction(self.d)[0]
        self.y += direction(self.d)[1]

    def get_loc(self):
        return (self.x, self.y)

    def boundary_check(self, N):
        if self.x==0 or self.x==N-1 or self.y==0 or self.y==N-1:
            # reached boundary
            self.d = opposite_dir(self.d)
            self.n = self.n // 2

    def set_dead(self):
        self.dead = 1
    
    def print_stat(self):
        print ('colony stat: ({},{},{},{} | {})'.format(
            self.x,self.y,self.n,self.d,self.dead))

def direction(num):
    if num == 1:
        return (-1,0)
    if num == 2:
        return (1,0)
    if num == 3:
        return (0,-1)
    if num == 4:
        return (0,1)

def opposite_dir(num):
    if num % 2 == 0:
        return num-1
    else:
        return num+1

#    if num == 1:
#        return 2
#    if num == 2:
#        return 1
#    if num == 3:
#        return 4
#    if num == 4:
#        return 3

def step(colony_list, N):
    
    locs = []; merge_list = []
    for c in colony_list:
        c.move()
        c.boundary_check(N)
        loc = c.get_loc()
        if (loc in locs) and (loc not in merge_list):
            # if merging condition
            merge_list.append(loc)
        locs.append(loc)
    
    # merge colonies
    merged_colonies = []
    for mergexy in merge_list:
        gather_colony = []
        for c in colony_list:
            loc = c.get_loc()
            if loc == mergexy:
                gather_colony.append(c)
        
        assert len(gather_colony) > 1
        n = 0
        max_n = 0
        for i, c in enumerate(gather_colony):
            c.set_dead()
            n += c.n
            
            # only save direction for largest n
            if c.n > max_n:
                max_n = c.n
                d = c.d
        
        merged_colonies.append(Colony(mergexy[0], mergexy[1], n, d))
    
    for c in colony_list:
        if not c.dead:
            merged_colonies.append(c)

    return merged_colonies


            


if __name__=='__main__':

    sys.stdin = open('sample_input.txt', 'r')
    T = int(input())
    for test_case in range(1, T+1):

        # read the first line
        N, M, K = map(int, input().split(' '))
        # N: num of blocks (N*N)
        # M: after M hours
        # K: num colonies
        
        # read colonies
        colonies = []
        for k in range(K):
            x,y,n,d = map(int, input().split(' '))
            colonies.append(Colony(x,y,n,d))
            # c = (x, y, n, d)
        
        for _ in range(M):
            colonies = step(colonies, N)
        output = sum([c.n for c in colonies])

        print ('#{} {}'.format(test_case, output))









    #
