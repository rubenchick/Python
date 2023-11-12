import re
import operator as op
# aa = 0 ==> 1
# a = 2 ==> 3
if __name__ == '__main__':
    s = "abbcccaa"

    def countHomogenous(s):
        x = 0
        # find_all_Homogenous
        current_ss = ""
        last_char = s[0]
        ss_set = set()
        # деление string на подстроки
        for substring in s:
            if substring == last_char:
                current_ss = current_ss + substring
                ss_set.add(current_ss)
            else:
                last_char = substring
                ss_set.add(current_ss)
                current_ss = substring
                ss_set.add(current_ss)

        ss_set.add(current_ss)
        def count_ss(text_):
            number_ = 0
            number_chars = len(text_)
            for idx in range(len(s)-len(text_)+1):
                if s[idx] == text_[0]:
                    is_contradiction = 0
                    current_char = 1
                    while (not is_contradiction) and (current_char < number_chars):
                        if s[idx+current_char] != text_[current_char]:
                            is_contradiction = 1
                        else:
                            current_char += 1
                    if not is_contradiction:
                        number_ += 1
            print(text_, number_)
            return number_


        count_ = 0
        for item in ss_set:
            count_ += count_ss(item)

        return count_


    print("\n", countHomogenous(s))
