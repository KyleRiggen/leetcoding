class Solution:
    def make(self,A):
        if A:
            m       =  len(A)//2
            n       =  TreeNode(A[m])
            n.left  = self.make(A[   :m])
            n.right = self.make(A[m+1:] )
            return n
    def sortedListToBST(self, head):
        A, n = [], head
        while n:
            A.append(n.val)
            n = n.next
        return self.make(A)