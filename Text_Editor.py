#text editor

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
class doubly_linked_list:
   def __init__(self):
      self.head = None     

   def append(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = None
      if self.head is None:
         NewNode.prev = None
         self.head = NewNode
         return
      last = self.head
      while (last.next is not None): 
         last = last.next
      last.next = NewNode
      NewNode.prev = last
      return
 
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         node = node.next
         
characterList = doubly_linked_list()
val = input("Text Editor:\n") + input("") 

while input() != '':
    val += input('')

for element in val:
    characterList.append(element)

characterList.listprint(characterList.head)
