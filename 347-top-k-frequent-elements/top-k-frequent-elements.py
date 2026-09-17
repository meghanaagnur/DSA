class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        count = {}
        buckets = [[] for _ in range(n+1)] 
        result = []
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num,freq in count.items():
            buckets[freq].append(num)
        for i in range(n,-1,-1):
            temp = buckets[i]
            for j in temp:
                result.append(j)
                if (len(result)==k):
                    return result
