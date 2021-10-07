class Solution:
    def hasCycle(self, head):
        point1 = head
        point2 = head
        while point2 and point2.next:
            point1 = point1.next
            point2 = point2.next.next
            if point1 == point2:
                return True

        return False
