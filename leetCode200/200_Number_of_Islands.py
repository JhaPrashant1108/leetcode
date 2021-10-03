class Solution:
    def dfs(self, grid, x, y):
        if(x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return
        if(grid[x][y] != "1"):
            return
        grid[x][y] = "0"
        self.dfs(grid, x-1, y)
        self.dfs(grid, x+1, y)
        self.dfs(grid, x, y-1)
        self.dfs(grid, x, y+1)

    def numIslands(self, grid) -> int:
        if not grid:
            return
        val = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == "1"):
                    val = val+1
                    self.dfs(grid, i, j)

        return val


L = Solution()

# print(L.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
#       "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
# print(L.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], [
#       "0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
print(L.numIslands([["1"]]))
