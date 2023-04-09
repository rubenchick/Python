def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # s = "egg"
    # t = "add"
    # s = "foo"
    # t = "bar"
    # s = "paper"
    # t = "title"
    # s = "bbbaaaba"
    # t = "aaabbbba"
    s = "badc"
    t = "baba"
    print(set(zip(s, t)))

    hashmap = {}
    # print(hashmap)
    for i, j in zip(s, t):
        if i in hashmap:
            if hashmap[i] != j:
                print("False")
        else:
            hashmap[i] = j
    if len(hashmap) == len(set(t)):
        print('True')
    else:
        print("False")





    #
    # if len(hashmap) == len(set(t)):
    #     print('True')
    # else:
    #     print("False")
