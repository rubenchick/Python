import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


if __name__ == '__main__':
    head_list = [1, 2, 3, 4, 5, 9, 10]
    # head_list = [1,2,3,4,5,6]
    head = ListToLinkedList(head_list)

    def solution(head):
        root = head
        x = 0

        while not (head is None):
            x +=1
            head = head.next

        middle = int((x+1) / 2)
        if ((x+1) % 2) != 0:
            middle += 1

        head = root
        for i in range(0, middle-1):
            head = head.next

        return head


    # print("\n", (solution(head)))
    print(LinkedListToList(solution(head)))