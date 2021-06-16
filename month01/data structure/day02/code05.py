"""
    二叉树的构建与遍历
    重点代码
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



class BiTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return not self.root

    def pre_order(self):
        res_list = []
        BiTree.get_val_pre_order(self.root, res_list)
        return res_list

    def mid_order(self):
        res_list = []
        BiTree.get_val_mid_order(self.root, res_list)
        return res_list

    def pos_order(self):
        res_list = []
        BiTree.get_val_pos_order(self.root, res_list)
        return res_list

    @staticmethod
    def get_val_pre_order(root, result_list):
        result_list.append(root.value)
        if root.left:
            BiTree.get_val_pre_order(root.left, result_list)
        if root.right:
            BiTree.get_val_pre_order(root.right, result_list)

    @staticmethod
    def get_val_mid_order(root, result_list):
        if root.left:
            BiTree.get_val_mid_order(root.left, result_list)
        result_list.append(root.value)
        if root.right:
            BiTree.get_val_mid_order(root.right, result_list)

    @staticmethod
    def get_val_pos_order(root, result_list):
        if root.left:
            BiTree.get_val_pos_order(root.left, result_list)
        if root.right:
            BiTree.get_val_pos_order(root.right, result_list)
        result_list.append(root.value)


if __name__ == "__main__":
    # 按照后续遍历增加节点
    b = Node("B")
    f = Node("F")
    g = Node("G")
    d = Node("D", f, g)
    i = Node("I")
    h = Node("H")
    e = Node("E", i, h)
    c = Node("C", d, e)
    a = Node("A", b, c)

    tree = BiTree(a)
    print(tree.is_empty())
    print(tree.pre_order())
    print(tree.mid_order())
    print(tree.pos_order())