class Solution():

    def Cookie(self, child, cookie):

        import numpy as np
        child = np.sort(child)
        cookie = np.sort(cookie)

        i = len(child) - 1
        j = len(cookie) - 1

        count = 0
        while i>=0 and j>=0:
            if cookie[j] >= child[i]:
                count += 1
                i -= 1
                j -= 1
            else: 
                i -= 1
            
        return count

if __name__=='__main__':
    
    child = [1, 2]
    cookie = [1,2,3]

    s = Solution()

    result = s.Cookie(child, cookie)

    print 'Assigned %d cookies.'%result
