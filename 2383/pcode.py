import sys
sys.stdin = open("sample_input.txt", "r")

import itertools


class Humans():
    def __init__(self, floor_maps):
        # human -> coord:(x,y), dest: {0, 1} , dist: d, tto: {-10123}
        
        human_list = [] 
        dst_list = []
        self.N = len(floor_maps)
        for x in range(self.N):
            for y in range(self.N):
                if floor_maps[x][y] == 0:
                    continue
                elif floor_maps[x][y] == 1:
                    # human
                    h = {'loc': (x,y)}
                    human_list.append(h)
                else:
                    s = {'loc': (x,y), 
                            'depth': floor_maps[x][y]+1}
                    dst_list.append(s)
        
        self.human_list = human_list
        self.dst_list = dst_list

    def set_destinations(self, dsts):
        # dsts: (0,1,1,0,0,1)
        assert len(dsts) == len(self.human_list)
        for i, h in enumerate(self.human_list):
            h['dest'] = dsts[i]
            h['dist'] = abs(h['loc'][0] - self.dst_list[dsts[i]]['loc'][0]) \
                    + abs(h['loc'][1] - self.dst_list[dsts[i]]['loc'][1])
            h['tto'] = -1


    def step(self):
        for h in self.human_list:
            # 1. going to on-stairs
            if h['dist'] > 0:
                h['dist'] -= 1
                if h['dist'] == 0:
                    # set timer
                    h['tto'] = self.dst_list[h['dest']]['depth']
            else:
                # going down the stairs
                if h['tto'] > 0:
                    h['tto'] -= 1
        
        
        # go back for some conditions
        for _ in range(10):
            num_instairs = [0, 0]
            for h in self.human_list:
                c1 = h['tto'] > 0 and h['tto'] < self.dst_list[h['dest']]['depth']
                if c1:
                    num_instairs[h['dest']] += 1

            if num_instairs[0] <= 3 and num_instairs[1] <= 3:
                break

            for h in self.human_list:
                c1 = h['tto'] == self.dst_list[h['dest']]['depth'] - 1 and num_instairs[h['dest']] >= 3
                if c1:
                    h['tto'] += 1
                    break

#        for _ in range(10):
#            num_onstairs = [0, 0]
#            for h in self.human_list:
#                c1 = h['dist'] == 0 and h['tto'] == self.dst_list[h['dest']]['depth']
#                if c1:
#                    num_onstairs[h['dest']] += 1
#            if num_onstairs[0] < 3 and num_onstairs[1] < 3:
#                break
#
#            for h in self.human_list:
#                c1 = h['dist'] == 0 and h['tto'] == self.dst_list[h['dest']]['depth']
#                if c1:
#                    h['dist'] = 1
#                    h['tto'] = -1
            

        # count left
        num_humans = 0
        for h in self.human_list:
            if h['tto'] != 0:
                num_humans += 1
        return num_humans
            






T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())
    floor_map = []
    num_humans = 0
    for _ in range(N):
        floor_map.append([int(i) for i in input().split()])
        num_humans += sum(i for i in floor_map[-1] if i==1)


    humans = Humans(floor_map)
    comb = itertools.product([0,1], repeat=num_humans)
    min_time = 100
    for c in comb:
        humans.set_destinations(c)
        for t in range(1, 100):

            if humans.step() == 0:
                break
        if t < min_time:
            min_time = t
        
        
    print ('#{} {}'.format(test_case, min_time))



#
