import sys
sys.stdin = open('sample_input.txt')



def bomb(bricks, wh, remove_dict):
    '''
    single shot / output is removing index
    '''
    w, h = wh
    n = bricks[w][h]
    
    # vertical
    for i in range(-n+1, n):
        if w+i >= W or w+i < 0:
            continue
        if len(bricks[w+i]) <= h:
            continue
                
        try:
            _ = remove_dict[(w+i,h)]
            # if it's already in the list: do nothing
        except:
            remove_dict[(w+i,h)] = 1
            bomb(bricks, (w+i,h), remove_dict)

    # horizontal
    for i in range(-n+1, n):
        if h+i >= H or h+i < 0:
            continue
        if len(bricks[w]) <= h+i:
            continue
        try:
            _ = remove_dict[(w,h+i)]
        except:
            remove_dict[(w,h+i)] = 1
            bomb(bricks, (w,h+i), remove_dict)
    return remove_dict
        


def shoot_1(brick_list):
    '''
    input is list of bricks
    output would be also list of bricks
    but len(output) = W*len(input)
    '''

    output_brick_list = []
    
    for bricks in brick_list:
        for w in range(len(bricks)):
            # simulates single block, single shot
            height = len(bricks[w]) - 1
            if height < 0:
                continue
            remove_dict = {(w,height): 1}
            remove_dict = bomb(bricks, (w,height), remove_dict)


            new_bricks = [[] for _ in range(len(bricks))]
            for _w in range(len(bricks)):
                new_bricks[_w] = [br_wh for i,br_wh in enumerate(bricks[_w]) if (_w,i) not in remove_dict]
            output_brick_list.append(new_bricks)
            
    return output_brick_list



T = int(input())
for test_case in range(1, T+1):
    
    N, W, H = map(int, input().split())
    
    _maps = []
    for h in range(H):
        _maps.append([int(i) for i in input().split()])


    # build new bricks for easier simulation: transposed / only use existing bricks
    bricks = [[] for _ in range(W)]
    # transpose
    for w in range(W):
        bricks[w] = [_maps[h][w] for h in range(H)]
    
    # backward and only existing blocks
    for w in range(W):
        bricks[w] = [i for i in bricks[w][::-1] if i > 0]
    bricks = [bricks]

    for n in range(N):
        bricks = shoot_1(bricks)

    if len(bricks) == 0:
        print ('#{} {}'.format(test_case, 0))
    else:
        min_bricks = H*W
        for br in bricks:
            num_bricks = sum([sum(len(_b) for _b in br)])
            if min_bricks > num_bricks:
                min_bricks = num_bricks
        
        print ('#{} {}'.format(test_case, min_bricks))
