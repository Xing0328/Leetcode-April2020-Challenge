class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = 0
        right = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                left += shift[i][1]
            else:
                right += shift[i][1]
        n = abs(right -left) % len(s)
        
        m = len(s)
        if left >= right:
            return s[n:] + s[:n]
        else:
            return s[m-n:] + s[:m-n]