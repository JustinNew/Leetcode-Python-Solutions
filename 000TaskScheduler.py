# 621. Task Scheduler

# Facebook Tag
# Count the number of idle slots. 
# Max idle slot is determined by (most_common_task_number - 1) * n
# Then minus other tasks' slots.

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        num_task = len(tasks)
        
        d = {}
        for i in tasks:

            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1

        d = sorted(d.items(), key=lambda x:x[1], reverse=True)

        max_value = d[0][1] - 1
        print(max_value)
        max_idles = max_value * n     

        for i in range(1, len(d)):
      
            max_idles -= min(max_value, d[i][1])

        if max_idles <= 0:
            return num_task
        else:
            return num_task + max_idles

    def leastInterval2(self, tasks, N):
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)   


    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        d = {}
        for i in tasks:
            d[i] = d.get(i, 0) + 1

        l = [(k, v) for k, v in d.items()]
        l.sort(key=lambda x: x[1], reverse=True)

        m = l[0][1]
        need = (m - 1) * n
        for i in range(1, len(l)):
            k, v = l[0], l[1]
            if v == m:
                need -= m - 1
            else:
                need -= v

        return len(tasks) + max(need, 0)
