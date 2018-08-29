class StringAlgorithm:

    """reverse str, don't use method->s[::-1]"""
    @staticmethod
    def reverse_string(s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        max_index = len(s) - 1
        for index, value in enumerate(s):
            res += s[max_index - index]
        return res

    """reverse int: 123 -> 321; -123 -> -321"""
    @staticmethod
    def reverse_num(x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        while x != 0:
            print(res)
            if abs(res) > (2 ** 31 - 1) / 10:
                return 0
            if x > 0:
                res = res * 10 + x % 10
                x //= 10
            elif x < 0:
                if x % 10 != 0:
                    res = res * 10 - (10 - x % 10)
                    x = x // 10 + 1
                else:
                    res = res * 10
                    x = x // 10
        return res
