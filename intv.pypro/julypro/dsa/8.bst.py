# binary search tree 
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return  # node already exist

        if data < self.data:
            if self.left:
                # insert into left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                # insert into right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        elements = []
        # visit left subtree
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        # visit right subtree
        if self.right:
            elements += self.right.inorder_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements += [self.data]
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    print(numbers)
    countries = ["India", "Japan", "Korea", "USA", "China", "Pakistan", "Korea", "Russia", "USA"]
    str_tree = build_tree(countries)
    print(str_tree.inorder_traversal())
    print(str_tree.search("Korea"))
    print(str_tree.search("Arab"))
    tree = build_tree(numbers)

    print(tree.inorder_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    print(tree.calculate_sum())
    print(tree.find_min())
    print(tree.find_max())
    print(tree.search(20))
    print(tree.search(188))
    tree.delete(34)
    tree.delete(9444)
    print(tree.inorder_traversal())
    print(tree.search(34))
