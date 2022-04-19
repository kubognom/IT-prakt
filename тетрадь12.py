T = ["a",["b", ["d","e"]],["c",["f"]]]
print("koren",T[0])
print("levoe",T[1])
print("pravoe",T[2])
class tree:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      #print(self.data)
      if self is not None:
         self.PrintTree2(self)

   def PrintTree2(self,node):
      if node is not None:
         self.PrintTree2(node.left)
         self.PrintTree2(node.right)
         print(str(node.data) + "")
   def vstav(self,data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = tree(data)
            else:
               self.left.vstav(data)
         elif data > self.data:
            if self.right is None:
               self.right = tree(data)
            else:
               self.right.vstav(data)
      else:
         self.data = data

kor = tree(20)
kor.vstav(21)
kor.vstav(19)
kor.vstav(18)

kor.PrintTree()