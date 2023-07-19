def find_duplicate(nums):
    if (not nums or
            not any(isinstance(num, int) for num in nums) or
            len(nums) < 2 or
            min(nums) < 1):
        return False

    nums.sort()

    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1]:
            return nums[index]

    return False
