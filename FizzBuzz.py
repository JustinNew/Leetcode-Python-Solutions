# Output string representation from 1 to n.
# When it's multiples of three output 'Fizz'
# When it's multiples of five output 'Buzz'
# When it's multiples of three and five output 'FizzBuzz'

def FizzBuzz(n):

  
    l = list()
    a = 1
    while a <= n:
        if a%5==0 and a%3==0:
            l.append('FizzBuzz')
        elif a%5==0:
            l.append('Buzz')
        elif a%3==0:
            l.append('Fizz')
        else:
            l.append(str(a))

        a += 1

    print l
    return


if __name__ == '__main__':
    n = 15
    FizzBuzz(n)  
