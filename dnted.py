import functools
from zss import distance, simple_distance
from zss.simple_tree import Node

def zero_or_one_distance(a, b):
    if a == b:
        return 0
    else:
        return 1

def default_tree_size(tree,get_children):
    size = 1
    children = get_children(tree)
    if children:
        size = size + sum(default_tree_size(child,get_children) for child in children)
    return size

def _compute_normalized_distance(edit_distance,alpha,size_A,size_B):
    return (2*edit_distance)/(alpha*(size_A+size_B)+edit_distance)

def normalized_simple_distance(A,B,get_children=Node.get_children,alpha=1,get_tree_size=None,return_operations=False,**kwargs):
    if get_tree_size is None:
        get_tree_size = functools.partial(default_tree_size,get_children=get_children)
    if return_operations:
        edit_distance, operations = simple_distance(A,B,get_children=get_children,**kwargs)
    else:
        edit_distance = simple_distance(A,B,get_children=get_children,**kwargs)
    d = _compute_normalized_distance(edit_distance,alpha,get_tree_size(A),get_tree_size(B))
    if return_operations:
        return d, operations
    else:
        return d

def normalized_distance(A,B,get_children,alpha=1,get_tree_size=None,return_operations=False,**kwargs):
    if get_tree_size is None:
        get_tree_size = functools.partial(default_tree_size,get_children=get_children)
    if return_operations:
        edit_distance, operations = distance(A,B,get_children,**kwargs)
    else:
        edit_distance = distance(A,B,get_children,**kwargs)
    d = _compute_normalized_distance(edit_distance,alpha,get_tree_size(A),get_tree_size(B))
    if return_operations:
        return d, operations
    else:
        return d
