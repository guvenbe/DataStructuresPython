class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # Breadth First Search
    def BSF(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_post_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def dfs_in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result

my_tree = BinarySearchTree()
print(my_tree.root)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(27))
print(my_tree.contains(17))

my_tree2 = BinarySearchTree()
my_tree2.insert(47)
my_tree2.insert(21)
my_tree2.insert(76)
my_tree2.insert(18)
my_tree2.insert(27)
my_tree2.insert(52)
my_tree2.insert(82)

print("Breadth first tree")
print(my_tree2.BSF())

my_tree3 = BinarySearchTree()
my_tree3.insert(47)
my_tree3.insert(21)
my_tree3.insert(76)
my_tree3.insert(18)
my_tree3.insert(27)
my_tree3.insert(52)
my_tree3.insert(82)

print("DFS one Pre Order")
print(my_tree3.dfs_pre_order())

my_tree4 = BinarySearchTree()
my_tree4.insert(47)
my_tree4.insert(21)
my_tree4.insert(76)
my_tree4.insert(18)
my_tree4.insert(27)
my_tree4.insert(52)
my_tree4.insert(82)

print("DFS one Post Order")
print(my_tree4.dfs_post_order())

my_tree5 = BinarySearchTree()
my_tree5.insert(47)
my_tree5.insert(21)
my_tree5.insert(76)
my_tree5.insert(18)
my_tree5.insert(27)
my_tree5.insert(52)
my_tree5.insert(82)

print("DFS In Order")
print(my_tree5.dfs_in_order())