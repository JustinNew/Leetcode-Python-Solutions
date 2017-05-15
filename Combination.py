def Combination(str, n, i):
    new = list(' '*i)
    ComUtil(str, new, 0, n, 0, i)

def ComUtil(str, new, start, end, index, r):

    if index==r:
        print (new)
        return

    for i in range(start, end):
        if end-i>=r-index:
            new[index] = str[i]
            ComUtil(str, new, start+1, end, index+1, r)

if __name__=='__main__':
    
    str = list('abcde')
    Combination(str, len(str), 3)
