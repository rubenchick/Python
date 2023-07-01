def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums1 = [-13,23,44,117,900,990]
    nums2 = [-15,20,35,118,223,500,663,717,789,813]
    k = 10

    def kSmallestPairs(nums1, nums2, k):
        def sort_list(list_):
            list_len = len(list_)
            index = 1
            while index < (list_len):
                if (list_[index][0] + list_[index][1]) < (list_[index - 1][0] + list_[index - 1][1]):
                    wrong_position = list_[index]
                    list_.pop(index)
                    i = index - 1
                    flag_exit = False
                    while not flag_exit:
                        if (list_[i][0] + list_[i][1]) <= (wrong_position[0] + wrong_position[1]):
                            list_.insert(i + 1, wrong_position)
                            flag_exit = True
                        else:
                            i -= 1
                index += 1
            return list_

        i = 0
        j = 0

        i0 = 0
        j0 = 0
        result = []
        sum = nums1[i] + nums2[j]
        result.append([nums1[i], nums2[j]])
        filled_list = [[i,j]]
        n = 1
        last = False
        is_print = False
        ## add last condition
        while ((n<(k*2)) == True) & (last == False) :
        # while n < (k * 2):
            if is_print: print(n,i,j,i0,j0,result[-1])
            if (i0 == len(nums1) - 1) & (j0 == len(nums2) - 1):
                if last != True:
                    if is_print: print("1::1", n)
                    if [i0, j0] not in filled_list:
                        result.append([nums1[i0], nums2[j0]])
                        filled_list.append([i0, j0])
                    last= True
            elif j==len(nums2) - 1:
                if j == j0:
                    if i0 != len(nums1) - 1:
                        i0 += 1
                        if [i0,j0] in filled_list:
                            n -= 1
                        else:
                            if is_print: print("2::2", n)
                            result.append([nums1[i0], nums2[j0]])
                            filled_list.append([i0, j0])
                            if (i0 == len(nums1) - 1) & (j0 == len(nums2) - 1):
                                last = True
                            sum = nums1[i0] + nums2[j]
                else:
                    if i0 != len (nums1) - 1:
                        i0 += 1
                        j = j0
                        if (nums1[i] + nums2[j] >= sum): ## & (i != i_last | j != j_last):
                            if [i, j] in filled_list:
                                n -= 1
                            else:
                                if is_print: print ("2::2+", n)
                                result.append([nums1[i], nums2[j]])
                                filled_list.append([i, j])
                                sum = nums1[i] + nums2[j]
                        else:
                            n -= 1
            elif i==len(nums1) - 1:
                if i == i0:
                    if j0 != len (nums2) - 1:
                        j0 += 1
                        if [i, j0] in filled_list:
                            n -= 1
                        else:
                            if is_print: print("3::3", n)
                            result.append([nums1[i], nums2[j0]])
                            filled_list.append([i, j0])
                            sum = nums1[i] + nums2[j0]
                else:
                    if j0 != len(nums2) - 1:
                        j0 += 1
                        i = i0
                        if (nums1[i] + nums2[j] >= sum): ## & (i != i_last | j != j_last):
                            if [i, j] in filled_list:
                                n -= 1
                            else:
                                if is_print: print("3::3", n)
                                result.append([nums1[i], nums2[j]])
                                filled_list.append([i, j])
                                sum = nums1[i] + nums2[j]
                        else:
                            n -= 1
            elif nums1[i+1] + nums2[j0] > nums1[i0] + nums2[j+1]:
                j += 1
                if is_print: print("4::4", n)
                result.append([nums1[i0], nums2[j]])
                filled_list.append([i0, j])
                sum = nums1[i0] + nums2[j]
            else:
                i += 1
                if is_print: print("5::5", n)
                result.append([nums1[i], nums2[j0]])
                filled_list.append([i,j0])
                sum = nums1[i] + nums2[j0]
            n += 1

        return sort_list(result)[:k]


    print("\n", kSmallestPairs(nums1, nums2, k))