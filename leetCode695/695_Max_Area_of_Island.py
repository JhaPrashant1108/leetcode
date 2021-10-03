class Solution:
    def dfs(self, grid, x, y, val):
        if(x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0):
            return 0
        grid[x][y] = 0
        val = val + 1
        val = val + self.dfs(grid, x-1, y) + self.dfs(grid,
                                                      x+1, y) + self.dfs(grid, x, y-1) + self.dfs(grid, x, y+1)

        return val

    def maxAreaOfIsland(self, grid):
        currVal = 0
        for i in range(len(grid)):
            print(5)
        return grid


L = Solution()
print(L.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
      0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
print(L.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
