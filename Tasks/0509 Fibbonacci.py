
if __name__ == '__main__':
    s = "abccccdd"
    n = 4
    def solution(n):
        result = 0
        prev1 = 1
        prev2 = 0

        if n == 0:
            return result
        else:
            result = 1
            for i in range(1, n):
                result = prev1 + prev2
                prev2 = prev1
                prev1 = result
        return result


    print("\n", solution(n))

    # def fib(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0 or n == 1:
    #         return n
    #     else:
    #         return self.fib(n-1) + self.fib(n-2)