def bestfit(bsize,m,psize,n):


    allocation = [-1]*n

    for i in range (n):
        bidx = -1
        for j in range (m):
            if bsize[j] >= psize[i]:
                if bidx == -1:
                    bidx = j
                elif bsize[bidx] < bsize[j]:
                    bidx = j
        if bidx !=-1 :
            allocation[i] = bidx
            bsize[bidx] -= psize[i]
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", psize[i], 
                                end = "        \t\t ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1) 
        else:
            print("Not Allocated")

if __name__ == '__main__':
    bsize = [100, 500, 200, 300, 600] 
    psize = [212,417,112,426]

    m = len(bsize)
    n = len(psize)
    
    bestfit(bsize,m,psize,n)
