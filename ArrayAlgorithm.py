class ArrayAlgorithm:

    """give a array (nums), find two numbers in this array which sum equals target"""
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    """give an array and rotate_step k, yaw right the array k step.Ex: [1,2,3] -> 1 = [3,1,2]"""
    @staticmethod
    def rotate_array(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k % len(nums) == 0:
            return

        start = 0
        i = 0
        cur = nums[i]
        counter = 0

        while counter < len(nums):
            i = (i + k) % len(nums)
            tmp = nums[i]
            nums[i] = cur
            if i == start:
                start += 1
                i += 1
                cur = nums[i]
            else:
                cur = tmp
            counter += 1

    """rotate Algorithm just for Python"""
    @staticmethod
    def rotate_array_python(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            nums[:] = nums[-k:] + nums[:-k]

    """remove the repeating elements in array"""
    @staticmethod
    def reduce_duplicate(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        number = 0
        for i in range(len(nums)):
            if nums[i] != nums[number]:
                number += 1
                nums[number] = nums[i]

        return nums[:number + 1]

    """the array includes many numbers with two times and just ONE in single, find the single number"""
    @staticmethod
    def single_number(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in nums:
            num ^= i
        return num

    """Given a non-empty array of digits representing a non-negative integer, plus one to the integer.Ex: [9,9,9] -> [1, 0, 0, 0]"""
    @staticmethod
    def plus_one(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[len(digits)-1] != 9:
            digits[len(digits)-1] += 1
        else:
            digits[len(digits)-1] += 1
            for i in range(len(digits)-1, 0, -1):
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i-1] += 1
            if digits[0] == 10:
                new_nums = [0 for i in range(len(digits)+1)]
                for i in range(len(digits)-1, 0, -1):
                    new_nums[i+1] = digits[i]
                new_nums[1] = 0
                new_nums[0] = 1
                return new_nums
        return digits

    """move a target number to the end of the array.Ex: [0,1,2,0,3,4]~key=0 -> [1,2,3,4,0,0]"""
    @staticmethod
    def move_num_to_end(nums, target):
        """
        :type target: int
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        number = 0
        for i in range(len(nums)):
            if nums[i] != target:
                nums[number] = nums[i]
                number += 1
        nums[number:] = [target for i in range(number, len(nums))]

    """You are given an n x n 2D matrix representing an image.Rotate the image by 90 degrees (clockwise)."""
    @staticmethod
    def rotate_matrix(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Flip by the main diagonal
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Flip by the y axis
        i = 0
        j = len(matrix[0])-1
        while i < j:
            for index in range(len(matrix)):
                matrix[index][i], matrix[index][j] = matrix[index][j], matrix[index][i]
            i += 1
            j -= 1