# Given an array of integers where 1<=a[i]<=n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Please do no use extra space and run time is O(n). 
import copy

def MissingValue(a):

    l = list()

    for i in range(len(a)):
        index = abs(a[i])-1
        if a[index]>0:
            a[index] *= -1

    for i in range(len(a)):
        if a[i]>0:
            l.append(i+1)

    return l

def MissingValue2(a):

    l = list()

    for i in range(len(a)):
        # This is tricky.
        # Using while instead of if.
        while i+1 != a[i] and a[a[i]-1] != a[i]:
            i1 = i
            i2 = a[i] - 1
            a[i1],a[i2] = a[i2], a[i1]

    for i in range(len(a)):
        if i+1 != a[i]:
            l.append(i+1)

    return l

if __name__=='__main__':

    a1 = [4,3,2,7,8,2,3,1]
    a2 = copy.copy(a1)

    print a1
    print MissingValue(a1)
    print a1
    print MissingValue2(a2)
    print a2
