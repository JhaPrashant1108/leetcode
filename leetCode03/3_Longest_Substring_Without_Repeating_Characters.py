class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        s = list(s)
        res = ""
        length = []
        for i in s:
            if i not in res:
                res = res+i
                length.append(len(res))
            else:
                length.append(len(res))
                res = res[res.find(i)+1:]
                res = res+i
        length.sort(reverse=True)
        return length[0]


        







l = Solution()
print(l.lengthOfLongestSubstring("abcabcbb"))
print(l.lengthOfLongestSubstring("bbbbb"))
print(l.lengthOfLongestSubstring("pwwkew"))
print(l.lengthOfLongestSubstring("au"))