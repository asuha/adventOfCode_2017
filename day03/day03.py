import math
import numpy as np

input = 361527

class Spiral():
    N = np.array([0,-1])
    S = np.array([0, 1])
    E = np.array([1, 0])
    W = np.array([-1,0])

    def __init__(self, matrixLenght, isAdjacentIncrementation):
        self.matrixLenght = matrixLenght
        self.initialPosition = [int(matrixLenght / 2),int(matrixLenght / 2)]
        self.position = self.initialPosition
        self.direction = Spiral.E
        self.value = 1
        self.matrix = np.array([np.array([None]*matrixLenght)]*matrixLenght)
        self.isAdjacentIncrementation = isAdjacentIncrementation

    def default_incrementation(self):
        self.value += 1

    def sum_adjacentes(self):
        result = 0
        bX = self.position[1] - 1
        bY = self.position[0] - 1

        for i in range(bY, bY + 3, 1):
            for j in range(bX, bX + 3, 1):
                if (self.matrix[i][j]):
                    result += self.matrix[i][j]
        self.value = result


    def check_direction(self, newDirection):
        newPosition = np.sum([newDirection, self.position], axis=0)

        if self.matrix[newPosition[0]][newPosition[1]] == None:
            self.direction = newDirection
        
    def generate(self, maxValue):
        
        while True:
            if self.position[0] >= len(self.matrix) or self.position[1] >= len(self.matrix[0]):
                break

            self.matrix[self.position[0]][self.position[1]] = self.value

            if (self.direction==Spiral.E).all():
                self.check_direction(Spiral.N)
            elif (self.direction==Spiral.N).all():
                self.check_direction(Spiral.W)
            elif (self.direction==Spiral.W).all():
                self.check_direction(Spiral.S)
            elif (self.direction==Spiral.S).all():
                self.check_direction(Spiral.E)

            self.position = np.sum([self.direction, self.position], axis=0)
            
            if self.isAdjacentIncrementation:
                self.sum_adjacentes()
                if self.value > maxValue:
                    return self.value
            else: 
                self.default_incrementation()
    
def parte1(matrixLenght):
    spiral = Spiral(matrixLenght, False)
    spiral.generate(None)

    resultPos = np.where(spiral.matrix==input)
    return abs(resultPos[0][0] - spiral.initialPosition[0]) + abs(resultPos[1][0] - spiral.initialPosition[1])

def parte2(matrixLenght):
    spiral = Spiral(matrixLenght, True)
    return spiral.generate(input)

matrixLenght = int(round(math.sqrt(input)) + 1)

print("Parte 1: " + str(parte1(matrixLenght)))
print("Parte 2: " + str(parte2(matrixLenght)))