class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        stack = []
        val = []
        if root == None:
            return val
        curr = root
        while curr or stack != []:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            val.append(curr.val)
            curr = curr.right

        return val


def TreeMaker(arr, root, i):
    if i < len(arr):
        temp = TreeNode(arr[i])
        root = temp
        root.left = TreeMaker(arr, root.left,
                              2 * i + 1)
        root.right = TreeMaker(arr, root.right,
                               2 * i + 2)
    return root


L = Solution()


print(L.inorderTraversal(TreeMaker([1, None, 2, 3], None, 0)))
print(L.inorderTraversal(TreeMaker([], None, 0)))
print(L.inorderTraversal(TreeMaker([1], None, 0)))
print(L.inorderTraversal(TreeMaker([1, 2], None, 0)))
print(L.inorderTraversal(TreeMaker([1, None, 2], None, 0)))
