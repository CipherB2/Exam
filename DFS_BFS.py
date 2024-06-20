from random import randint
from PIL import Image, ImageDraw, ImageFont

class Node:
    def __init__(self, val, name):
        self.data:int = val
        self.left: Node | None = None
        self.right: Node | None = None
        self.id: int = name

    def __repr__(self):
        return "\n".join([f'Data = {self.data}',
                          f'Right = {None if self.right is None else self.right.data}',
                          f'Left = {None if self.left is None else self.left.data}'])

class BinaryTree:
    def __init__(self):
        self.root: Node | None = None
        self.count: int = 0

    def __str__(self):
        if self.root is not None:
            return " ".join(self._get_tree(self.root))
        return ''

    def __len__(self):
        if self.root is not None:
            return len(self._get_tree(self.root))
        return 0

    def find(self, value: int):
        if self.root is not None:
            return self._find(value, self.root, None)
        return None

    def insert(self, val: int, name: int):
        if self.root is not None:
            self._insert(val, self.root, name)
        else:
            self.root = Node(val, name)
        self.count += 1

    def delete(self, value: int):
        node,pred = self.find(value)
        if node is not None:
            self._delete_node(node,pred)
            self.count -= 1
        else:
            print(f'В дереве нет узла со значением {value}')

    def delete_tree(self,node: Node):
        if node is not None :
            self.delete_tree(node.left)
            self.delete_tree(node.right)
            del node
            self.count -= 1

    def paint_tree(self,maxLine):
        img = Image.new("RGB", (1000, 1000), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("ArialRegular.ttf",20)

        if self.root is not None:
            self._drawTree(self.root,500,25,250,50,draw,font,maxLine)

        return img

    def dfs_get_maxline(self):

        stack = []
        maxline = []
        return self._dfs_2(self.root)

    def _dfs_maxline(self, node, stack, maxline):
        if node is None :
            return maxline

        stack.append(node.id)

        if node.left is None and node.right is None:
            if len(stack) > len(maxline):
                  maxline = stack[:]
                  #print(maxline)
        else:
            maxline = self._dfs_maxline(node.left, stack,  maxline)
            maxline = self._dfs_maxline(node.right, stack, maxline)

        stack.remove(node.id)

        return maxline

    def _dfs_2(self, node):
        if node is not None :
            m1 = self._dfs_2(node.left)
            m2 = self._dfs_2(node.right)
            if len(m1) >= len(m2) :
                return m1 + [node.id]
            return m2 + [node.id]
        return []

    def _bfs(self):
      queue = [self.root, None]
      i = 0
      while i != len(queue) - 1:
        if queue[i] == None:
          queue.append(None)
        else:
          if queue[i].left is not None: queue.append(queue[i].left)
          if queue[i].right is not None: queue.append(queue[i].right)
        i+=1
      maxline = [self.root.id]
      line = []
      for i in range(2, len(queue)):
        if queue[i] != None:
          line.append(queue[i].id)
        else:
          print('line',line)
          if len(line)>len(maxline):
            maxline = line[:]
          line = []
      return maxline

    def bfs_get_maxline(self):
      return self._bfs()

    def _drawTree(self,node,x,y,dx,dy,draw,font, maxLine):
       if node.left is not None :
         newx,newy = x-dx,y+dy
         draw.line([(x,y),(newx,newy)],width=2,fill = 'black')
         self._drawTree(node.left,newx,newy,dx//2,dy,draw,font, maxLine)
       if node.right is not None:
         newx,newy = x+dx,y+dy
         draw.line([(x,y),(newx,newy)],width=2,fill = 'black')
         self._drawTree(node.right,newx,newy,dx//2,dy,draw,font,maxLine)

       if node.id in maxLine:
           ol = 'red'
       else:
           ol = 'black'
       draw.ellipse( (x-25,y-25,x+25,y+25),fill = 'white', outline = ol)
       if node.data < 10:
           draw.text((x-7,y-7),str(node.data),(0,0,0),font)
       else:
           draw.text((x-10,y-7),str(node.data),(0,0,0),font)

    def _find(self, value: int, node:Node, pred:Node):
        if value == node.data:
            return node,pred
        if value < node.data and node.left is not None:
            return self._find(value, node.left, node)
        if value > node.data and node.right is not None:
            return self._find(value, node.right, node)
        return None

    def _insert(self, value: int, node: Node, name: int):
        if value < node.data:
            if node.left is not None:
                self._insert(value, node.left, name)
            else:
                node.left = Node(value,name)
        else:
            if node.right is not None:
                self._insert(value, node.right, name)
            else:
                node.right = Node(value,name)

    def _pop_max(self, node: Node, pred : Node):
        if node is not None:
            if node.right is None:
                x = node.data
                pred.left = node.left
                del node
            else:
                pred,q = node, node.right
                while q.right is not None:
                    pred = q
                    q = q.right
                x = q.data
                pred.right = q.left
                del q
            return x
        return None

    def _delete_node(self, node: Node, pred:Node):
        if node is not None and pred is not None:
            if node.right is not None and node.left is not None:
                node.data = self._pop_max(node.left,node)
            else:
                if node.left is not None:
                    if pred.left is node:
                        pred.left = node.left
                    else:
                        pred.right = node.left
                else:
                    if pred.left is node:
                        pred.left = node.right
                    else:
                        pred.right = node.right
                del node
        elif pred is None and node is not None:
            if node.right is not None and node.left is not None:
                node.data = self._pop_max(node.left, node)
            elif node.right is None and node.left is None:
                self.root = None
                del node
            else :
               if node.left is not None:
                    self.root = node.left
               else:
                    self.root = node.right
               del node

    def _get_tree(self, node: Node):
        if node is not None:
            return self._get_tree(node.left) + [str(node.data)] \
                   + self._get_tree(node.right)
        return []

tree = BinaryTree()
for i in range(20):
    tree.insert(randint(1, 20), i)
print(tree._get_tree(tree.root))
print(f'Вывод по порядку: {tree}\nРазмер дерева: {len(tree)}')
print(tree)
print(len(tree))

maxLine = tree.dfs_get_maxline()
print(maxLine)
img1 = tree.paint_tree(maxLine)
maxLine = tree.bfs_get_maxline()
print(maxLine)

img2 = tree.paint_tree(maxLine)
tree.delete_tree(tree.root)
tree = None

img1

img2
