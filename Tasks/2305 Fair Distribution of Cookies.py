def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cookies = [2, 4, 6, 8]
    k = 2
    def Solution(cookies, k):
        result = []
        dict_ = {}
        def all_dataset(list_prev, list_,k):
            for index in range(0, len(list_)):
                temp = list_.copy()
                temp.remove(list_[index])
                rest_cookies = temp
                if len(list_prev) != 0:
                    result.append([[list_prev, list_[index]], rest_cookies])
                else:
                    result.append([list_[index], rest_cookies])
                if len(rest_cookies) >= k:
                    if len(list_prev) != 0:
                        all_dataset([list_prev, list_[index]], rest_cookies, k)
                    else:
                        all_dataset([list_[index]], rest_cookies, k)

        all_dataset([], cookies, k)
        # for item in result:
        #     print(item[0])

        def get_value(list_, pos):
            for item in list_:
                if type (item) != list:
                    val = dict_[pos]
                    val.append (item)
                    dict_[pos] = val
                else:
                    get_value (item, pos)

        for tt in result:
            print(tt[0])

        for idx, item in enumerate(result):

            if type(item[0]) == list:
                dict_[idx] = []
                for index in range (0, len (item[0])):
                    if type (item[index]) != list:
                        val = dict_[idx]
                        val.append (item[index])
                        dict_[idx] = val
                    else:
                        get_value (item[index], idx)
            else:
                dict_[idx] = [item[0]]

        return dict_

    print("\n", Solution(cookies, k))

