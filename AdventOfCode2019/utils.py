def fileToIntList(file):
    with open(file) as f: 
        return [float(s.strip()) for s in f.readlines()]