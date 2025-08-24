from dataclasses import dataclass

@dataclass
class AVL:
    key: int
    height: int
    left: 'AVL'=None
    right: 'AVL'=None

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left)-get_height(node.right) if node else 0

def right_rotate(node):##node为原本的根节点，node_left为新根节点，并返回
    node_left = node.left
    node_left_right=node_left.right
    node.left = node_left_right
    node_left.right = node

    node.height = 1+max(get_height(node.left), get_height(node.right))
    node_left.height = 1+max(get_height(node_left.left), get_height(node_left.right))

    return node_left

def left_rotate(node):
    node_right = node.right
    node_right_left=node_right.left
    node_right.left = node
    node.right = node_right_left

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    node_right.height = 1+max(get_height(node_right.left), get_height(node_right.right))
    return node_right

def insertion(root, key):
    if not root:
        return AVL(key,1)
    elif key < root.key:
        root.left = insertion(root.left, key)
    elif key > root.key:
        root.right = insertion(root.right, key)
    else:
        return root

    root.height = max(get_height(root.left), get_height(root.right))+1
    balance = get_balance(root)
    ##ll
    if balance >1 and key <root.left.key:
        return right_rotate(root)
    ##rr
    elif balance<-1 and key > root.right.key:
        return left_rotate(root)
    ##lr
    elif balance>1 and key > root.left.key:
        root.left=left_rotate(root.left)
        return right_rotate(root)
    ##rl
    elif balance<-1 and key <root.right.key:
        root.right=right_rotate(root.right)
        return left_rotate(root)
    return root

def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

if __name__ == '__main__':
    root = None
    nums = [1,2,32,23,57,61,7]
    for num in nums:
        root = insertion(root, num)
    print(inorder(root))

