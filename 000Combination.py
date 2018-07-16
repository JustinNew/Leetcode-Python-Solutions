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

# Combination of [1,1,2]: [[1], [1, 1], [2], [1, 2], [1, 1, 2]]
def combination(list):

    list.sort()

    if len(list) == 0:
        return []
    if len(list) == 1:
        return [[list[0]]]

    result = [[list[0]]]
    for i in range(1, len(list)):
        if list[i] != list[i - 1]:
            temp = []
            temp.append([list[i]])
            for l in result:
                temp.append(l + [list[i]])
        else:
            if i == 1:
                temp = [k for k in result]
            t = []
            for l in temp:
                t.append(l + [list[i]])
            temp = [k for k in t]
        result += [k for k in temp]

    return result

if __name__=='__main__':
    
    str = list('abcde')
    Combination(str, len(str), 3)
