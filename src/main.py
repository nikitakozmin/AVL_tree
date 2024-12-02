class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: Node | None = left
        self.right: Node | None = right
        self.height: int = 1


def find_height_and_balance(root: Node | None) -> tuple:
    if root == None:
        return 0, True
    left = find_height_and_balance(root.left)
    right = find_height_and_balance(root.right)
    height = max(left[0], right[0])+1
    is_balanced = abs(left[0] - right[0]) < 2
    return height, left[1] and right[1] and is_balanced

# Checking the whole tree
def check_avl_tree(root: Node | None) -> bool:
    return find_height_and_balance(root)[1]

def diff(root: Node | None) -> int:
    if root == None:
        return float("+inf")
    diffs = [float("+inf")]
    if root.left != None:
        diffs.append(abs(root.val - root.left.val))
        diffs.append(diff(root.left))
    if root.right != None:
        diffs.append(abs(root.right.val - root.val))
        diffs.append(diff(root.right))
    return min(diffs)

def height(root: Node | None) -> int:
    return root.height if root != None else 0

def small_left_turn(root: Node) -> Node:
    tmp_root = root
    root = root.right
    tmp_root.right = root.left
    root.left = tmp_root
    root.left.height = max(height(root.left.left), height(root.left.right))+1
    root.height = max(height(root.left), height(root.right))+1
    return root

def small_right_turn(root: Node) -> Node:
    tmp_root = root
    root = root.left
    tmp_root.left = root.right
    root.right = tmp_root
    root.right.height = max(height(root.right.left), height(root.right.right))+1
    root.height = max(height(root.left), height(root.right))+1
    return root

def balancing(root: Node | None) -> Node:
    if root == None:
        return None
    left_height = height(root.left)
    right_height = height(root.right)
    
    # Left turn
    if left_height - right_height == -2:
        # Big turn
        if height(root.right.left) - height(root.right.right) > 0:
            root.right = small_right_turn(root.right)
        
        return small_left_turn(root)
    
    # Right turn
    elif left_height - right_height == 2:
        # Big turn
        if height(root.left.left) - height(root.left.right) < 0:
            root.left = small_left_turn(root.left)
        
        return small_right_turn(root)
    
    else:
        root.height = max(height(root.left), height(root.right))+1
        return root

def insert(val, root: Node | None) -> Node:
    if root == None:
        return Node(val)
    if val <= root.val:
        if root.left == None:
            root.left = Node(val)
        else:
            root.left = insert(val, root.left)
    else:
        if root.right == None:
            root.right = Node(val)
        else:
            root.right = insert(val, root.right)
    root = balancing(root)
    return root

def delete_max(root: Node | None) -> Node | None:
    if root == None:
        return None, None
    if root.right != None:
        root.right, del_val = delete_max(root.right)
        root = balancing(root)
    else:
        del_val = root.val
        root = root.left
    return root, del_val

def delete_min(root: Node | None) -> Node | None:
    if root == None:
        return None, None
    if root.left != None:
        root.left, del_val = delete_min(root.left)
        root = balancing(root)
    else:
        del_val = root.val
        root = root.right
    return root, del_val

def delete(val, root: Node | None) -> Node | None:
    if root == None:
        return None
    if val < root.val:
        root.left = delete(val, root.left)
    elif val > root.val:
        root.right = delete(val, root.right)
    else:
        if root.right == None:
            root = root.left
        elif root.left == None:
            root = root.right
        else:
            root.right, root.val = delete_min(root.right)
    root = balancing(root)
    return root

def in_order(root: Node | None) -> str:
    if root == None:
        return ""
    rslt = []
    left = in_order(root.left)
    if left != "":
        rslt.append(left)
    right = in_order(root.right)
    rslt.append(str(root.val))
    if right != "":
        rslt.append(right)
    return " ".join(rslt)

def visualize(root: Node) -> None:
    if root == None:
        print("x x x, height: 0")
        return
    if root.left != None:
        left = root.left.val
    else:
        left = "x"
    if root.right != None:
        right = root.right.val
    else:
        right = "x"
    print(f"{left} {root.val} {right}, height: {root.height}")
    if root.left != None:
        visualize(root.left)
    if root.right != None:
        visualize(root.right)

def generate_avl_tree(line: str) -> Node:
    root = None
    arr = list(map(int, line.split()))
    for i in arr:
        root = insert(i, root)
    return root
