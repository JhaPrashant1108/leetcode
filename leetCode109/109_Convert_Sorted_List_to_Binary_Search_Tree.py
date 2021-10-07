class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructTreefromList(self, nums, left, right):
        if left > right:
            return
        mid = (int)(left + (right - left)/2)
        node = TreeNode(nums[mid])
        node.left = self.constructTreefromList(nums, left, mid-1)
        node.right = self.constructTreefromList(nums, mid+1, right)

        return node

    def sortedListToBST(self, head):
        link = []
        ll = head
        while ll:
            link.append(ll.val)
            ll = ll.next
        if not link:
            return
        return self.constructTreefromList(link, 0, len(link)-1)


def LLMaker(link):
    res = curr = ListNode(0)
    for i in link:
        curr.next = ListNode(i)
        curr = curr.next
    return res.next


def LLPrinter(head):
    ls = head
    link = []
    while ls:
        link.append(ls.val)
        ls = ls.next
    return link


def flatten(root):
    if (root == None or root.left == None and
            root.right == None):
        return
    if (root.left != None):
        flatten(root.left)
        tmpRight = root.right
        root.right = root.left
        root.left = None
        t = root.right
        while (t.right != None):
            t = t.right
        t.right = tmpRight
    flatten(root.right)


L = Solution()
print(L.sortedListToBST(LLMaker([-10, -3, 0, 5, 9])))
print(L.sortedListToBST(LLMaker([])))
print(L.sortedListToBST(LLMaker([0])))
print(L.sortedListToBST(LLMaker([1, 3])))
