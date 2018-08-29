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

    """Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1."""
    @staticmethod
    def first_uniq_char(s):
        """
        :type s: str
        :rtype: int
        """
        reduce = {}
        for i in range(len(s)):
            if s[i] not in reduce:
                reduce[s[i]] = 1
            else:
                reduce[s[i]] += 1

        print(reduce)
        for i in range(len(s)):
            if reduce[s[i]] == 1:
                return i
        return -1
