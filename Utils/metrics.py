def dist(x, y):
    '''
    Calculate the Euclidean distance between two points
    represented as n-tuples
    '''
    return p_norm(x, y, 2)

def taxi(x, y):
    '''
    Calculate the taxicab distance between two points
    represented as n-tuples
    '''
    total = 0
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            total += abs(x[i] - y[i])

    return total

def p_norm(x, y, p):
    '''
    Caluculate the Lp metric between two points
    represented as n-tuples
    '''
    total = 0
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            total += (x[i] - y[i])**p

    return total ** (1 / p)
