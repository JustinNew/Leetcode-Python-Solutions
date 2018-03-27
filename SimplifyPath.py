# 71. Simplify Path

# 1. Strip first '/'
# 2. Strip last '/'
# 3. Split on '/'
# 4. Go through the list and use stack to do operations.
# 5. Corner cases: '///', '/..', '/'

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        if path and path[0] == '/':
            path = path[1:]
        if path and path[-1] == '/':
            path = path[:-1]

        if len(path) == 0:
            return '/'
        
        d = path.split('/')
        s = []

        for i in d:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(s) != 0:
                    s.pop()
            else:
                s.append(i)

        n = ['/' + i for i in s]
        if len(n) == 0:
            return '/'
        else:
            return ''.join(n)

if __name__ == '__main__':

    s = Solution()
    print(s.simplifyPath('///'))
