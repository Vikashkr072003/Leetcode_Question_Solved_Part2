# Questions :-- 61. Rotate List
# Problem :- Given the head of a linked list, rotate the list to the right by k places.
"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

"""

# Code :---


def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    n = 1
    tail = head

    while tail.next:
        n += 1
        tail = tail.next

    k = k % n
    if k == 0:
        return head

    tail.next = head

    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
