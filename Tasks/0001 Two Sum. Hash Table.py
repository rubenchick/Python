def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    nums = [2, 7, 11, 15]
    target = 9
    i = 0
    flag = False
    second = 0
    while not flag:
        try:
            second = nums.index(target - nums[i])
            print('Found :', i, second, nums[i], nums[second])
        except:
            print('Sorry')

        if (second!=0) & (second!=i):
            flag = True

        if i == len(nums) - 1:
            flag = True

        i += 1

    print(i-1, second)


# Right solutuon with hashmap
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [i, hashmap[complement]]
#             hashmap[nums[i]] = i

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]
