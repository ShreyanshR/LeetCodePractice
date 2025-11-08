from typing import List
from functools import cmp_to_key

def finding_largest_number(list_of_numbers: List[int]) -> str:
    """
    Find the largest number that can be formed by arranging the given numbers.
    
    Args:
        list_of_numbers: List of integers to arrange
        
    Returns:
        String representation of the largest possible number
    """
    if not list_of_numbers:
        return "0"
    
    # Convert all numbers to strings for string concatenation comparison
    nums = [str(num) for num in list_of_numbers]

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a  + b < b + a:
            return 1
        else:
            return 0

    nums.sort(key=cmp_to_key(compare))

    result = ''.join(nums)

    return int(result)


if __name__ == "__main__":
    nums = [4, 56, 6, 3]
    n1 = [91, 62, 7, 12, 3999, 913]

    print(finding_largest_number(nums))
    print(finding_largest_number(n1))





    




