from collections import Counter

if __name__ == '__main__':
    nums = [5, 5, 5, 3, 3, 1, 1]
    def reductionOperations(nums):
        count = 0
        nums = sorted(nums)
        num_dict = dict(Counter(nums))
        pos_list = [idx for idx in range(len(num_dict))]

        for idx, value in enumerate(num_dict.values()):
            count += value*pos_list[idx]

        return count

    print("\n", reductionOperations(nums))
