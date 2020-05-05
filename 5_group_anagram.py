class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sol={}
        if len(strs) <= 0:
            return strs
        else:
            for i in range(len(strs)):
                temp = strs[i]
                sorted_temp = ''.join(sorted(temp))
                if sorted_temp in sol:
                    sol[sorted_temp].append(temp)
                else:
                    sol[sorted_temp] = [temp]
        return sol.values()