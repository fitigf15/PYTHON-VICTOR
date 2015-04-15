class SimpleNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.root=None
	self.items=0
    def isEmpty(self):
	return self.root==None
    def push(self,item):
        self.root=SimpleNode(data=item,next=self.root)
	self.items+=1
    def __getitem__(self,position):
	probe=self.root
	for i in range(position):
	    probe=probe.next
	return probe
    def __setitem__(self,position,value):
	probe=self.root
	for i in range(position):
	    probe=probe.next
	probe.data=value
    def pop(self):
	poppedItem=None
	if self.root:
	    poppedItem=self.root.data
	    self.root=self.root.next
	    self.items-=1
	else:
	    print "EMPTY STACK"
	return poppedItem
    def peek(self):
	if self.root:
	    return self.root.data
	else:
	    print "EMPTY STACK"
class ABBNode:
    def __init__(self,val,key,left=None,right=None):
	self.val=val
	self.key=key
	self.right=right
	self.left=left
    def addVal(self,value):
	if type(self.val) is list:
	    self.val.append(value)
	else:
	    self.val=[self.val,value]
    def children_count(self):
	count=0
	if not self.val or not self.key:
	    return None
	if self.left:
	    count+=1
	if self.right:
	    count+=1
	return count
    def __str__(self):
	return "NODE: [VAL:"+str(self.val)+", KEY:"+str(self.key)+"], CHILDREN: [LEFT:"+str(self.left)+" RIGHT:"+str(self.right)+"]"
    
class ABB:
    def __init__(self):
	self.root=None
	self.items=0
    def insert(self,val,key):
	if not(self.root):
	    self.root=ABBNode(val,key)
	    self.items+=1
	else:
	    actual=self.root
	    while actual:
		parent=actual
		if actual.key is key:
		    actual.addVal(val)
		    self.items+=1
		    actual=None
		    parent=None
		elif actual.key<key:
		    actual=actual.right
		else:
		    actual=actual.left
	    if parent:
		if parent.key>key:
		    parent.left=ABBNode(val,key)
		    self.items+=1
		else:
		    parent.right=ABBNode(val,key)
		    self.items+=1
    def search(self,key):
	n=self.root
	while True:
	    if n is None:
		return None
	    elif n.key == key:
		return n
	    elif n.key > key:
		n=n.left
	    else:
		n=n.right
    def searchWithParent(self,key):
	parent=self.root
	node=parent
	if key>parent.key:
	    node=parent.right
	if key<parent.key:
	    node=parent.left
	while True:
	    if node is None:
		return None
	    elif node.key is key:
		return node,parent
	    elif node.key >key:
		parent=node
		node=node.left
	    else:
		parent=node
		node=node.right
	
    def remove(self,key):
	node,parent=self.searchWithParent(key)
	if node is not None:
	    children_count=node.children_count()
	    if children_count==0:
		if parent.left is node:
		    parent.left =None
		else:
		    parent.right=None
		#del node
	    if children_count==1:
		if node.left:
		    n=node.left
		else:
		    node=node.right
		if parent:
		    if parent.left is node:
			parent.left=n
		    else:
			parent.right=n
		#del node
	    if children_count==2:
		parent=node
		successor=node.right
		while successor.left:
		    parent=successor
		    successor=successor.left
		node.key=successor.key
		node.val=successor.val
		if parent.left is successor:
		    parent.left=successor.right
		else:
		    parent.right=successor.right
    def preorder(self):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    node=self.root
	    
	    while not stop:
		if node!=None:
		    print str(node.val)+",",
		    stack.push(node)
		    node=node.left
		else:
		    if not stack.isEmpty():
			node=stack.pop()
			node=node.right
		    else:
			stop=True  
    def inorder(self):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    node=self.root
	    while not stop:
		if node!=None:
		    stack.push(node)
		    node=node.left
		else:
		    if not stack.isEmpty():
			node=stack.pop()
			print str(node.val)+",",
			node=node.right
		    else:
			stop=True
    def postorder(self):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    head=self.root
	    node=self.root
	    stack.push(self.root)
	    while not stack.isEmpty():
		node=stack.peek()
		if node.left is head or node.right is head or (node.left is None and node.right is None):
		    stack.pop()
		    print str(node.val)+",",
		    head=node
		else:
		    if node.right is not None:
			stack.push(node.right)
		    if node.left is not None:
			stack.push(node.left)
	    
	
	    

def pre():
    a=ABB()
    print "F, B, A, D, C, E, G, I, H"
    a.insert("F",6)
    a.insert("B",2)
    a.insert("A",1)
    a.insert("D",4)
    a.insert("C",3)
    a.insert("E",5)
    a.insert("G",7)
    a.insert("I",9)
    a.insert("H",8)
    a.preorder()
    print
def inord():
    a=ABB()
    print "A, B, C, D, E, F, G, H, I"
    a.insert("F",6)
    a.insert("B",2)
    a.insert("A",1)
    a.insert("D",4)
    a.insert("C",3)
    a.insert("E",5)
    a.insert("G",7)
    a.insert("I",9)
    a.insert("H",8)
    a.inorder()
    print
def postord():
    a=ABB()
    print " A, C, E, D, B, H, I, G, F "
    a.insert("F",6)
    a.insert("B",2)
    a.insert("A",1)
    a.insert("D",4)
    a.insert("C",3)
    a.insert("E",5)
    a.insert("G",7)
    a.insert("I",9)
    a.insert("H",8)
    a.postorder()  
def remove():
    a=ABB()
    a.insert("F",6)
    a.insert("B",2)
    a.insert("A",1)
    a.insert("D",4)
    a.insert("C",3)
    a.insert("E",5)
    a.insert("G",7)
    a.insert("I",9)
    a.insert("H",8)
    a.inorder()
    a.remove(6)
    a.inorder()
    a.remove(9)
    a.inorder()

