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
    head_list = [1, 2, 3, 4, 5]
    head = ListToLinkedList(head_list)

    def solution(head):
        second = None
        while not (head is None):
            prev = head
            head = head.next
            prev.next = second
            second = prev

        return prev
    # root.next = None

    print(LinkedListToList(solution(head)))

    # root_node1 = ListToLinkedList(list1)
    # root_node2 = ListToLinkedList(list2)
    # print(LinkedListToList(root_node1))
    #
    # if root_node1 is None:
    #     print(LinkedListToList(root_node2))
    #     # return root_node2