if __name__ == '__main__':
    s = "lEetcOde"
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def sortVowels(s):
        vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowel_letters = []
        # создаем list с vowel
        s_list = list(s)

        for item in s_list:
            if item in vowel_list:
                print(ord(item), item)
                vowel_letters.append(item)

        vowel_letters_sorted = sorted(vowel_letters, key=lambda code: ord(code))

        pos = 0
        result_ = []
        for idx in range(len(s_list)):
            if s_list[idx] in vowel_list:
                result_.append(vowel_letters_sorted[pos])
                pos += 1
            else:
                result_.append(s_list[idx])
        return ''.join(result_)


    print("\n", sortVowels(s))