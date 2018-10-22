
# What is Trie: “Trie” basically comes from the word “retrieval”, as 
# the main purpose of using this structure is that it provides fast
# retrieval. Tries are mostly used for searching words in the dictionary,
# provide auto-suggestions in search engines, and for IP routing as well.

#Trie delete caan become complecated as follows:
#While deleting a word from a Trie, we need to perform two important steps
# which are given below:
#Suppose we have a root and their, the and bat words

#First of all all, we find the “value” set for the given word and set it
# to null. The value is always stored at the last letter of the word

#Secondly, we make sure that the node that we are trying to delete does
# not have any further branches. If there are no branches, then we can
# easily remove the node. However, if the node contains further branches
# then this opens up a lot of scenarios which are covered below:

#Case 1: If the word to be deleted has no common subsequence
#If the word to be deleted has no common subsequence, then all the nodes
# of that word are deleted. ie: root has their and bat then rmoving bat we
#have to delete all the characters

#Case 2: If the word to be deleted is a prefix of some other word
#If the word to be deleted is a prefix of some other word, then the
# value of isEndWord of the last node of that word is set to false,
# and no node is deleted.i.e: to remove the (inside their) we unmark e
# to show that the word “the” doesn’t exist anymore.

#case 3: If the word to be deleted has a common prefix
#If the word to be deleted has a common prefix and the last node of that
# word is also the leaf node i.e. last node of its branch, then this node
# is deleted along with all the nodes up in its branch which do not have
# any other children and whose isEndWord is false.i.e: in order to delete
# their, #  we’ll traverse the common path upto the and delete the 
# characters “i” and “r”.

class TrieNode:
  def __init__(self):
    self.children = [] #Total # of English Alphabets
    for _ in range(26):
      self.children.append(None)
    self.isEndWord = False #will be true if the node represents the end of word
    self.value = -1 #To store the value of a particular key
  
  #Function to mark the currentNode as Leaf
  def markAsLeaf(self,val):
    self.value = val
    self.isEndWord = True
    
  #Function to unMark the currentNode as Leaf  
  def unMarkAsLeaf(self):
    self.value = -1
    self.isEndWord = False

#A Trie will be implemented using the Node class. 
# a Node in Trie represents one alphabet which keeps pointers
# to children nodes. Each Node can have at max 26 children
# if we are storing English words.
class Trie:
  def __init__(self):
    self.root = TrieNode() #Root node
    
  #Function to get the index of character 't'
  def getIndex(self,t):
    return ord(t) - ord('a')
  
  #Function to insert a key,value pair in the Trie
  def insert(self,key,value):
    if key == None:
      return
    
    key = key.lower()
    currentNode = self.root
    index = 0
    #Iterate the Trie with given character index,
    #If it is None, then simply create a TrieNode and go 
    #down a level
    for level in range(len(key)):
      index = self.getIndex(key[level])
      if currentNode.children[index] == None:
        currentNode.children[index] = TrieNode()
      currentNode = currentNode.children[index]
      
    currentNode.markAsLeaf(value)

   
  #Function to search a given key in Trie
  def search(self,key):
    if key == None:
      return False #None key
    
    key = key.lower()
    currentNode = self.root
    index = 0
   
    #Iterate the Trie with given character index,
    #If it is None at any point then we stop and return false
    #We will return true only if we reach leafNode and have traversed the
    #Trie based on the length of the key. if the key is 
    #completely traversed and isEndWord is set for the last
    #node in the path.
    
    for level in range(len(key)):
      index = self.getIndex(key[level])
      if currentNode.children[index] == None:
        return False
      currentNode = currentNode.children[index]
      
    if currentNode != None and currentNode.isEndWord:
      return True
    
    return False
  
  #Helper Function to return true if currentNode does not have any children
  def hasNoChildren(self, currentNode):
    for i in range(len(currentNode.children)):
      if currentNode.children[i] != None:
        return False
    return True 
  

 


  #deleteHelper() is a recursive function to delete given key, it takes in
  # a key of type string, root of Trie, length of the key, and an integer
  # indicating level as an argument.

  #It goes through all the cases explained above, while the base case for this
  # recursive function is when the level becomes equal to the length of key i.e 
  #we’ve reached the last node in Trie path indicating the last character for the
  # particular word. At this point we check if the last node has any further
  # children or not, if it does then we simply unMark it i.e setting isEndWord to 
  # False, while on the other hand if the last node doesn’t contain any children then
  # we simply set it to None and move up in Trie for checking remaining nodes of the path.
  def deleteHelper(self, key, currentNode, length, level):
    deletedSelf = False
    if currentNode == None:
      print("Key does not exist")
      return deletedSelf
   
    #Base Case: If we have reached at the node which points to the 
    # alphabet at the end of the key.
    if level == length:
      #If there are no nodes ahead of this node in this path
      #Then we can delete this node
      if self.hasNoChildren(currentNode):
        currentNode = None
        deletedSelf = True  
      
      #If there are nodes ahead of currentNode in this path 
      #Then we cannot delete currentNode. We simply unmark this as leaf
      else:
        currentNode.unMarkAsLeaf()
        deletedSelf = False

    else:
      childNode = currentNode.children[self.getIndex(key[level])]
      childDeleted = self.deleteHelper(key, childNode, length, level + 1)
      if childDeleted:
        #Making children pointer also null: since child is deleted
        currentNode.children[self.getIndex(key[level])] = None
        #If currentNode is leaf node that means currentNode is part of another key
        #and hence we can not delete this node and it's parent path nodes
        if currentNode.isEndWord:
          deletedSelf = False
        
        #If childNode is deleted but if currentNode has more children then currentNode must be part of another key
        #So, we cannot delete currenNode
        elif self.hasNoChildren(currentNode) == False:
          deletedSelf = False
        
        #Else we can delete currentNode
        else:
          currentNode = None
          deletedSelf = True
        
      else:
        deletedSelf = False
      
    return deletedSelf


  #Function to delete given key from Trie
  #Delete Function takes in a key of type string and then checks if either
  # Trie is empty or key is None, and for each case, it simply returns from the function.
  def delete(self,key):
    if self.root == None or key == None:
      print("Null key or Empty trie error")
      return
    self.deleteHelper(key, self.root, len(key), 0)

  
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any",
                     "by", "bye", "their","abc"]
    output = ["Not present in trie", "Present in trie"]
    
    t = Trie()
    print("Keys to insert: ")
    print(keys)
    
    #Construct Trie
    for i in range(len(keys)):
      t.insert(keys[i], i)
    
    if t.search("the") == True:
      print("the --- " + output[1])
    else:
      print("the --- " + output[1])
      
    if t.search("these") == True:
      print("these --- " + output[1])
    else:
      print("these --- " + output[0])
      
    if t.search("abc") == True:
      print("abc --- " + output[1])
    else:
      print("abc --- " + output[1])

    t.delete("abc")
    print("Deleted key \"abc\"")
         
    if t.search("abc") == True:
      print("abc --- " + output[1])
    else:
      print("abc --- " + output[0])

if __name__ == "__main__":
    main()
