def main():
    start = 246515
    count = 0
    end  = 739105

    start += 1
    while True:
        if start >= end:
            break

        # check increasin
        correct = True
        for i in range(1, len(str(start))):
            if str(start)[i] < str(start)[i-1]:
                correct = False
                break

        if not correct:
            start += 1
            continue

        correct = False
        # check adj are the same
        for i in range(1, len(str(start))):
            if str(start)[i] == str(start)[i-1]:
                if i < 2 or str(start)[i-2] != str(start)[i]:
                    if i > len(str(start)) - 2 or str(start)[i] != str(start)[i+1]:
                        correct = True
                        break

        if correct:
            count += 1
            print(start)
        start += 1

    print(count)

print(main())
