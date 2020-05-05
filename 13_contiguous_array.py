class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        summ = 0
        res = 0
        sum_dic = {}
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            if sum(nums) == 1:
                return 2
            else:
                return 0
        else:
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    summ -= 1
                if nums[i] == 1:
                    summ += 1
                if summ == 0:
                    res = i+1
                elif summ in sum_dic:
                    res = max(res, i - sum_dic[summ] )
                else:
                    sum_dic[summ] = i
                
        return res
                