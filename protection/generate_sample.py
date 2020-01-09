import numpy as np
f = open('newsample.txt', 'w')

T = 100
f.write(str(T) + '\n')

for t in range(T):
    D = np.random.randint(3, 14)
    W = np.random.randint(1, 21)
    K = np.random.randint(1, int(D)+1)
    line = '{} {} {}\n'.format(D, W, K)
    f.write(line)

    for d in range(D):
        line = np.random.randint(2, size=W)
        line = ' '.join([str(_l) for _l in line]) + '\n'
        f.write(line)
f.close()
