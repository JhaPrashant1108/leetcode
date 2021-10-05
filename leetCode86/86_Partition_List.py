class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        res = curr = ListNode(0)
        link = []
        ll = head
        while ll:
            link.append(ll.val)
            ll = ll.next
        l1 = []
        l2 = []
        for i in link:
            if i < x:
                l1.append(i)
            else:
                l2.append(i)
        link = l1 + l2
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

print(LLPrinter(L.partition(LLMaker([1, 4, 3, 2, 5, 2]), 3)))
print(LLPrinter(L.partition(LLMaker([2, 1]), 2)))
