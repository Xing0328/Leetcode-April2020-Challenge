'''
This solution works, but not time efficient

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.len = len(nums) 
        self.arr = nums

    def showFirstUnique(self) -> int:
        if self.len == 0:
            return -1
        
        dic = {}
        for num in self.arr:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        for i in range(self.len):
            if dic[self.arr[i]] == 1:
                return self.arr[i]
        return -1

    def add(self, value: int) -> None:
        self.arr.append(value)
        self.len += 1

'''

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.arr = []
        self.dic = {}
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        while len(self.arr) >0 and self.dic[self.arr[0]] > 1:
            self.arr.pop(0)
            
        if len(self.arr) == 0:
            return -1
        return self.arr[0]
       

    def add(self, value: int) -> None:
        if value in self.dic:
            self.dic[value] += 1
            
        else:
            self.dic[value] = 1
            self.arr.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)