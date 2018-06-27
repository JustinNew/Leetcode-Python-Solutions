# 406. Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sort first.
        # Move into position one by one.

        people.sort(key=lambda x: (x[0], x[1]))

        cur = 0
        while cur < len(people):

            num, require = people[cur]
            flag = 0
            have = 0
            for i in range(cur):
                if people[i][0] >= num:
                    have += 1

            i = cur + 1
            while have < require:
                flag = 1
                if people[i][0] >= num: 
                    have += 1
                people[i - 1], people[i] = people[i], people[i - 1]
                i += 1

            if flag == 0:
                cur += 1

        return people

    def reconstructQueue2(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # Sort first.
        # Move into position one by one.

        # Sort 'k' reversely.
        people.sort(key=lambda x: (x[0], -1 * x[1]))

        cur = len(people) -1
        while cur >= 0:
            num, require = people[cur]
            for i in range(cur + 1, len(people)):
                if require > 0:
                    people[i], people[i - 1] = people[i - 1], people[i]
                    require -= 1
                    if require == 0:
                        break
            cur -= 1

        return people            

if __name__ == '__main__':

    so = Solution()
    print(so.reconstructQueue2([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
