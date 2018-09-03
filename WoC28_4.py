import sys

t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]

    chainList = []
    redundancyConnects = 0

    for a1 in range(m):
        x,y = input().strip().split(' ')
        x,y = [int(x),int(y)]

        if chainList == []:
            chainList.append([x,y])
        else:
            chainsFound = []
            chainIndex = 0
            loop = True
            while loop:
                a,b = x in chainList[chainIndex], y in chainList[chainIndex]
                if a ^ b:
                    if chainsFound == []:
                        chainList[chainIndex] += [x,y]
                        chainsFound.append(chainIndex)
                    else:
                        chainList[chainsFound[0]] += chainList[chainIndex]
                        chainList.pop(chainIndex)
                        chainIndex -= 1
                elif a and b:
                    redundancyConnects += 1
                    loop = False
                    chainsFound = [0]
                    break
                if chainIndex == len(chainList) - 1:
                    loop = False
                    break
                chainIndex += 1
            if chainsFound == []:
                chainList.append([x,y])
    chainList.sort()
    for i in range(len(chainList)):
        chainList[i] = len(chainList[i]) // 2
    total = 0
    currScore = 0
    for i in chainList:
        total += i*(i+1)/2 + i*(i+1)*(2*i+1)/6 + i * currScore
        currScore += i**2 + i
    total += redundancyConnects * currScore
    print(total)
