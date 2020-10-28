class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        return 5







L = Solution()
print(L.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]))
print(L.findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log"]))

#testCase = int(input())

# for i in range(testCase):
#     N,M = map(int,input().split())
#     output = []
#     for j in range(N):
#         minDisc = 1
#         index = -1
#         for k in range(M):
#             a,b,c = map(int, input().split())
#             if (1-0.01*a)*(1-0.01*b)*(1-0.01*c)<=minDisc:
#                 minDisc = (1-0.01*a)*(1-0.01*b)*(1-0.01*c)
#                 index = k+1
#         output.append(index)
#     print(output)

