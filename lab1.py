##Creating queue class:

class Node:
    def __init__(self, element):
        self.value = element
        self.next = None

class Que:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front == None and self.rear == None:
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
            if self.front == None: self.rear= None
        return node.value

    def display(self):
        node = self.front
        while node:
            print (node.value)
            node = node.next

#Taking input for graph            
nodes = input("Enter the number of nodes: ")
edges = int(input("Enter the number of edges: "))
def input_graph(edges):
    graph = {}
    for i in range(edges):
        from_node = input("Enter a parent_node: ")
        to_node = input("Enter the child_node: ")
        
        if from_node in graph:
            graph[from_node].append(to_node)
        else:
            graph[from_node] = [to_node]
    print(f"The given graph would be: {graph}")

# graph = {
#     "0" : ["1", "2"],
#     "1" : ["2"],
#     "2" : ["0", "3"],
#     "3" : ["3"]
# }

#Taking input for finding path:

source = input("Enter source-node: ")
target = input("Enter target-node: ")

explore = Que()
explore.push(source)
mark = set()
flag = 1

while not explore.is_empty():
    current = explore.pop()
    if current not in mark:
        mark.add(current)
        for j in graph[current]:
            if j!=target:
                explore.push(j)
            else:
                flag = 0
                print("found")
                break

if flag != 0:
    print("not found")

input_graph(edges)