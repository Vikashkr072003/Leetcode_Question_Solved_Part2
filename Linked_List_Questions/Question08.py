# 2. Add Two Numbers
"""
Problem :---

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example :---
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807


"""

# Code :----


def addTwoNumber(self, l1, ListNode, l2):
    return self.addWithCarry(l1, l2, 0)


def addWithCarry(self, l1, l2, carry, ListNode):
    if not l1 and not l2 and carry == 0:
        return None

    total = carry
    if l1:
        total += l1.val
    if l2:
        total += l2.val

    node = ListNode(total % 10)
    node.next = self.addWithCarry(
        l1.next if l1 else None, l2.next if l2 else None, total // 10
    )
    return node
