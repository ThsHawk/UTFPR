from BTree import *

if __name__ == '__main__':
    tree = Tree(5)
    tree.printTree()
    tree.insert(tree.getRoot(), 1)
    tree.printTree()
    tree.insert(tree.getRoot(), 3)
    tree.printTree()
    tree.insert(tree.getRoot(), 1)
    tree.printTree()
    tree.insert(tree.getRoot(), 2)
    tree.printTree()
    tree.insert(tree.getRoot(), 4)
    tree.printTree()
    tree.insert(tree.getRoot(), 5)
    tree.printTree()
    tree.insert(tree.getRoot(), -1)
    tree.printTree()
