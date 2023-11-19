import re
import operator as op
# aa = 0 ==> 1
# a = 2 ==> 3
if __name__ == '__main__':
    s = "aabca"

    def countPalindromicSubsequence(s):
        result = set()
        for idx in range(len(s)-2):
            # print(idx, s[idx])
            # print("---------")
            pos = len(s)-1
            while pos > idx:
                # print(pos, s[pos])
                if s[pos] == s[idx]: # first and last letter were found
                    middle = idx + 1
                    letters_list = []
                    while middle < pos:
                        if s[middle] not in letters_list:
                            letters_list.append(s[middle])
                            # print("result", s[idx] + s[middle] + s[pos])
                            result.add(s[idx] + s[middle] + s[pos])
                        # print(middle, "- middle")
                        middle += 1
                pos -= 1
        return len(result)


    print("\n", countPalindromicSubsequence(s))