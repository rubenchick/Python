dict_ = {1:'Home', 2: "Car"}

if 1 in dict_.keys():
    print('True')
else:
    print('False')


if 'Home' in dict_.values():
    print('True')
else:
    print('False')

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic3[7] = 80
# result = dic1 + dic2
dic3.pop(7)
print(dic3)
x = dic3[5]
print(x)