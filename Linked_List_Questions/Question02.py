# Questions :-19. Remove Nth Node From End of List
# Problem :---
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

# Code :----


def removeNthFromEnd(head, listNode, n):
    dummy = listNode(0, head)
    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


head = [1, 2, 3, 4, 5]
n = 2
print(removeNthFromEnd(head, n))
