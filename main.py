from ArrayAlgorithm import ArrayAlgorithm


def main():
    def firstUniqChar(s):
        reduce = {}
        for i in range(len(s)):
            if s[i] not in reduce:
                reduce[s[i]] = 1
            else:
                reduce[s[i]] += 1

        for index, element in enumerate(reduce):
            if reduce[element] == 1:
                return index
        return -1

    res = firstUniqChar("aababcas")


if __name__ == '__main__':
    main()
