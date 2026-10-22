class Solution:
    def merge(self,arr,left,right,mid):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0]* n1
        R = [0]* n2
        for i in range(0,n1):
            L[i] = arr[left + i] 
        for j in range(0,n2):
            R[j] = arr[mid + j + 1]
        i = j = 0
        k = left
        while(i<len(L) and j<len(R)):
            if L[i]<=R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i<n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j<n2:
            arr[k] = R[j]
            j += 1
            k += 1


    def mergesorthelper(self,arr,left,right):
        if left>= right:
            return 
        mid = (left + right) // 2
        self.mergesorthelper(arr,left,mid)
        self.mergesorthelper(arr,mid+1, right)
        self.merge(arr,left,right,mid)


    def sortArray(self, nums):
        arr = nums
        if len(nums)<2:
            return arr
        left = 0
        right = len(nums) - 1
        self.mergesorthelper(arr,left,right)
        return arr
    