from structure import TreeNode


class BST:
    __root = None

    def build(self, tree_list):
        for n in tree_list:
            self.append(self.__root, n, father=None)

    def search(self, key: TreeNode) -> TreeNode:
        if self.__root is None:
            raise Exception("search:尚未初始化数据")
        return self.__find(self.__root, key)

    def __find(self, node: TreeNode, key: TreeNode) -> TreeNode:
        cmp = self.__compare(key.val(), node.val())
        if cmp < 0:
            return self.__find(node.lc(), key)
        elif cmp > 0:
            return self.__find(node.rc(), key)
        else:
            return node

    def append(self, node: TreeNode, new_Node: TreeNode, father, left_side=True):
        if node is None:
            if self.__root is None:
                self.__root = new_Node
            elif left_side:
                father.set_lc(new_Node)
            elif not left_side:
                father.set_rc(new_Node)
        else:
            cmp = self.__compare(new_Node.val(), node.val())
            if cmp < 0:
                self.append(node.lc(), new_Node, node, left_side=True)
            elif cmp > 0:
                self.append(node.rc(), new_Node, node, left_side=False)
            else:
                node.copy(new_Node)

    def __compare(self, a, b):
        # if you want get an result by DECS, feel free to exchange value [-1 1]
        if a == b:
            return 0
        else:
            return 1 if a > b else -1


# There is the demo how to use this alg-class
if __name__ == '__main__':
    # 1. get Instance and set sort-order
    S = BST()
    # 2. prepare data
    import datasets
    tree = datasets.load_bst_tree_data()
    # 3. feed data to BST
    S.build(tree)
    # 4. get result
    target = TreeNode(2, None, None, index=-1)
    print(S.search(target))

