class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        cnt = 0
        n = len(nums)
        d = {}
        d[0] = 1
        s=0
        
        for i in range(n):
            s += nums[i]
            
            if s - k in d:
                cnt += d[s-k]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        
                            
        return cnt