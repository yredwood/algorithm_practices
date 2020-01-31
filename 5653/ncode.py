import sys
sys.stdin = open('sample_input.txt')


class Cells:
    def __init__(self, init):

        self.cells = {}
        
        '''
        # cell[coord] = {
            'life': n, 
            'time_to_be_activated': n, 
            'time_to_dead': n, 
            'cell_status': k, k \in {0,1,2}
        }
        '''
        for i in range(len(init)):
            for j in range(len(init[0])):
                if init[i][j]==0:
                    continue
                
                self.cells[(i,j)] = {
                    'life': init[i][j],
                    'ttb_activated': init[i][j],
                    'tt_dead': init[i][j],
                    'status': 0
                }
    
    def step(self):
        new_cell_list = [] # ((x,y),n)
        for key, val in self.cells.items():
            if val['status'] == 2:
                # dead: do nothing
                pass

            elif val['status'] == 0:
                # deactivated
                val['ttb_activated'] -= 1
                if val['ttb_activated'] == 0:
                    val['status'] = 1

            else: # status==1
                # key: coordinates
                new_points = [(key[0]-1,key[1]), (key[0]+1,key[1]),
                        (key[0],key[1]-1), (key[0],key[1]+1)]
                for np in new_points:
                    try:
                        _ = self.cells[np]
                    except:
                        new_cell_list.append((np, val['life']))
                
                val['tt_dead'] -= 1
                if val['tt_dead'] == 0:
                    val['status'] = 2

        added_coord = []
        added_life = []
        for coord, life in new_cell_list:
            if coord in added_coord:
                _idx = added_coord.index(coord)
                if added_life[_idx] < life:
                    del added_coord[_idx]
                    del added_life[_idx]
                    added_coord.append(coord)
                    added_life.append(life)
            else:
                added_coord.append(coord)
                added_life.append(life)

        
        for coord, life in zip(added_coord, added_life):
            self.cells[coord] = {
                'life': life,
                'ttb_activated': life,
                'tt_dead': life,
                'status': 0
            }


    def get_num_alive(self):
        n = 0
        for key, value in self.cells.items():
            if value['status'] < 2:
                n+=1
        return n


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
