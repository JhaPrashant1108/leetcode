class Solution(object):
    def calculateMinimumHP(self, dungeon):
        r, c = len(dungeon), len(dungeon[0])

        for i in range(r - 1):
            dungeon[i].append(float('inf'))
        dungeon.append([float('inf') for _ in range(c + 1)])

        dungeon[r - 1].append(1)

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                dungeon[i][j] = max(1, -dungeon[i][j] +
                                    min(dungeon[i+1][j], dungeon[i][j+1]))

        return dungeon[0][0]


L = Solution()
print(L.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
print(L.calculateMinimumHP([[0]]))
