
if __name__ == '__main__':
    s = "abccccdd"
    s = "a"
    def solution(s):
        list_ = list(s)
        set_ = set(s)
        hashmap = {}
        result = 0
        extra = False
        for item in set_:
            item_count = list_.count(item)
            # if len(item_count == 1:
            odd = item_count%2
            if (odd == 1) & (extra == False):
                extra = True
            result += item_count - odd
        if extra:
            return result + 1
        else:
            return result


    print("\n", solution(s))