class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        res = n = ListNode(0)
        while l1 or l2 or temp:
            if l1: 
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next 
            temp, val = divmod(v1+v2+temp,10)
            n.next = ListNode(val)
            n=n.next
        return res.next


# divmod() with Floats
print('divmod(8.0, 3) = ', divmod(8.0, 3))

#divmod(8, 3) =  (2, 2)