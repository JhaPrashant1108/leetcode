class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        res = curr = ListNode(0)
        link = []
        ls = head
        while ls:
            link.append(ls.val)
            ls = ls.next
        del link[len(link)-n]
        for i in link:
            curr.next = ListNode(i)
            curr = curr.next
        return res.next


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


L = Solution()


print(LLPrinter(L.removeNthFromEnd(LLMaker([1, 2, 3, 4, 5]), 2)))
print(LLPrinter(L.removeNthFromEnd(LLMaker([1]), 1)))
print(LLPrinter(L.removeNthFromEnd(LLMaker([1, 2]), 1)))
