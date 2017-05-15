class Solution():

    def RN(self, RansonNote, Magazine):
        l = {}
        for i in range(len(Magazine)):
            if Magazine[i] in l.keys():
                l[Magazine[i]] = l[Magazine[i]] + 1
            else:
                l[Magazine[i]] = 1

        for i in range(len(RansonNote)):
            if RansonNote[i] in l.keys():
                l[RansonNote[i]] = l[RansonNote[i]] - 1
            else:
                l[RansonNote[i]] = -1

        for i in range(len(RansonNote)):
            if l[RansonNote[i]] < 0:
                return False

        return True

if __name__=='__main__':

    s = 'abcdedf'
    t = 'abcdedfgefds'

    so = Solution()
    
    print so.RN(s, t)
