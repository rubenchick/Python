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


if __name__ == '__main__':
    # head_list = [1, 2, 3, 4, 5, 9, 10]
    head_list = [3, 2, 0, -4]
    head = ListToLinkedListWithCycle(head_list, 2)
    hashmap = {}

    def solution(head):
        # for i in range(0, 10):
        #     hashmap[head] = i
        #     print(head.val)
        #     head = head.next


        # root = head
        i = 0
        #
        while not (head is None):
            if head in hashmap.keys():
                print(hashmap[head])
                head = head.next
                return head

            hashmap[head] = i
            # if i == 10:
            #     return head

            i +=1
            head = head.next
        #
        # middle = int((x+1) / 2)
        # if ((x+1) % 2) != 0:
        #     middle += 1
        #
        # head = root
        # for i in range(0, middle-1):
        #     head = head.next
        # ListToLinkedListWithCycle(head, 3)

        return head


    solution(head)
    print(hashmap)
    print(head.val)
    # print("\n", (solution(head)))
    # print(ListToLinkedListWithCycle(solution(head), 3)))