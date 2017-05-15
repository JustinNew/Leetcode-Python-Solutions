def coinProbability(n, m):
    if m>n:
        return 0
    if m<0:
        return 0

    p =[[0 for i in range(n+1)] for j in range(n+1)]
    p[1][0] = 1
    p[1][1] = 1

    for i in range(2,n+1):
        p[i][0] = 1
        for j in range(1,i+1):
            p[i][j] = p[i-1][j] + p[i-1][j-1]

    print ('p[%d][%d] is %d.'%(n,m,p[n][m]))
    return p[n][m]*(0.5)**n

if __name__=='__main__':

    n = 10
    m = 5
    print ('%d heads out of %d coins is %f.'%(m, n, coinProbability(n,m)))
