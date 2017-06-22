def kth(self, A, B, k):
        if len(A) > len(B):
            A, B = (B, A)
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
    
        i = min(len(A)-1, k/2)
        j = min(len(B)-1, k-i)
    
        if A[i] > B[j]:
            return self.kth(A[:i], B[j:], i)
        else:
            return self.kth(A[i:], B[:j], j)
