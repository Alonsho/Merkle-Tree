# Alon Shoval, 309825172, Or Lion, 204025175
import hashlib

# class to represent each node of the merkle tree
class Node:
    value = None
    right = None
    left = None
    father = None

# create a list of Nodes which are the leaves of the merkle tree
def create_leaves(args):
    leaf_list = []
    for value in args:
        node = Node()
        node.value = value
        leaf_list.append(node)
    return leaf_list




# create a complete merkle tree from given leaves list
def create_merkle_tree(leaf_nodes):
    current_nodes = leaf_nodes
    size = len(current_nodes)
    # loop until created root Node
    while size != 1:
        parent_nodes = []
        i = 0
        # loop to create a father Node from every 2 adjacent nodes
        # NOTE: even indexes are left sons and odd indexes are right sons
        while i < size:
            left_son = current_nodes[i]
            right_son = current_nodes[i+1]
            father_node = Node()
            father_node.left = left_son
            father_node.right = right_son
            left_son.father = father_node
            right_son.father = father_node
            # create the value of father node to be the concatenation of both his sons
            father_node.value = hashlib.sha256((left_son.value + right_son.value).encode()).hexdigest()
            parent_nodes.append(father_node)
            i += 2
        size = len(parent_nodes)
        current_nodes = parent_nodes
    return current_nodes[0]


# create a proof of inclusion for a given leaf Node
def get_proof(args):
    # index of givdn leaf
    num = int(args[0])
    # given leaf
    node = leaf_nodes[num]
    proof = ''
    # loop until reached root of tree
    while node != root:
        father = node.father
        left = father.left
        # check if current node is a left son or a right son and concatenate to 'proof' accordingly
        if node == left:
            proof = proof + 'r ' + father.right.value + ' '
        else:
            proof = proof + 'l ' + left.value + ' '
        node = father
    return proof


# check if given proof of inclusion does indeed match for the given root
def check_proof(args):
    root = args[1]
    # current node
    current_root = args[0]
    i = 2
    # loop to create a hash from the given proof of inclusion
    while i < len(args):
        direction = args[i]
        brother_value = args[i+1]
        if direction == 'l':
            current_root = hashlib.sha256((brother_value + current_root).encode()).hexdigest()
        elif direction == 'r':
            current_root = hashlib.sha256((current_root + brother_value).encode()).hexdigest()
        i += 2
    # check if the resulting root is the same as the given root
    if root == current_root:
        return True
    else:
        return False


# find a number that when concatenated with given root, hash value begins with at least the given number of 0's
def find_nonce(args, root):
    root_value = root.value
    # number of 0's hash should start with
    num = args[0]
    # expression the hash should start with
    regex = '0' * int(num)
    i = 0
    # loop until found an appropriate number
    current = hashlib.sha256((str(i) + root_value).encode()).hexdigest()
    while not current.startswith(regex):
        i += 1
        current = hashlib.sha256((str(i) + root_value).encode()).hexdigest()
    return str(i) + ' ' + current



try:
    root = None
    leaf_nodes = None
    while True:
        user_input = input()
        args = user_input.split()
        input_type = args[0]
        args = args[1:]
        if input_type == '1':
            leaf_nodes = create_leaves(args)
            root = create_merkle_tree(leaf_nodes)
            print(root.value)
        elif input_type == '2':
             proof = get_proof(args)
             print(proof)
        elif input_type == '3':
            is_proof = check_proof(args)
            print(is_proof)
        elif input_type == '4':
            num = find_nonce(args, root)
            print(num)
        elif input_type == '5':
            exit()
        else:
            exit()
except:
    exit(1)
