import numpy
class Turing:

    def __init__(self):
        self.tape = numpy.zeros(1000000)
        self.pointer = self.tape.size / 2
        self.next_state = self.exec_A

    def exec_A(self):
        if self.tape[self.pointer] == 0:
            self.tape[self.pointer] = 1
            self.next_state = self.exec_B
        else:
            self.tape[self.pointer] = 0
            self.next_state = self.exec_F
        
        self.pointer += 1
    
    def exec_B(self):
        if self.tape[self.pointer] == 1:
            self.next_state = self.exec_C

        self.pointer -= 1

    def exec_C(self):
        if self.tape[self.pointer] == 0:
            self.tape[self.pointer] = 1
            self.pointer -= 1
            self.next_state = self.exec_D
        else:
            self.tape[self.pointer] = 0
            self.pointer += 1

    def exec_D(self):
        if self.tape[self.pointer] == 0:
            self.tape[self.pointer] = 1
            self.pointer -= 1
            self.next_state = self.exec_E
        else:
            self.pointer += 1
            self.next_state = self.exec_A

    def exec_E(self):
        if self.tape[self.pointer] == 0:
            self.tape[self.pointer] = 1
            self.next_state = self.exec_F
        else:
            self.tape[self.pointer] = 0
            self.next_state = self.exec_D
        self.pointer -= 1

    def exec_F(self):
        if self.tape[self.pointer] == 0:
            self.tape[self.pointer] = 1
            self.pointer += 1
            self.next_state = self.exec_A
        else:
            self.tape[self.pointer] = 0
            self.pointer -= 1
            self.next_state = self.exec_E


    def run(self, steps):
        count = 0
        while count < steps:
            count += 1
            self.next_state()
        
        return numpy.count_nonzero(self.tape)


turing = Turing()

checksum_steps = 12425180

print "Parte 1: " + str(turing.run(checksum_steps))
