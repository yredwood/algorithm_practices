import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    
    mountain = []
    top = 0
    for _ in range(N):
        _input =  [int(i) for i in input().split()]
        mountain.append(_input)
        top = max(_input) if max(_input) > top else top
    
    
    # path: {'joker': False, 'path': [(3,4),(4,4),...], 'last_height': 4}
    # find largest num indexes
    start_points = []
    for x in range(N):
        for y in range(N):
            if mountain[x][y] == top:
                start_points.append((x,y))
        
    prev_path = []
    for i in range(len(start_points)):
        prev_path.append(
            {'joker': False, 'path': [start_points[i]], 'last_height': 
                top}
        )
        
    
    for max_path_length in range(N**2):
        path_list = []
        for path in prev_path:
            # 1. add 4 directions 
            x,y = path['path'][-1]
            new_point_list = [
                (x+1,y), (x-1,y), (x,y-1), (x,y+1)
            ]
            
            for np in new_point_list:
                new_dict = {}
                nx, ny = np
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    # out of box case
                    continue

                if np in path['path']:
                    # revisit case
                    continue
                
                long_condition = mountain[nx][ny] >= path['last_height'] and \
                        not path['joker'] and \
                        mountain[nx][ny] - K < path['last_height'] 
                if long_condition:
                    new_dict['joker'] = True
                    new_dict['path'] = path['path'] + [np]
                    new_dict['last_height'] = path['last_height'] - 1
                    path_list.append(new_dict)
                    continue

                if mountain[nx][ny] < path['last_height']:
                    # simple descending case
                    new_dict['joker'] = path['joker']
                    new_dict['path'] = path['path'] + [np]
                    new_dict['last_height'] = mountain[nx][ny]
                    path_list.append(new_dict)
            
        if len(path_list) == 0:
            break

        prev_path = path_list

    print ('#{} {}'.format(test_case, max_path_length+1))









    #
