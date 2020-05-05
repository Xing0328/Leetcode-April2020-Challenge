class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        dirs = [[-1,0], [1,0],[0,1],[0,-1]]
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if nr >=0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == '1':
                    self.dfs(grid, nr, nc)
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if len(grid) == 0:
            return 0
        x = range(len(grid))
        y = range(len(grid[0]))
        
        for r in x:
            for c in y:
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    res += 1
        return res