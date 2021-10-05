class Solution:
    def longestValidParentheses(self, s):
        s = list(s)
        if not s:
            return 0
        stack = [-1]
        val = 0
        for i, x in enumerate(s):
            if x == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    val = max(val, i-stack[len(stack)-1])

        return val


L = Solution()
print(L.longestValidParentheses("(()"))
print(L.longestValidParentheses(")()())"))
print(L.longestValidParentheses(""))
