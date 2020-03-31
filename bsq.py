class Node:     # c structure analog
    def __init__(self):
        self.left = None    # link to left node
        self.up = None      # link to up node
        self.link = None    # link to last node of previous line
        self.symbol = None  # symbol of the node taken from input map
        self.number = None  # https://ru.stackoverflow.com/questions/485486/ДП-Наибольшая-квадратная-подматрица-из-единиц
        self.x = None       # symbols x position
        self.y = None       # symbols y position


file_name = 'map0.txt'                                      # input filename
with open(file_name, 'r') as f:
    characters = f.readline()                               # read first line
    bsq_map = f.readlines()                                 # read map
nodelist = [' ' for i in range(len(bsq_map[0])-1)]          # list of nodes (linking crutch)
for line in range(len(bsq_map)):                            # going through the map...
    for symbol in range(len(bsq_map[line]) - 1):
        if type(nodelist[0]) == str:                        # initial node
            node = Node()
            node.symbol = bsq_map[line][symbol]
            if bsq_map[line][symbol] == characters[0]:
                node.number = 1
            else:
                node.number = 0
            node.x = symbol
            node.y = line
            nodelist[symbol] = node
        else:
            if type(nodelist[-1]) == str:                               # first line of nodes is not finished
                node = Node()
                node.symbol = bsq_map[line][symbol]
                if bsq_map[line][symbol] == characters[0]:
                    node.number = 1
                else:
                    node.number = 0
                node.left = nodelist[symbol-1]
                node.x = symbol
                node.y = line
                nodelist[symbol] = node
            else:
                if symbol == 0:                                         # first line finished, node #0
                    node = Node()
                    node.symbol = bsq_map[line][symbol]
                    if bsq_map[line][symbol] == characters[0]:
                        node.number = 1
                    else:
                        node.number = 0
                    node.link = nodelist[-1]
                    node.up = nodelist[0]
                    node.x = symbol
                    node.y = line
                    nodelist[symbol] = node
                else:                                                   # all other nodes
                    node = Node()
                    node.symbol = bsq_map[line][symbol]
                    node.up = nodelist[symbol]
                    node.left = nodelist[symbol - 1]
                    if bsq_map[line][symbol] == characters[0]:
                        node.number = min(node.up.number, node.left.number, node.left.up.number) + 1  # link in the begining
                    else:
                        node.number = 0

                    node.x = symbol
                    node.y = line
                    nodelist[symbol] = node
f.close()
n_max = [0 for i in range(3)]               # array for biggest nodes value, x, y
while True:   # find biggest node
    if node.number > n_max[0]:              # searching for biggest value
        n_max[0] = node.number
        n_max[1] = node.x
        n_max[2] = node.y
    print(node.number, end='')
    if node.left is not None:
        node = node.left
    elif node.link is not None:
        node = node.link
        print()
    else:
        print()
        break

with open(file_name + 'solved', 'w+') as f:  # write answer to file
    for line in range(len(bsq_map)):
        for symbol in range(len(bsq_map[line]) - 1):
            if n_max[2] - n_max[0] <= line < n_max[2] and n_max[1] - n_max[0] <= symbol < n_max[1]:
                f.write(characters[2])
            else:
                f.write(bsq_map[line][symbol])
        f.write('\n')
