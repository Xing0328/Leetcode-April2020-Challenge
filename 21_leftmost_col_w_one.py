# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
       
        [m,n] = binaryMatrix.dimensions()
        
        col = -1
        i = 0
        j = n-1
        while i < m and j >=0:
            if binaryMatrix.get(i,j) == 0:
                i += 1
            else:
                col = j
                j -= 1
            
        return col
                
                    
        