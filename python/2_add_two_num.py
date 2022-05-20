"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution:
def iterateSLL(SLL):
    # Helper function, I'm assuming I can't edit the data structure.
    """
    Iterates through a linked list and returns the unreversed integer.
    """
    numRev = ""
    current = SLL
    while current.next is not None:
        numRev += str(current.val)
        current = current.next
    if current.next is None:
        numRev += str(current.val)
    return int(numRev[::-1])


def addTwoNumbers(L1, L2):
    """
    Adds two linked lists, returns linked list (LeetCode question variant).
    """
    num_of_L3 = str(iterateSLL(L1) + iterateSLL(L2))[::-1]    

    head = int(num_of_L3[0])
    L3 = ListNode(head)
    current = L3
    # "This seems kind of useless...", nonono. It makes sure we're able to input two of the same ints down the line.
    ignored_head = False
    for num in num_of_L3:
        if int(num) == head and ignored_head == False:
            ignored_head = True
        else:
            newNode = ListNode(int(num))
            current.next = newNode
            current = newNode
            
    return L3
    

if __name__ == "__main__":
    testA = ListNode(5, 6)
    testB = ListNode(5, ListNode(4, ListNode(9)))

    test = addTwoNumbers(testA, testB)


"""
SUBMISSION DETAILS:
Runtime: 105 ms, faster than 34.47% of Python3 online submissions for Add Two Numbers.

Memory Usage: 13.9 MB, less than 87.11% of Python3 online submissions for Add Two Numbers.

MY NOTES:
Very fun question, I had to dig out my old freshman year notes. I'm not **super proud** of my implementation and struggled
mostly on the creation of L3 from the new number.

I am, however, very proud of my memory usage - especially it being less than 87.11% of all submissions. In school, we had a focus on 
managing memory and making sure you're not using more than you need. I *KNOW* I am using more than I need (see boolean "ignored_head"), 
which is unfortunate.

Still proud :)
"""