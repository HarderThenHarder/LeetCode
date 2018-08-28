class StringAlgorithm:

    """reverse str, don't use method->s[::-1]"""
    @staticmethod
    def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        max_index = len(s) - 1
        for index, value in enumerate(s):
            res += s[max_index - index]
        return res
