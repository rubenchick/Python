def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    s = "LVIII"
    # s = "III"
    s = 'MCMXCIV'
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    hashmap = {i: item for i, item in enumerate(s)}
    result = 0
    for i in range(len(hashmap)):
        if i!=(len(hashmap)-1):
            if rom_dict[hashmap[i]] < rom_dict[hashmap[i+1]]:
                result -= rom_dict[hashmap[i]]
            else:
                result += rom_dict[hashmap[i]]
        else:
            result += rom_dict[hashmap[i]]
    print(result)

