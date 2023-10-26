import sys

def sortName(a):
    return a[0]

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
        processAmount = len(queue)
        waitingTime = queue.copy()
        waitQueue = list()
        waitQueue.append(queue[0])
        queue.pop(0)
        records = list()
        print("\n\n---TimeLine---")
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
            print(aux[0].upper() + " ", end="")
            if waitQueue[0][1] == 0:
                records.append((waitQueue[0][0], counter - waitQueue[0][2], waitQueue[0][2]))
                waitQueue.pop(0)            
        print("\n\n")
        media = 0
        for i in range(processAmount):
            media = media + records[i][1]
        media = media / processAmount
        print("---TempoMedioDeResposta---")
        print("TMR - " + str(media) + "\n")
        waitingTime.sort(key=sortName)
        records.sort(key=sortName)
        time = 0
        for i in range(processAmount):
            time = time + (records[i][1] - waitingTime[i][1])
        time = time / processAmount
        print("---TempoMedioDeEspera---")
        print("TME - " + str(time) + "\n\n")
        


        file.close()

main()