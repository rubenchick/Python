# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# Input: nums = [1,2,3], target = 4
# Output: 7
#
# The possible combination ways are:
# (1, 1, 1, 1),   (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1)

nums = [10, 20, 30, 90]
target = 40

class Solution(object):
    def combinationSum4(self, nums, target):
        # remove digit more than target
        filtered = filter(lambda item: item < target, nums)
        new_nums = list(filtered)
        def reqursion(idx, current_list, pos):
            print(pos, len(new_nums))
            while pos < len(new_nums):
                print(pos)
                reqursion(idx, current_list, pos + 1)

            return

            #
            #
            # current_list.append(new_nums[pos])
            # if sum(current_list)> target:
            #     return
            # else:
            #     if sum(current_list) == target:
            #         print(current_list)
            #         return
            #     else:
            #         reqursion(idx, current_list, pos)
            #         # reqursion(idx, current_list, pos+1)





            # current_list.append(new_nums[pos])
            # if sum(current_list) > target:
            #     return
            # else:
            #     if sum(current_list) == target:
            #         print(current_list)
            #         return
            #     else:
            #         reqursion(idx, current_list, pos+1)

        for idx in range(len(new_nums)):
            current_list = [new_nums[idx]]
            pos = 0
            reqursion(idx, current_list, pos)

        return 99

if __name__ == '__main__':
    result = Solution()
    print(result.combinationSum4(nums, target))