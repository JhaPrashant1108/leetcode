class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        val = [0 for _ in range(len(text2) + 1)]

        for i in text1:
            currVal = [0]
            for j, k in enumerate(text2):
                if i == k:
                    currVal.append(1 + val[j])
                else:
                    currVal.append(max(currVal[-1], val[j + 1]))
            val = currVal

        return val[-1]


L = Solution()
print(L.longestCommonSubsequence(text1="abcde", text2="ace"))
print(L.longestCommonSubsequence(text1="abc", text2="abc"))
print(L.longestCommonSubsequence(text1="abce", text2="def"))
print(L.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))
print(L.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
