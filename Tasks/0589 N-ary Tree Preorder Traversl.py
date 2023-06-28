import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def ListToLinkedList(list_):
    if len(list_) == 0:
        return None
    else:
        root_node = ListNode(list_[0])
        prev_node = root_node
        for i in range(1, len(list_)):
            new_note = ListNode(list_[i])
            prev_node.next = new_note
            prev_node = new_note
    return root_node


def LinkedListToList(root_node):
    if root_node is None:
        return []
    else:
        list_ = []
        list_.append(root_node.val)
        node = root_node.next

        while not (node is None):
            list_.append(node.val)
            node = node.next
    return list_

def ListToLinkedListWithCycle(list_, pos):
    if len(list_) == 0:
        return None
    else:
        root_node = ListNode(list_[0])
        prev_node = root_node
        cycle_start = root_node
        for i in range(1, len(list_)):
            new_note = ListNode(list_[i])
            prev_node.next = new_note
            prev_node = new_note
            if i == pos:
                cycle_start = new_note

    if pos != -1:
        new_note.next = cycle_start

    return root_node
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    print("Yes")
    print (f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
    # head_list = [3, 2, 0, -4]
    # head = ListToLinkedListWithCycle(head_list, 2)
    # hashmap = {}
    #
    # def solution(head):
    #
    #     while not (head is None):
    #         if head in hashmap.keys():
    #             print(hashmap[head])
    #             head = head.next
    #             return head
    #
    #         hashmap[head] = i
    #
    #
    #     return head
    #
    #
    # solution(head)