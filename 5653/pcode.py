import sys
sys.stdin = open('sample_input.txt')


class Cells:
    def __init__(self, init):
        
        # cells are 
        self.cell_coord = []
        self.cell_life = []
        self.time_tob_activated = []
        self.time_to_dead = []
        self.cell_status = [] # 0: deactivated, 1: activated, 2: dead 

        self.key_dicts = {}

        for i in range(len(init)):
            for j in range(len(init[0])):
                if init[i][j]==0:
                    continue

                self.cell_coord.append((i,j))
                self.cell_life.append(init[i][j])
                self.time_tob_activated.append(init[i][j])
                self.time_to_dead.append(init[i][j])
                self.cell_status.append(0)
                self.key_dicts[(i,j)] = 1
    
    def step(self):

        new_cell_lists = [] # (x,y)
        new_cell_lifes = []
    
        for i in range(len(self.cell_status)):
            if self.cell_status[i] == 2:
                # dead: do nothing
                pass

            elif self.cell_status[i] == 0:
                # deactivated
                self.time_tob_activated[i] -= 1
                if self.time_tob_activated[i] == 0:
                    self.cell_status[i] = 1

            elif self.cell_status[i] == 1:
                # activated: reproduce and decrease ttd
                c = self.cell_coord[i]
                newpoints = [(c[0]-1,c[1]), (c[0]+1,c[1]),
                        (c[0],c[1]-1), (c[0],c[1]+1)]
                for np in newpoints:
                    try:
                        _ = self.key_dicts[np]
                    except:
                        new_cell_lists.append(np)
                        new_cell_lifes.append(self.cell_life[i])

                self.time_to_dead[i] -= 1
                if self.time_to_dead[i] == 0:
                    self.cell_status[i] = 2

        added_cell_lists = []
        added_life_lists = []
        for i in range(len(new_cell_lists)):
            coord = new_cell_lists[i]
            life = new_cell_lifes[i]
            if coord in added_cell_lists:
                _idx = added_cell_lists.index(coord)
                if added_life_lists[_idx] < life:
                    # remove prev one and add it
                    del added_cell_lists[_idx]
                    del added_life_lists[_idx]
                    added_cell_lists.append(coord)
                    added_life_lists.append(life)
            else:
                added_cell_lists.append(coord)
                added_life_lists.append(life)

        for i in range(len(added_cell_lists)):
            self.cell_coord.append( added_cell_lists[i] )
            self.cell_life.append( added_life_lists[i] )
            self.time_tob_activated.append( added_life_lists[i] )
            self.time_to_dead.append( added_life_lists[i] )
            self.cell_status.append( 0 )
            self.key_dicts[added_cell_lists[i]] = 1
    

    def get_num_alive(self):
        return sum([1 for i in self.cell_status if i<2])


T = int(input())
for test_case in range(1,T+1):
    
    N, M, K = map(int, input().split())
    init = []
    for n in range(N):
        init.append([int(i) for i in input().split()])

    cell = Cells(init)
    for k in range(K):
        cell.step()

    print ('#{} {}'.format(test_case, cell.get_num_alive()))
