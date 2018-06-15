# 299. Bulls and Cows

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        d_s = {}
        d_g = {}

        bulls = 0
        cows = 0
        for i in range(len(secret)):

            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in d_s:
                    d_s[secret[i]] += 1
                else:
                    d_s[secret[i]] = 1

                if guess[i] in d_g:
                    d_g[guess[i]] += 1
                else:
                    d_g[guess[i]] = 1

        for i in d_g:
            if i in d_s:
                cows += min(d_s[i], d_g[i])

        return str(bulls) + 'A' + str(cows) + 'B'

if __name__ == '__main__':

    so = Solution()
    print(so.getHint('1807', '7810'))
