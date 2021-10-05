class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        res = curr = ListNode(0)
        listl = []
        ll1 = l1
        while ll1:
            listl.append(ll1.val)
            ll1 = ll1.next
        ll2 = l2
        while ll2:
            listl.append(ll2.val)
            ll2 = ll2.next
        listl.sort()
        for i in listl:
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

print(LLPrinter(L.mergeTwoLists(LLMaker([1, 2, 4]), LLMaker([1, 3, 4]))))
print(LLPrinter(L.mergeTwoLists(LLMaker([]), LLMaker([]))))
print(LLPrinter(L.mergeTwoLists(LLMaker([]), LLMaker([0]))))
