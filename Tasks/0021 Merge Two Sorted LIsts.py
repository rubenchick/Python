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
    list1 = [1, 2, 4, 4]
    list2 = [1, 1, 3, 4]
    # list1 = [2]
    # list2 = [1]
    root_node1 = ListToLinkedList(list1)
    root_node2 = ListToLinkedList(list2)
    print(LinkedListToList(root_node1))

    if root_node1 is None:
        print(LinkedListToList(root_node2))
        # return root_node2
    if root_node2 is None:
        print(LinkedListToList(root_node1))
        # return root_node1
    if root_node1.val <= root_node2.val:
        root = root_node1
        node1 = root_node1
        node2 = root_node2
    else:
        root = root_node2
        node1 = root_node2
        node2 = root_node1

    prev_node = node1

    while not (node1 is None):
        if node1.val <= node2.val:
            prev_node = node1
            node1 = node1.next
        else:
            new_node = ListNode(node2.val)
            new_node.next = node1
            prev_node.next = new_node
            prev_node = new_node
            node2 = node2.next
            # if node2 is None:
            #     return root_node1

    if not (node2 is None):
        prev_node.next = node2


    print(LinkedListToList(root))
    # return root_node1





    # flag = False
    # i = 0
    # j = 0
    # if len(list1) == 0:
    #     print(list2)
    # if len(list2) == 0:
    #     print(list1)
    #
    # while flag == False:
    #     if list1[i] <= list2[j]:
    #         i += 1
    #     else:
    #         list1.insert(i, list2[j])
    #         j += 1
    #         i += 1
    #
    #     if i == len(list1):
    #         flag = True
    #
    # list1 += list2[j:len(list2)]
    # print(list1)
