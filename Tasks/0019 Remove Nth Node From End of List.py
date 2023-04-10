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
    head_list = [1, 2, 3, 4, 5, 9]
    head_list = [1, 2]
    n = 2
    head = ListToLinkedList(head_list)

    def solution(head, n):
        root = head
        x = 0

        while not (head is None):
            x +=1
            head = head.next

        if x == 1:
            return None

        if x == n:
            return root.next

        head = root
        for i in range(0, x-n-1):
            print("Before ", i, head.val)
            head = head.next
            print("After ", i, head.val)

        head.next = head.next.next

        return root


    # print("\n",(solution(head, 2)))
    print(LinkedListToList(solution(head, n)))