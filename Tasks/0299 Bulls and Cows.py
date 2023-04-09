def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    secret = "1807"
    guess = "7810"
    secret = "1123"
    guess = "0111"
    secret = list(secret)
    guess = list(guess)
    bow = 0
    cow = 0
    hashmap = {}
    # for i in range(len(guess)):
    flag = False
    i = 0
    while flag == False:
        if guess[i] == secret[i]:
            bow += 1
            guess.pop(i)
            secret.pop(i)
            i -= 1

        if i == len(secret)-1:
            flag = True
        i += 1

    flag = False
    i = 0
    # print(secret.index('7'))
    while flag == False:
        if guess[i] in secret:
            cow += 1
            secret.pop(secret.index(guess[i]))
            guess.pop(i)
            i -= 1

        if i == len(secret) - 1:
            flag = True
        i += 1
    rrr = "{}A{}B".format(bow, cow)
    print(rrr)
    print("Bow :", bow)
    print("Cow :", cow)
