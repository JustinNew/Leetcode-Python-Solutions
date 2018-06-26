# 394. Decode String

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        strings = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'

        result = ''

        i = 0
        num = ''
        while i < len(s):

            if s[i] in strings and not num:
                result += s[i]
                i += 1
            elif s[i] in strings and num:
                result += num * s[i]
                num = ''
                i += 1
            elif s[i] == '[':
                pos = 1
                temp = ''
                while pos != 0:
                    i += 1
                    if s[i] == '[':
                        pos += 1
                    elif s[i] == ']':
                        pos -= 1
                    temp += s[i]
                temp = temp[:-1]
                temp = self.decodeString(temp)
                if num:
                    result += num * temp
                    num = ''
                else:
                    result += temp
                i += 1
            elif s[i] in digits:
                while s[i] in digits:
                    num += s[i]
                    i += 1
                num = int(num)

        return result

if __name__ == '__main__':

    so = Solution()
    print(so.decodeString("2[abc]3[cd]ef"))
