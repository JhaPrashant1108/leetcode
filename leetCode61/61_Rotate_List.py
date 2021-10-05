class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        res = curr = ListNode(0)
        link = []
        ll = head
        while ll:
            link.append(ll.val)
            ll = ll.next
        if len(link) == 0:
            return res.next
        if k != 0:
            k = k % len(link)
            link = link[-k:] + link[:-k]
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

print(LLPrinter(L.rotateRight(LLMaker([1, 2, 3, 4, 5]), 2)))
print(LLPrinter(L.rotateRight(LLMaker([0, 1, 2]), 4)))
