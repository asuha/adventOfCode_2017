class Stack:
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        return self.items.pop()

class Bridge:
    def __init__(self,input):
        self.input = input
        self.stack = Stack()
        self.max_strength = 0
        self.max_length = 0
        self.max_length_strength = 0

    def calculate_strength(self):
        regex = re.compile(r"([0-9]+)/([0-9]+)")
        strength = 0
        for v in self.stack.items:
            values = regex.match(v)
            strength += int(values.group(1))
            strength += int(values.group(2))
        
        return strength
    
    def calculate_info(self):
        length = len(self.stack.items)
        strength = self.calculate_strength()

        if length >= self.max_length:
            self.max_length = length
            if strength > self.max_length_strength:
                self.max_length_strength = strength
             
        if strength > self.max_strength:
            self.max_strength = strength

    def get_values(self, number):
        regex = "(^x\/[0-9]+),|,(x\/[0-9]+),|,([0-9]+\/x),|([0-9]+\/x\Z)".replace('x',str(number))
        regex = re.compile(regex)
        values = list()
        for v in regex.findall(self.input):
            for i in v:
                if i != "":
                    values.append(i)
                    break
        return values
    
    def get_next_value(self, number, cur_value):
        regex = "x/([0-9]+)|([0-9]+)/x".replace('x', str(number))
        regex = re.compile(regex)
        return int(filter(None, regex.match(cur_value).groups())[0])
        

    def check_length(self, value):
        values = self.get_values(value)

        for cur_v in values:
            if cur_v in self.stack.items:
                continue

            self.stack.push(cur_v)
            self.check_length(self.get_next_value(value, cur_v))

            self.stack.pop()
        
        self.calculate_info()

import re
with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')
    input = str.join(',,', input)

    bridge = Bridge(input)

    bridge.check_length(0)

    print("Parte 1: " + str(bridge.max_strength))
    print("Parte 2: " + str(bridge.max_length_strength))
