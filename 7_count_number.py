class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = 0
        for num in arr:
            if num + 1 in arr:
                cnt += 1
        return cnt