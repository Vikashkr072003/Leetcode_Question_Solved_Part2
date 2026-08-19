# 82. Remove Duplicates from Sorted List II
# Problem :---
"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

"""

# Code :---


def deleteDuplicates(head, ListNode):
    dummy = ListNode(0, head)
    prev = dummy

    current = head
    while current:
        if current.next and current.val == current.next.val:
            while current.next and current.val == current.next.val:
                current = current.next

            prev.next = current.next

        else:
            prev = prev.next

        current = current.next

    return dummy.next


head = [1, 2, 3, 3, 4, 4, 5]
print(deleteDuplicates(head))
