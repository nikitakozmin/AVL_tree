"""This file should be placed along with the executable file."""

import pytest
from main import *

@pytest.mark.parametrize('root',
                    [
                        (None),
                        (Node(15)),
                        (generate_avl_tree("-34 45 66")),
                        (generate_avl_tree("758 -98 457 189 434 802 5 5 -561 92")),
                    ])
def test_generate_avl_tree(root):
    assert check_avl_tree(root) == True

@pytest.mark.parametrize('root, del_vals, expected_inorder',
                    [
                        (None, [5], ""),
                        (Node(15), [15], ""),
                        (generate_avl_tree("-34 45 66"), [-34, 45], "66"),
                        (
                            generate_avl_tree("758 -98 457 189 434 802"),
                            [758, 457, 500, 802, 457],
                            "-98 189 434"
                        ),
                    ])
def test_delete_vals(root, del_vals, expected_inorder):
    for i in del_vals:
        root = delete(i, root)
    assert check_avl_tree(root) == True
    assert in_order(root) == expected_inorder
