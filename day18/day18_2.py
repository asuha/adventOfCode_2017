import threading

class Program(threading.Thread):

    def __init__(self, program_id, command_lines, condition, channel):
        threading.Thread.__init__(self)
        self.variables = {}
        self.variables['p'] = program_id

        self.channel = channel
        self.send_count = 0

        self.program_id = program_id
        self.command_lines = command_lines
        self.condition = condition

    def is_int(self, string):
        try: 
            int(string)
            return True
        except ValueError:
            return False

    def get_value(self, value):
        if self.is_int(value):
            return int(value)
        return int(self.variables[value])

    def run(self):
        pos = 0
        while pos < len(self.command_lines):
            line = self.command_lines[pos].split(' ')

            pos += 1

            if line[1] not in self.variables: 
                self.variables[line[1]] = 0

            if len(line) > 2:
                p2 = self.get_value(line[2])

            if line[0] == 'set':
                self.variables[line[1]] = p2

            elif line[0] == 'add':
                self.variables[line[1]] += p2

            elif line[0] == 'mul':
                self.variables[line[1]] *= p2

            elif line[0] == 'mod':
                self.variables[line[1]] %= p2

            elif line[0] == 'rcv':
                self.condition.acquire()
                obj = None
                while obj == None:
                    for v in self.channel:
                        if v['id'] != self.program_id:
                            obj = v
                            break
                    if obj == None:
                        self.condition.wait()
                self.variables[line[1]] = obj['message']
                self.channel.remove(obj)
                self.condition.release()

            elif line[0] == 'snd':
                self.condition.acquire()
                self.channel.append({'id': self.program_id, 'message': self.variables[line[1]]})
                self.send_count += 1
                if self.program_id == 1:
                    print("Program " + str(self.program_id) + " sent " + str(self.send_count) + " messages")
                self.condition.notify()
                self.condition.release()
       
            elif line[0] == 'jgz':
                p1 = self.get_value(line[1])
                if p1 > 0:
                    pos += p2 - 1


with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    channel = []
    condition = threading.Condition()
    p0 = Program(0, input, condition, channel)
    p1 = Program(1, input, condition, channel)
    p0.start()
    p1.start()
    p0.join()
    p1.join()