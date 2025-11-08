from typing import List

def missing_number(nums: List[int]) -> int:
    missing = 0

    #we can't do len(nums)+ 1, bcoz it will give index out of bounds if it's the end

    if nums[0] != 1:
        return 1

    for i in range(len(nums) - 1):
        print(f'i, num, num1: {i, nums[i], nums[i+1]}')
        if nums[i+1] != nums[i] + 1:
            return nums[i] + 1
    
    return nums[-1] + 1

def missing_number_with_sum(nums: List[int]) -> int:
    end = nums[-1]
    start = nums[0]
    expected_sum = (end - start + 1) * (end + start)/2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [2, 3, 4, 5, 6]

    print(missing_number(nums))
    print(missing_number_with_sum(nums))