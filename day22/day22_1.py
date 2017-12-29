import numpy as np
class Virus():
    N = [-1,0]
    S = [1,0]
    W = [0,-1]
    E = [0,1]

    def __init__(self,matrix):
        self.matrix = matrix
        self.direction = None
        self.pos = [len(matrix)/2, len(matrix[0])/2]
        self.infections = 0

    def _change_direction(self):
        cur_status = self.matrix[self.pos[0], self.pos[1]]

        if cur_status == 0:
            if self.direction == self.E:
                self.direction = self.N
            elif self.direction == self.W:
                self.direction = self.S
            elif self.direction ==  self.S:
                self.direction = self.E
            else:
                self.direction = self.W
            
        else:
            if self.direction == self.E:
                self.direction = self.S
            elif self.direction == self.W:
                self.direction = self.N
            elif self.direction ==  self.S:
                self.direction = self.W
            else:
                self.direction = self.E

    def _change_state(self):
        if matrix[self.pos[0]][self.pos[1]] == 1:
            matrix[self.pos[0]][self.pos[1]] = 0
        else:
            matrix[self.pos[0]][self.pos[1]] = 1
            self.infections += 1

    def _move(self):
        self.pos = np.sum((self.pos, self.direction), 0)

    def burst(self):
        self._change_direction()
        self._change_state()
        self._move()


with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day22/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')
    
    for i, v in enumerate(input):
        input[i] = list(v)
    
    input = np.array(input) == "#"
    input = input.astype(int)

    #Prepare matrix with map inside
    matrix = np.zeros((10000,10000))
    start_pos = len(matrix)/2 - (len(input)/2)
    matrix[start_pos:start_pos + len(input),start_pos:start_pos + len(input)] = input

    virus = Virus(matrix)

    bursts = 0
    while bursts < 10000:
        bursts += 1
        virus.burst()

    print("Parte 1: " + str(virus.infections))

