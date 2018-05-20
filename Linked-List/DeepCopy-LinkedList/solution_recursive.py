# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# Dictionary which hold old nodes as keys and new nodes as its values. 
visitedDict = {}
class Solution(object):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """

    def copyRandomList(self, head):
        global visitedDict
        if head == None:
            return None
        
        # If there is value in the dictionary corresponding to the node to be copied
        # then return the respective value from the visited dictionary
        if head in visitedDict:
            return visitedDict[head]

        # create a new node
        # with the label same as old node. 
        node = RandomListNode(head.label)

        # save this value in the dictionary, this is needed since there might be dependency loops due 
        # to randomness of random pointers.
        # this would help in having a object reference saved in the dictionary already
        # which could be updated later.
        visitedDict[head] = node

        # creating a copy of next and random nodes by calling the function recursively
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        # update the new node pointer to save the updated references.
        visitedDict[head] = node
        
        return node