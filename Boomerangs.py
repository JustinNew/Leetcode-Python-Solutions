class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        pairdistance = []
        pair_1 = []
        pair_2 = []

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                temp = (points[i][0]-points[j][0])*(points[i][0]-points[j][0])
                temp = temp + (points[i][1]-points[j][1])*(points[i][1]-points[j][1])
                pairdistance.append(temp)
                pair_1.append(i)
                pair_2.append(j)

        #print (pairdistance)
        #print (pair_1)
        #print (pair_2)

        result = 0
        for i in range(len(pairdistance)-1):
            for j in range(i+1, len(pairdistance)):
                t_l = [pair_1[i],pair_2[i],pair_1[j],pair_2[j]]
                t = len(set(t_l))
                if pairdistance[j]==pairdistance[i] and t==3: 
                    #print (pair_1[i],pair_2[i],pair_1[j],pair_2[j])
                    result += 2

        return result

    def numberOfBoomerangs2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        pairdistance = []
        pair_1 = []
        pair_2 = []

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                temp = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2) 
                pairdistance.append(temp)
                pair_1.append(i)
                pair_2.append(j)

        result = 0
        for i in range(len(pairdistance)-1):
            for j in range(i+1, len(pairdistance)):
                if pairdistance[j]==pairdistance[i] and (pair_1[i]==pair_1[j] or pair_1[i]==pair_2[j] or pair_2[i]==pair_1[j] or pair_2[i]==pair_2[j]):
                    result += 2

        return result

# for each point, create a hashmap and count all points with same distance. 
# If for a point p, there are k points with distance d, number of boomerangs corresponding to that are k*(k-1).
    def numberOfBoomerangs3(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return 0
        res = 0
        for i in range(len(points)):
            pDict = {}
            for j in range(len(points)):
                if j == i:
                    continue
                dis = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                key = str(dis)
                if key in pDict:
                    pDict[key] += 1
                else:
                    pDict[key] = 1
            for p in pDict:
                if pDict[p] > 1:
                    res += pDict[p] * (pDict[p] - 1)
        return res


if __name__=='__main__':

    points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]] 
    #points = [[0,0],[1,0],[2,0]] 

    so = Solution()

    print (so.numberOfBoomerangs2(points))
