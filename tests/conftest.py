"""
Pytest configuration and shared fixtures.

Add common test fixtures and utilities here.
"""

import pytest
from typing import List, Any


@pytest.fixture
def sample_array() -> List[int]:
    """Sample array for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_tree():
    """Sample binary tree for testing."""
    # TODO: Define your TreeNode class and create sample tree
    pass


@pytest.fixture
def sample_graph():
    """Sample graph for testing."""
    return {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }


class AssertionHelpers:
    """Helper methods for common assertions."""
    
    @staticmethod
    def assert_lists_equal_unordered(list1: List[Any], list2: List[Any]):
        """Assert two lists are equal regardless of order."""
        assert sorted(list1) == sorted(list2)
    
    @staticmethod
    def assert_tree_equal(tree1, tree2) -> bool:
        """Assert two binary trees are equal."""
        # TODO: Implement tree comparison
        pass


@pytest.fixture
def helpers():
    """Provide assertion helpers to tests."""
    return AssertionHelpers()

