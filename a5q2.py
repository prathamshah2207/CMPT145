# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import treenode as tn
def subst(tnode, t, r):
    """
    Substitute a target value t with a replacement value r wherever it appears in the given tree.
    :param tnode: The root treenode
    :param t: Target value to replace
    :param r: The replacement value
    :return: None
    """

    if tnode is None:
        return None
    else:
        if tnode.get_data() == t:
            tnode.set_data(r)
        subst(tnode.get_left(), t, r)
        subst(tnode.get_right(), t, r)

def copy(tnode):
    """
    Create an exact copy of the given tree, with completely new treenodes, but exactly the same data values, in exactly the same places.
    :param tnode: The root treenode
    :return: A reference to the new tree.
    """

    if tnode is None:
        return None
    else:
        left = copy(tnode.get_left())
        right = copy(tnode.get_right())

        data = tnode.get_data()
        newtree = tn.Treenode(data)

        newtree.set_left(left)
        newtree.set_right(right)

        return newtree

