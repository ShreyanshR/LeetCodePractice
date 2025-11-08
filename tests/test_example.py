"""
Example test file demonstrating the testing framework.

This shows how to structure your tests for coding interview practice.
"""

import pytest


@pytest.mark.easy
@pytest.mark.array
class TestTwoSum:
    """Example: Two Sum problem tests."""
    
    def test_basic_case(self):
        """Test basic two sum case."""
        # TODO: Implement solution and uncomment
        # from solutions.two_sum import two_sum
        # assert two_sum([2, 7, 11, 15], 9) == [0, 1]
        pass
    
    def test_edge_case_empty(self):
        """Test empty array."""
        # TODO: Implement
        pass
    
    def test_no_solution(self):
        """Test case with no valid solution."""
        # TODO: Implement
        pass


@pytest.mark.medium
@pytest.mark.string
class TestLongestSubstring:
    """Example: Longest substring without repeating characters."""
    
    def test_basic_case(self):
        """Test basic case."""
        # TODO: Implement solution and uncomment
        # from solutions.longest_substring import length_of_longest_substring
        # assert length_of_longest_substring("abcabcbb") == 3
        pass
    
    def test_all_unique(self):
        """Test string with all unique characters."""
        # TODO: Implement
        pass


@pytest.mark.hard
@pytest.mark.dp
class TestEditDistance:
    """Example: Edit Distance problem tests."""
    
    def test_basic_case(self):
        """Test basic edit distance case."""
        # TODO: Implement solution and uncomment
        # from solutions.edit_distance import min_distance
        # assert min_distance("horse", "ros") == 3
        pass


# Parametrized test example
@pytest.mark.easy
@pytest.mark.array
@pytest.mark.parametrize("nums,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_two_sum_parametrized(nums, target, expected):
    """Parametrized test for multiple test cases."""
    # TODO: Implement solution and uncomment
    # from solutions.two_sum import two_sum
    # assert two_sum(nums, target) == expected
    pass

