# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# Input: nums = [1,2,3], target = 4
# Output: 7
#
# The possible combination ways are:
# (1, 1, 1, 1),   (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1)

nums = [1, 2, 3, 9]
target = 4

class Solution(object):
    def combinationSum4(self, nums, target):
        # remove digit more than target
        filtered = filter(lambda item: item < target, nums)
        new_nums = list(filtered)
        def reqursion(list_, target_):
            return list_

        # reqursion(new_nums, target)

        return reqursion(new_nums, target)

if __name__ == '__main__':
    result = Solution()
    print(result.combinationSum4(nums, target))