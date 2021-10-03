class Solution:
    def dfs(self, grid, x, y):
        if(x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0):
            return 1
        return 0

    def islandPerimeter(self, grid):
        val = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    val = val + \
                        self.dfs(grid, i-1, j) + self.dfs(grid,
                                                          i+1, j) + self.dfs(grid, i, j-1) + self.dfs(grid, i, j+1)

        return val


L = Solution()
print(L.islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(L.islandPerimeter([[1]]))
print(L.islandPerimeter([[1, 0]]))
