def Perm(str, n, i):
    if i==n:
        print (str)

    for j in range(i, n):
        str[i], str[j] = str[j], str[i]
        Perm(str, n, i+1)
        str[i], str[j] = str[j], str[i]

if __name__=='__main__':
    
    str = list('abcde')
    Perm(str, len(str), 0)
