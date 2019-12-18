from copy import deepcopy

def main(code):
    i = 0
    while True:
        inst = code[i]
        if inst == 99:
            break
        inPosOne = code[i+1]
        inPosTwo = code[i+2]
        outPos   = code[i+3]
        if inst == 1:
            code[outPos] = code[inPosOne] + code[inPosTwo]
            i += 4
        elif inst == 2:
            code[outPos] = code[inPosOne] * code[inPosTwo]
            i += 4
        else:
            i += 1

    return code

with open('pr2_input.txt') as f:
    L = f.readline().split(',')
    L = list(map(int, L))
    print(L)
    for inputOne in range(0, 100):
        for inputTwo in range(100):
            code = deepcopy(L)
            code[1] = inputOne
            code[2] = inputTwo
            out = main(code)[0]
            if out == 19690720:
                print(100 * inputOne + inputTwo)
    inputTwo = 0
    main(L)
