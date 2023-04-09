def print_hi(name):
    print (f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    nums = [1, 2, 3, 4, 5]
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [2, -1, 1]
    # nums = [-1, -1, 0, 1, 1, 0]
    # nums = [-1, -1, 1, 1, 0, 0]
    # nums = [-1, 1, -1, -1, 0, 1]
    nums = [2, 5]
    nums.append(0)
    nums.insert(0, 0)

    i = 1
    flag = False
    index = 0
    left_sum = sum(nums[0:i])
    right_sum = sum(nums[i+1:len(nums)])
    print(left_sum, right_sum)  # correct
    if left_sum == right_sum:
        index = 0
    else:
        while not flag:
            i += 1
            left_sum += nums[i-1]
            right_sum -= nums[i]
            # print("i=", i, " ; value=", nums[i-1], ' ;Left sum =', left_sum, ' ;Right sum=', right_sum)
            if i == len(nums)-2:
                index = -1
                flag = True
            if left_sum == right_sum:
                index = i-1
                flag = True






    # if (right_sum+nums[1]) == 0:
    #     index = 0
    # else:
    #     if left_sum == right_sum:
    #         index = 1
    #     else:
    #         while not flag:
    #             i += 1
    #             left_sum += nums[i-1]
    #             right_sum -= nums[i]
    #             # print("i=", i, " ; value=", nums[i-1], ' ;Left sum =', left_sum, ' ;Right sum=', right_sum)
    #             if i == len(nums)-2:
    #                 index = -1
    #                 flag = True
    #             if left_sum == right_sum:
    #                 index = i-1
    #                 flag = True
    #         if index == 1:
    #             if (right_sum + nums[0] + nums[1] - nums[len(nums)-1]) == 0:
    #                 index = len(nums)-1
    #

    print("index=", index)



    # list2 = [sum(list1[0:i]) for i in range(1, len(list1)+1)]
    # list2 = []
    # for i in range(0, len(list1)-1):
    #     if i != 0:
    #         list2.append(list1[i]+list2[i-1])
    #     else:
    #         list2.append(list1[i])

    # print(list1)
    # print(list2)


## 734/746 done
# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 1
#         flag = False
#         index = 1
#         left_sum = sum(nums[0:i])
#         right_sum = sum(nums[i+1:len(nums)])
#         if (right_sum+nums[1]) == 0:
#             index = 0
#         else:
#             if left_sum == right_sum:
#                 index = 1
#             else:
#                 while not flag:
#                     i += 1
#                     left_sum += nums[i-1]
#                     right_sum -= nums[i]
#                     if i == len(nums)-1:
#                         index = -1
#                         flag = True
#                     if left_sum == right_sum:
#                         index = i
#                         flag = True
#                 if index == 1:
#                     if (right_sum + nums[0] + nums[1] - nums[len(nums)-1]) == 0:
#                         index = len(nums)-1
#         return index