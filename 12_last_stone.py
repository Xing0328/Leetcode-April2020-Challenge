class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones =  sorted(stones)
            x = stones.pop()
            y = stones.pop()
            if x > y:
                stones.append(x - y)
        if stones != []:
            return stones[0]
        else:
            return 0