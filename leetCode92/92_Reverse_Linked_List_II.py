class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        res = curr = ListNode(0)
        link = []
        ll = head
        while ll:
            link.append(ll.val)
            ll = ll.next
        linkleft = link[:left-1]
        linkRight = link[right:]
        linkMid = link[left-1:right]
        linkMid.reverse()

        link = linkleft + linkMid + linkRight

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
print(LLPrinter(L.reverseBetween(LLMaker([1, 2, 3, 4, 5]), 2, 4)))
print(LLPrinter(L.reverseBetween(LLMaker([5]), 1, 1)))
