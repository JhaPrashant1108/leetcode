class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        res = curr = ListNode(0)
        link = []
        ll = head
        while ll:
            link.append(ll.val)
            ll = ll.next
        dupList = []
        valList = []
        for i in link:
            if i in valList:
                valList.remove(i)
                dupList.append(i)
            elif i in dupList:
                continue
            else:
                valList.append(i)

        for i in valList:
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

print(LLPrinter(L.deleteDuplicates(LLMaker([1, 2, 3, 3, 4, 4, 5]))))
print(LLPrinter(L.deleteDuplicates(LLMaker([1, 1, 1, 2, 3]))))
