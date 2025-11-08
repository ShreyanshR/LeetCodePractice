"""
Test cases for backtracking algorithms, particularly the reachPath function.

Tests various tree structures with at least 3 levels to ensure proper backtracking behavior.
"""

import pytest
from solutions.backtracking import TreeNode, reachPath, canReachLeaf


@pytest.fixture
def basic_tree_3_levels():
    """Create a basic 3-level tree that can reach a leaf."""
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


@pytest.fixture
def tree_with_blocked_path():
    """Create a 3-level tree with a blocked (zero) node in one path."""
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    / \
    #   0   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)  # blocked
    root.left.right = TreeNode(5)
    return root


@pytest.fixture
def deep_tree_4_levels():
    """Create a 4-level tree to test deeper backtracking."""
    # Tree structure:
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7
    #    / \     \
    #   8   9    10
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.right.left.right = TreeNode(10)
    return root


@pytest.fixture
def fully_blocked_tree():
    """Create a tree where all nodes are blocked."""
    # Tree structure:
    #       0
    #      / \
    #     0   0
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    return root


@pytest.mark.tree
@pytest.mark.backtracking
@pytest.mark.medium
class TestReachPath:
    """Test suite for the reachPath backtracking function."""

    def test_basic_3_level_tree_left_path(self, basic_tree_3_levels):
        """Test reachPath on 3-level tree finding left path."""
        path = []
        result = reachPath(basic_tree_3_levels, path)
        
        assert result is True
        # Should find a path to a leaf (either [1, 2, 4] or [1, 2, 5] or [1, 3])
        assert len(path) == 3
        assert path[0] == 1  # root
        assert path[-1] in [3, 4, 5]  # should end at a leaf
        # Verify it's a valid path from root
        assert path == [1, 2, 4] or path == [1, 2, 5] or path == [1, 3]

    def test_tree_with_blocked_path(self, tree_with_blocked_path):
        """Test reachPath when one path is blocked."""
        path = []
        result = reachPath(tree_with_blocked_path, path)
        
        assert result is True
        # Should find [1, 3] since left path is blocked at node 0
        # Or it could find [1, 2, 5] by skipping the blocked left child
        assert len(path) == 2 or len(path) == 3
        assert path[0] == 1
        
        # Should not contain 0 (blocked node)
        assert 0 not in path

    def test_deep_tree_4_levels(self, deep_tree_4_levels):
        """Test reachPath on a 4-level tree."""
        path = []
        result = reachPath(deep_tree_4_levels, path)
        
        assert result is True
        # Should find a path to a leaf
        assert len(path) >= 3  # At least 3 levels deep
        assert path[0] == 1
        # Verify it ends at a leaf
        assert path[-1] in [8, 9, 10, 5, 7]

    def test_all_paths_blocked(self, fully_blocked_tree):
        """Test reachPath when all nodes are blocked."""
        path = []
        result = reachPath(fully_blocked_tree, path)
        
        assert result is False
        assert len(path) == 0

    def test_single_node_tree(self):
        """Test reachPath on a single node tree."""
        root = TreeNode(5)
        path = []
        result = reachPath(root, path)
        
        assert result is True
        assert path == [5]

    def test_single_node_blocked(self):
        """Test reachPath on a single blocked node."""
        root = TreeNode(0)
        path = []
        result = reachPath(root, path)
        
        assert result is False
        assert len(path) == 0

    def test_path_tracking_multiple_levels(self):
        """Verify that path tracking works correctly across multiple levels."""
        # Tree structure:
        #          1
        #        /   \
        #       2     0
        #      / \     \
        #     4   5     6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(0)  # blocked
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        path = []
        result = reachPath(root, path)
        
        assert result is True
        # Should take left path only since right is blocked
        assert path[0] == 1
        assert path[1] == 2
        assert path[2] in [4, 5]
        assert len(path) == 3

    def test_unbalanced_tree_left(self):
        """Test reachPath on a left-heavy unbalanced tree (4 levels)."""
        # Tree structure (left-heavy):
        #          1
        #         /
        #        2
        #       /
        #      3
        #     /
        #    4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        path = []
        result = reachPath(root, path)
        
        assert result is True
        assert path == [1, 2, 3, 4]
        assert len(path) == 4

    def test_unbalanced_tree_right(self):
        """Test reachPath on a right-heavy unbalanced tree (4 levels)."""
        # Tree structure (right-heavy):
        #          1
        #           \
        #            2
        #             \
        #              3
        #               \
        #                4
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        
        path = []
        result = reachPath(root, path)
        
        assert result is True
        assert path == [1, 2, 3, 4]
        assert len(path) == 4

    def test_complex_tree_with_multiple_solutions(self):
        """Test reachPath on a tree with multiple valid paths (5 levels)."""
        # Tree structure:
        #              1
        #            /   \
        #           2     3
        #          / \   / \
        #         4   0 6   7
        #        / \
        #       8   9
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(0)  # blocked
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        
        path = []
        result = reachPath(root, path)
        
        assert result is True
        # Should find one of many valid paths
        assert len(path) >= 3
        assert path[0] == 1
        # Should not contain the blocked node
        assert 0 not in path

    def test_path_backtracking_verification(self):
        """Verify that path is correctly modified during backtracking."""
        # This test ensures that when we backtrack, we properly remove nodes
        # from the path that didn't lead to a solution.
        root = TreeNode(1)
        root.left = TreeNode(0)  # blocked, should backtrack here
        root.right = TreeNode(3)
        
        path = []
        result = reachPath(root, path)
        
        assert result is True
        # Should only have [1, 3], not [1, 0, ...]
        assert 0 not in path
        assert path == [1, 3]

