import math
class Node:
    def __init__(self,element, priority):
        self.node = element
        self.priority = priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i-1)/2)

    def left_child(self, i):
        return int(2*i + 1)

    def right_child(self, i):
        return int(2*i + 2)
    
    def height(self):
        N = len(self.heap)
        h = math.log(N+1,2)
        return h

    def swap(self, a, b):
        temp = self.heap[a]
        self.heap[a]= self.heap[b]
        self.heap[b] = temp

    def reHeapUp(self, i):
        if i == 0:
            return
        else:
            while(self.heap[i] < self.heap[self.parent(i)]):
                #print(self.heap[i], self.heap[self.parent(i)])
                self.swap(i, self.parent(i))
                i = self.parent(i)

    def reheapDown(self, i):
        h = 1
        while(h<self.height() and i<=len(self.heap)-1):
            if(self.right_child(i)<= len(self.heap)-1 and self.left_child(i)<= len(self.heap)-1):
                if self.heap[self.right_child(i)] < self.heap[self.left_child(i)]:
                    smaller_child = self.right_child(i)
                else:
                    smaller_child = self.left_child(i)
                
                while(self.heap[i] > self.heap[smaller_child]):
                    self.swap(i, smaller_child)
                    i = smaller_child
                h+=1
            else:
                return
            


    def enqueue(self, value):
        self.heap.append(value)
        self.reHeapUp(len(self.heap)-1)

    def dequeue(self):
        self.swap(len(self.heap)-1, 0)
        self.heap.pop()
        self.reheapDown(0)

    def display(self):
        for elements in self.heap:
            print(elements)

class Graph:
    def __init__(self):
        self.graph = {}
    
    def input_edge(self, from_node, to_node, cost):          
        if from_node in self.graph.keys:
            self.graph[from_node].append([to_node, cost])
        else:
            self.graph[from_node] = [to_node, cost]
        
    def display_graph(self):
        print(self.graph)


class A_star:
    def __init__(self, source, goal, input_graph, heuristic) -> None:
        self.source = source
        self.goal = goal
        self.graph = input_graph
        self.h_value = heuristic
        


        