import sys, re, math

if __name__ == "__main__":
    total = int(raw_input())
    for index in xrange(1, total + 1):
        row1 = int(raw_input())
        counter = 0
        while counter < 4:
            line = raw_input()
            counter += 1
            if counter == row1:
                cand1 = line.split()
        row2 = int(raw_input())
        counter = 0
        while counter < 4:
            line = raw_input()
            counter += 1
            if counter == row2:
                cand2 = line.split()
        res = list(set(cand1).intersection(cand2))
        print "Case #" + str(index) + ":",
        if len(res) == 1:
            print res[0]
        elif len(res) == 0:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"
