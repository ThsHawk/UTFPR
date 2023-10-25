import sys

def sortTime(a):
    return a[1]

def sortArrive(a):
    return a[2]

def arrived(counter, queue):
    if queue == None:
        return 0
    elif queue[2] <= counter:
        return 1
    else:
        return 0

def main():
    argvLen = len(sys.argv)
    if argvLen < 2:
        print("ERR: Too few arguments!")
        exit()
    elif argvLen > 2:
        print("ERR: Too many arguments!")
        exit()
    else:
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            print("file \'" + sys.argv[1] + "\' not found")
            exit()
            
        lines = file.readlines()
        #lines[0] -- processos
        #lines[1] -- tempo
        #lines[2] -- chegada
        for i in range(len(lines)):
            lines[i] = lines[i][:len(lines[i])-1]
            lines[i] = lines[i].split("\t")
            lines[i].pop(0)

        queue = list()
        for i in range(len(lines[0])):
            queue.append((lines[0][i], int(lines[1][i]), int(lines[2][i])))
        queue.sort(key=sortArrive)
        
        counter = 0
        execTime = 0
        waitQueue = list()
        waitQueue.append(queue[0])
        queue.pop(0)
        records = list()
        while(len(waitQueue) != 0):
            if len(queue) != 0:
                if arrived(counter, queue[0]):
                    waitQueue.append(queue[0])
                    waitQueue.sort(key=sortTime)
                    queue.pop(0)
            aux = list(waitQueue[0])
            aux[1] -= 1
            waitQueue[0] = (aux[0], aux[1], aux[2])
            counter += 1
            execTime += 1
            print(aux)
            if waitQueue[0][1] == 0:
                records.append((waitQueue[0][0], waitQueue[0][2], counter, execTime))
                execTime = 0
                waitQueue.pop(0)

        print(records)
                


        file.close()

main()