import math
if __name__ == '__main__':
    # prices = [7, 4, 5, 2, 6, 1]
    prices = [7, 6, 4, 3, 1]
    # prices = [2, 7, 1, 4]
    # prices = [7, 2, 4, 1]
    prices = [2, 1, 2, 1, 0, 0, 1]
    # prices = [6, 7, 4, 5, 2, 6, 1]
    prices = [1, 2]
    def solution(prices):
        if len(prices) == 1:
            return 0

        current = prices[0]
        max_price = max(prices[1:len(prices)])
        max_ = max_price
        result = [0]
        flag = False
        if max_price > current:
            result.append(max_price - current)

        pos = 1
        while pos < len(prices) - 1:
            current = prices[pos]
            if current < prices[pos + 1]:
                if flag:
                    max_price = max(prices[pos + 1:len(prices)])
                    flag = False
                result.append(max_price - current)
            if current == max_price:
                flag = True
            pos += 1
        return max(result)





    print("\n", solution(prices))
