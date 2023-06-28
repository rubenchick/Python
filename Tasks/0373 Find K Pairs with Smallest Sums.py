def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # nums1 = [1, 7, 11]
    # nums2 = [1, 4, 6, 9]
    # k = 3
    # [1,1] [1,4] [1,6] [7,1] [11,1] [7,4] [7,6] [11,4] [7,9] [11,6] [11,9]
    nums1 = [1,2,4]
    nums2 = [-1,1,2]
    k = 100

    def kSmallestPairs(nums1, nums2, k):
        i = 0
        j = 0

        i0 = 0
        j0 = 0
        i_last = 0
        j_last = 0
        result = []
        sum = nums1[i] + nums2[j]
        result.append([nums1[i], nums2[j]])
        n = 1
        last = False

        while n<k:
            # print(n,i,j,i_last,j_last, result[-1])
            if (i0 == len(nums1) - 1) & (j0 == len(nums2) - 1):
                if last != True:
                    result.append([nums1[i0], nums2[j0]])
                    last= True
            elif j==len(nums2) - 1:
                i0 += 1
                j = j0
                if (nums1[i] + nums2[j] >= sum) & (i != i_last | j != j_last):
                    result.append([nums1[i], nums2[j]])
                    i_last = i
                    j_last = j
                    sum = nums1[i] + nums2[j]
                else:
                    n -= 1
            elif i==len(nums1) - 1:
                j0 += 1
                i = i0
                print (n, i, j, i_last, j_last, result[-1])
                if (nums1[i] + nums2[j] >= sum) & (i != i_last | j != j_last):
                    result.append([nums1[i], nums2[j]])
                    i_last = i
                    j_last = j
                    sum = nums1[i] + nums2[j]
                else:
                    n -= 1
            elif nums1[i+1] + nums2[j0] > nums1[i0] + nums2[j+1]:
                j += 1
                result.append([nums1[i0], nums2[j]])
                i_last = i0
                j_last = j
                sum = nums1[i0] + nums2[j]
            else:
                i += 1
                result.append([nums1[i], nums2[j0]])
                i_last = i
                j_last = j0
                sum = nums1[i] + nums2[j0]
            n += 1
        return result


    print("\n", kSmallestPairs(nums1, nums2, k))
