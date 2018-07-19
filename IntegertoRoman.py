# 12. Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        l = [(k, v) for k,v in d.items()]
        l.sort(key=lambda x: x[0], reverse=True)

        result = []
        for pair in l: 
            while num >= pair[0]:
                result.append(pair[1])
                num -= pair[0]

        return ''.join(result)

if __name__ == '__main__':

    so = Solution()
    print(so.intToRoman(3888))
