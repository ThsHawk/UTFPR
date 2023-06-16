import sys
import random

op = ["i", "s", "r"]

if len(sys.argv) == 4:

    try:
        quantity = int(sys.argv[1])
        start = int(sys.argv[2])
        stop = int(sys.argv[3])
    except ValueError:
        print("unsuported arguments")
        exit()

    random.seed()
    v = []
    file = None
    i = 1
    while file == None:
        try:
            file = open("input" + str(i) + ".txt", "x")
        except FileExistsError:
            i += 1
    file = open("input" + str(i) + ".txt", "w")
    for i in range(quantity):
        randOp = random.randrange(0, 2)
        randOp = op[randOp]
        file.write(randOp + ", " + str(random.randrange(start, stop)) + "\n")
    file.close()