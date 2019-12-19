from copy import deepcopy
from collections import defaultdict 

class IntCode():
    def __init__(self):
        self.out = []
        self.input = []
        self.numParams = defaultdict(int)
        self.numParams[1] = 3
        self.numParams[2] = 3
        self.numParams[3] = 1
        self.numParams[4] = 1
        self.numParams[5] = 2
        self.numParams[6] = 2
        self.numParams[7] = 3
        self.numParams[8] = 3

    def main(self, code):
        i = 0
        while True:
            val = str(code[i])
            inst = int(val[-2:])
            paramTypes = val[:-2]
            if inst == 99:
                break

            numParams = self.numParams[inst]
            params = []
            origParams = []
            for j in range(i+1, i+1+numParams):
                origParams.append(code[j])
                if paramTypes == "":
                    params.append(code[code[j]])
                elif paramTypes[-1] == "1":
                    params.append(code[j])
                elif paramTypes[-1] == "0":
                    params.append(code[code[j]])

                paramTypes = paramTypes[:-1]

            jump = False

            if inst == 1:
                code[origParams[2]] = params[0] + params[1]
            elif inst == 2:
                code[origParams[2]] = params[0]* params[1]
            elif inst == 3:
                code[origParams[0]] = self.input[-1]
            elif inst == 4:
                self.out.append(params[0])
            elif inst == 5:
                if params[0] != 0:
                    i = params[1]
                    jump = True
            elif inst == 6:
                if params[0] == 0:
                    i = params[1]
                    jump = True
            elif inst == 7:
                if params[0] < params[1]:
                    code[origParams[2]] = 1
                else:
                    code[origParams[2]] = 0
            elif inst == 8:
                if params[0] == params[1]:
                    code[origParams[2]] = 1
                else:
                    code[origParams[2]] = 0
            if not jump:
                i += numParams + 1

        return code

with open('pr5_input.txt') as f:
    L = f.readline().split(',')
    L = list(map(int, L))
    print(L)
    intCode = IntCode()
    intCode.input =[5]
    res = intCode.main(L)
    print(intCode.out)
