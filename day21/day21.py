class Matrix:
    
    def __init__(self, rules):
        self.matrix = np.array([['.', '#', '.'],['.', '.', '#'],['#', '#', '#']])
        self.rules = rules

    def get_size(self, matrix):
        if matrix.size % 2 == 0:
            return 2
        return 3
    
    def get_regex(self, rule):
        string = ""
        if len(rule) == 2:
            string1 = rule[0] + rule[1] 
            string2 = rule[1] + rule[0]
            string = re.escape(string1) + "|" + re.escape(string2) 
        else:
            string1 = rule[0] + rule[1] + rule[2]
            string2 = rule[2] + rule[1] + rule[0]
            string = re.escape(string1)  + "|" + re.escape(string2)
        return re.compile(string)

    def check_submatrix(self, submatrix, rule):
        size = self.get_size(submatrix)
        a_rule = rule.split('/')
        
        if size % len(a_rule) != 0:
            return False

        count = 0
        while count < 4:
            if self._exec_rules(submatrix, a_rule):
                return True

            submatrix = np.rot90(submatrix)
            count += 1
        
        return False

    def _exec_rules(self, submatrix, a_rule):
        for index, value in enumerate(a_rule):
            regex = self.get_regex(value)
            string = ''.join(submatrix[index])

            if regex.match(string) == None:
                return False
        
        return True

    def get_submatrix(self, pos):

        size = self.get_size(self.matrix)
        
        if size == self.matrix[pos[0]].size:
            return self.matrix

        x_to = pos[0] + size
        y_to = pos[1]+ size

        return self.matrix[pos[0]: x_to, pos[1]:y_to]

    def generate_new_art(self):
        new_matrix = None
        x_matrix = None
        pos = [0,0]
        size = self.get_size(self.matrix)

        while pos[0] < len(self.matrix):
            submatrix = self.get_submatrix(pos)

            for r in self.rules:
                if self.check_submatrix(submatrix, r[0]):
                    value = r[1].split('/')
                    for i,v in enumerate(value):
                        value[i] = list(v)
                    
                    if x_matrix == None:
                        x_matrix = np.array(value)
                    else:
                        x_matrix = np.concatenate((x_matrix,value), 1) 
                    break

            pos[1] += size
            if pos[1] >= self.matrix[pos[0]].size:
                pos[0] += size
                pos[1] = 0
                if new_matrix == None:
                    new_matrix = x_matrix
                else:
                    new_matrix = np.concatenate((new_matrix, x_matrix), 0)
                x_matrix = None
            
        self.matrix = new_matrix


import numpy as np
import re
with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day21/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    rules = [None]* len(input)

    for i,r in enumerate(input):
        cur_r = r.split(' => ')
        
        rules[i] = (cur_r[0],cur_r[1])

    matrix1 = Matrix(rules)
    matrix2 = Matrix(rules)

    for i in range(5):
        matrix1.generate_new_art()

    for i in range(18):
        matrix2.generate_new_art()


    print "Parte 1: " + str(np.count_nonzero(matrix1.matrix == '#'))
    print "Parte 2: " + str(np.count_nonzero(matrix2.matrix == '#'))