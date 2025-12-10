class Node:
    def __init__(self, value):
        self.value = value
        self.left: "Node | None" = None
        self.right: "Node | None" = None


def insert(root: Node | None, value) -> Node:
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def find_max_value(root: Node | None):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current.value


if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, 20]
    root = None
    for v in values:
        root = insert(root, v)

    print(find_max_value(root))  # 20