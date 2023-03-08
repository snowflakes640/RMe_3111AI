class Node:
    def __init__(self, element):
        self.value = element
        self.next = None

class Que:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front is None and self.rear is None:
            return True
    
    def push(self, new_node):
        node = Node(new_node)
        if self.front is None and self.rear is None:
            self.front = node 
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def pop(self):
        if self.front == None:
            return None
        else:
            node = self.front
            self.front = self.front.next
            return node.value

    def display(self):
        node = self.front
        while node:
            print (node.value)
            node = node.next
            

q1 = Que()
q1.push(2)
q1.push(3)
q1.push(4)
q1.push(5)
x = q1.pop()
print(f"The first elem:{x}")
q1.display()
