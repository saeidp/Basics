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
#----------------------------------------------------------
# This unction should return all the words
# keys = ["the", "a", "there", "answer", "any",
#         "by", "bye", "their","abc"]
# output -> 'a', 'abc','answer','any','by','bye','the','their','there'
#Recursive Function to generate all words
def getWords(root, result, level, string):
	#Leaf denotes end of a word
	if root.isEndWord:
    #current word is stored till the 'level' in the character array
		temp = ""
		for x in range(level):
			temp += str(string[x])
		
		result.append(temp)
	for i in range(26):
		if root.children[i] != None:
			#Non-None child, so add that index to the character array
			string[level] = chr(i + ord('a'))
			getWords(root.children[i], result, level + 1, string)
		
    
def findWords(root):
	result = []
	chararr = [None] * 20
	getWords(root, result, 0, chararr)
	return result


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any",
                     "by", "bye", "their","abc"]
    t = Trie()
    for i in range(len(keys)):
      t.insert(keys[i], i)
    words = findWords(t.root)
    print(words) # -> [output -> 'a', 'abc','answer', 'any','by','bye','the','their','there']

main()