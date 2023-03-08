class Nodes():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.tos = None

    def is_empty(self):
        if self.tos == None:
            return True
    
    def push(self, new_node):
        node = Nodes(new_node)
        if self.tos == None:
            self.tos = node
        else:
            self.tos.next = node
            self.tos = node
    
    def pop(self):
        if self.tos == None:
            return None
        else:
            node = self.tos
            self.tos = self.tos.next
            node.next = None
            return node.value
    
    def display(self):
        node = self.tos
        while node:
            print(node.value)
            print(33333)
            node = node.next


st1 = Stack()
st1.push(2)
st1.push(3)
st1.push(4)
st1.push(7)
x = st1.pop()
print(x)
st1.display()

