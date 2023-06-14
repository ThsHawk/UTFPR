from BTree import *

if __name__ == '__main__':
    tree = Tree(3)
    tree.printTree()
    tree.insert(tree.getRoot(), 1)
    tree.printTree()
    tree.insert(tree.getRoot(), 3)
    tree.printTree()
    tree.insert(tree.getRoot(), 1)
    tree.printTree()
    tree.insert(tree.getRoot(), 2)
    tree.printTree()
