class LRUCache:

    def __init__(self, capacity: int):
        self.len = capacity
        
        self.d = collections.OrderedDict()
    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.d:
            del self.d[key]
        elif len(self.d) == self.len:
            self.d.popitem(last=False)
        self.d[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)