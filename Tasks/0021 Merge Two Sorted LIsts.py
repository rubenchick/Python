class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToLinkedList(list_):
    if len(list_) == 0:
        return None
    else:
        root_note = ListNode(list_[0])
        prev_node = root_note
        for i in range(1, len(list_)):
            new_note = ListNode(list_[i])
            prev_node.next = new_note
            prev_node = new_note
    return root_note

def LinkedListToList(root_note):
    if root_note is None:
        return []
    else:
        list_ = []
        list_.append(root_note.val)
        note = root_note.next

        while not (note is None):
            list_.append(note.val)
            note = note.next
    return list_



if __name__ == '__main__':
    list1 = [1, 2, 4]
    list1 = [1, 5, 7, 9]
    root_node1 = ListToLinkedList(list1)
    print(LinkedListToList(root_node1))




    # list2 = [1, 3, 4]
    # list1 = None
    # list2 = ListNode(88)
    # list1.next = list2
    # print(list1)
    # if list1 is None:
    #     print("None")
    # print(list1.val)
    # print(list1.next)
    # print(list2)
    # print(type(list1))
    # print("Yes")





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
