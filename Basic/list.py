# list_1 = [1, 2, 3, 4, 3, 2]
# list_2 = [11, 12, 13, 14]
# list_2.remove(11)
# print(list_2)
# result = list_1 + list_2
# result.append(99)
# result.pop()
# result.insert(2,"home")
# max value

# result = max(list_1)
# result = sum(list_1)
# print(result)

 # max value
# Write a Python program to remove duplicates from a list.
# result = list(set(list_1))
# print(result)
# p = False
# for item in list_1:
#     if item in list_2:
#         p = True
#         print('True')
#         break
# if not p:
#     print('False')

#
# list_ = [[1,2],[3,5],[7,8]]
# # print(list_[:6])
# print(False & False)
# print(True & True)
# print(False & True)

# dict_ = {0: [], 1: [], 2: []}
dict_ = {}
list_ = [[[2], 4, [9,6,[3,11]]], [5], [[[], 4], 2],77]
# list_ = [[[], 2], 4]
def get_value(list_, pos):
    for item in list_:
        if type(item) != list:
            val = dict_[pos]
            val.append(item)
            dict_[pos] = val
        else:
            get_value(item, pos)

for idx, item  in enumerate(list_):

    if type(item) == list:
        dict_[idx] = []
        for index in range(0, len(item)):
            if type(item[index]) != list:
                val = dict_[idx]
                val.append(item[index])
                dict_[idx] = val
            else:
                get_value(item[index], idx)
    else:
        dict_[idx] = [item]


print(dict_)