# Calculate the moving average (with a fixed window size) of a data stream.

def MovingAverage(a, m):
    
    sum = 0
    ave = list()

    for i in range(m):
        sum += a[i]
        ave.append(sum/float(i+1))

    for i in range(m,len(a)):
        sum = sum + a[i] - a[i-m]
        ave.append(sum/float(m))

    return ave

if __name__=='__main__':

    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    m = 4

    average = MovingAverage(a,m)

    print average         
