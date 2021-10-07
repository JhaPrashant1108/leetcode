class Solution:
    def exist(self, board, word):
        m, n, p = len(board), len(board[0]), len(word)

        def finder(r, c, pos):
            if pos >= p:
                return True
            elif 0 <= r < m and 0 <= c < n and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = '*'
                if finder(r-1, c, pos+1) or finder(r+1, c, pos+1) or finder(r, c-1, pos+1) or finder(r, c+1, pos+1):
                    return True
                board[r][c] = temp
            return False

        for i in range(m):
            for j in range(n):
                if finder(i, j, 0):
                    return True

        return False


L = Solution()
print(L.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
print(L.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(L.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
