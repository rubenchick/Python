# Constraints:
#
#     n == nums.length
#     1 <= n <= 16
#     nums[i].length == n
#     nums[i] is either '0' or '1'.
#     All the strings of nums are unique.

if __name__ == '__main__':
    nums = ["1110", "0101", "0000", "0001"]

    text_ = ""
    def DecimalToBinary(num):
        global text_
        if num >= 1:
            DecimalToBinary(num // 2)
        if num % 2 == 0:
            tt = "0"
        else:
            tt = "1"
        # tt = f"{num % 2}"
        text_ = text_ + tt
        # text_ = text_ + f"{num % 2}"

    def findDifferentBinaryString(nums):
        global text_
        n = len(nums)
        max_n = 2 ** n

        for idx in range(max_n):
            DecimalToBinary(idx)
            if len(text_) < n:
                text_ = '0' * (n - len(text_)) + text_
            else:
                if len(text_) > n:
                    text_ = text_[1:]
            if text_ not in nums:
                return text_
            text_ = ""

        return text_


    print("\n", findDifferentBinaryString(nums))
