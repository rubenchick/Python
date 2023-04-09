def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    s = "abc"
    t = "ahbgd"
    s = "acb"
    t = "ahbgdc"
    if len(s) == 0:
        print("True")
    if len(t) == 0:
        print("False")
    s_list = list(s)
    t_list = list(t)

    j = 0
    for i in range(len(s_list)):
        flag = False
        # if j == len(t_list):
<<<<<<< HEAD
        #     print('Fatal') ### End
=======
        #     print('Fatal')
>>>>>>> 8c0b01a (Second)
        # else:
        while flag == False:
            if s_list[i] == t_list[j]:
                # print("Inner ", s_list[i], t_list[j])
                flag = True
                j += 1
                if (j == len(t_list)) & (i != len(s_list)-1):
                    print('Fatal')
            else:
                if j == (len(t_list) - 1):
                    flag = True
                    print('Fatal')
                else:
                    j += 1
                    if (j == len (t_list)) & (i != len (s_list) - 1):
                        print ('Fatal')

    print('TRUE')
        # for j in range(len(t_list)):
        #     print(i, j)
        #     print(s_list[i], t_list[j])
