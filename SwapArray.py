a = [1,2,3,4,5,6]
b = [2,1,4,3,6,5]

print (b)
swap = 0
for i in range(len(a)):
    print (a)
    if a[i] != b[i]:
        swap += 1
        for j in range(i+1, len(a)):
            if a[j] == b[i]:
                a[i], a[j] = a[j], a[i]

print (swap)
