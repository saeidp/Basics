class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
#--------------------------------------------------
# Given a binary tree, figure out whether it's a BST
#A binary search tree holds the property that each node's
# key value is smaller than the key value of all nodes
# in the right subtree and greater than the key values of
# all nodes in the left subtree i.e. L < N < R.

#O(n) runtime and o(h) memory (h: is log(n) in balance
# and n in unbalance)
# In order Traverse
import sys
def is_bst_rec(root, min_value, max_value):
    if root == None:
        return True
    if root.data < min_value or root.data > max_value:
        return False
    return is_bst_rec(root.left, min_value, root.data) and \
           is_bst_rec(root.right, root.data, max_value) 

def is_bst(root):
    return is_bst_rec(root, -sys.maxsize - 1, sys.maxsize)

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(125)
root.right.left = Node(150)
root.right.right = Node(350)

print(is_bst(root)) #False  50 < 125 < 100

root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.left = Node(125)
root.right.right = Node(350)
print(is_bst(root)) #True

# Solution 2 - Another basic approach less efficient than the above
# A basic algorithm would be to check on each node that
#  maximum value of its left sub-tree is less than node's
# data and minimum value of its right sub-tree is greater
#  than node's data

# /* Returns true if a binary tree is a binary search tree */ 
# int isBST(struct node* node)  
# {  
#   if (node == NULL)  
#     return(true);  
      
#   /* false if the max of the left is > than us */
#   if (node->left!=NULL && maxValue(node->left) > node->data)  
#     return(false);  
      
#   /* false if the min of the right is <= than us */
#   if (node->right!=NULL && minValue(node->right) < node->data)  
#     return(false);  
    
#   /* false if, recursively, the left or right is not a BST */
#   if (!isBST(node->left) || !isBST(node->right))  
#     return(false);  
      
#   /* passing all that, it's a BST */
#   return(true);  
# }  

# Solution 3 O(n) using inorder traverse to order the data then 
# check if this order is valid
# boolean checkBST(Node root) {
#         ArrayList<Integer> result = new ArrayList<>();
#         result = inOrder(root, result);
#         for(int i=0; i < result.size()-1; i++){
#             if(result.get(i) >= result.get(i+1)) return false;
#         }
#         return true;
#     }
    
#     private ArrayList<Integer> inOrder(Node root, ArrayList<Integer> list){
#         if(root == null) return null;
#         else{
#             if(root.left != null) inOrder(root.left, list);
#             list.add(root.data);
#             if(root.right != null) inOrder(root.right, list);
#             return list;
#         }
#     }