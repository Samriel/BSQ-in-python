import random
import numpy as np
density = int(input('input density percent: '))

for i in range(int(input('input number of maps: '))):
    nums = [i for i in range(32, 127)]
    random.shuffle(nums)
    char_list = [nums.pop() for _ in range(3)]
    x = random.randint(3, 31)
    y = random.randint(3, 31)
    obs_map = [[chr(np.random.choice(char_list, p=[1-density/100, density/100, 0]))
                for _ in range(x)] for _ in range(y)]
    with open('map'+str(i)+'.txt', 'w+') as f:
        for sym in char_list:
            f.write(chr(sym))
        f.write('\n')
        for j in obs_map:
            for k in j:
                f.write(k)
            f.write('\n')
