
import math

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

    def __gt__(self,other):
        return self.priority > other.priority
    def __lt__(self,other):
        return self.priority < other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def __str__(self):
        return self.data

class min_heap:


    def __init__(self):
        self.heap = []


    def parent(self,i):
        if self.is_empty !=0:
            return (i-1)//2
        return None


    def left_child(self,i):
        index = int(2*i+1)
        if index < len(self.heap):
            return index
        else:
            return -1

    def right_child(self,i):
        index = int(2*i+2)
        if index < len(self.heap):
            return index
        else:
            return -1
    def height(self):
        N = len(self.heap)
        h = math.log(N+1,2)
        return h
    def swap(self,a,b):
        self.heap[a],self.heap[b] = self.heap[b],self.heap[a]
    def is_empty(self):
        if len(self.heap) == 0:
            return 1
        return 0
    def reheap_up(self):
        if self.is_empty != 0:
            index = len(self.heap) - 1
            index_parent = self.parent(index)
            while self.heap[index_parent] > self.heap[index]:
                self.swap(index,index_parent)
                index = index_parent
                index_parent = self.parent(index)
            return
        else:
            return  

    def reheap_down(self):
        if self.is_empty() !=0 :
            h = 1
            max_h= self.height()
            index = 0
            highest_index = len(self.heap)-1
            while h<max_h:
                left_child_index = self.left_child(index)
                right_child_index = self.right_child(index)
                if left_child_index != -1: #there is at least one child
                    if left_child_index == highest_index: #this is the only child 
                        smaller_child_index = left_child_index
                    else: #there is a right child
                        if self.heap[right_child_index] < self.heap[left_child_index]: # checking the smaller child
                            smaller_child_index = right_child_index
                        else:
                            smaller_child_index = left_child_index
                
                    if self.heap[index] > self.heap[smaller_child_index]:
                        self.swap(index,smaller_child_index)
                        index = smaller_child_index
                    else:
                        break
            
                else:
                    break
            return
        else:
            return    
    def enqueue(self,node): #this is the node which has data and f
        self.heap.append(node)
        self.reheap_up()
    
    def dequeue(self):
        self.swap(0,len(self.heap)-1)
        hehe = self.heap.pop()
        self.reheap_down()
        return hehe.data

    def display(self):
        for i in self.heap:
            print(i)

class  Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,x,y,g): #using every edge to update adjacency list
        arr = [y,g]
        if x in self.adj_list.keys():
            self.adj_list[x].append(arr)
        else:
            self.adj_list[x] = [arr]

    def display_adj_list(self):
        print(self.adj_list)  

class A_search:
    def __init__(self,source,goal,graph,h):
        self.source = source
        self.goal = goal
        self.graph = graph
        self.h = h
        visited = []
        path = []
        parent = {}
        parent[self.source] = None
        pq = min_heap()
        pq.enqueue(Node(self.source,self.h[self.source]))
        cost_from_source = {}
        for i in self.h.keys():
            if i == self.source:
                cost_from_source[i] = 0
            else:
                cost_from_source[i] = math.inf
    


        while pq.is_empty() != 1:
            temp = pq.dequeue()
            #print(temp)
            if temp == self.goal:
                break
            #TwT
            visited.append(temp)
            neighbours = self.graph.adj_list[temp]
            for neighbour in neighbours:
                name,weight = neighbour
                cost = cost_from_source[name]
                if cost > weight + cost_from_source[temp]:
                    cost_from_source[name] = weight + cost_from_source[temp]
                    pq.enqueue(Node(name,cost_from_source[name]+self.h[name]))
                    parent[name] = temp
        current = self.goal
        #print(parent)
        while parent[current] != None:
            path.append(parent[current])
            current = parent[current]

        path.reverse()
        path.append(self.goal)
        print(path)


if __name__ == '__main__':
    
    #graph
    graph = Graph()
    graph.add_edge('S','A',2)
    graph.add_edge('S','B',4)
    graph.add_edge('A','B',1)
    graph.add_edge('A','C',4)
    graph.add_edge('B','C',2)
    graph.add_edge('B','G',6)
    graph.add_edge('C','G',3)
    #graph.display_adj_list()

    #heuristic functions
    h1 = {'S':8,'A':3,'B':7,'C':2,'G':0}
    h2 = {'S':7,'A':4,'B':5,'C':2,'G':0}
    a_star1 = A_search('S','G',graph,h1)
    a_star2 = A_search('S','G',graph,h2)
    
    





    
heap1 = min_heap()
heap1.enqueue(1)
heap1.enqueue(5)
heap1.enqueue(3)
heap1.enqueue(6)
heap1.enqueue(9)
heap1.enqueue(8)

#heap1.reHeapUp(5)
heap1.display()



















# class priority_queue:
#     def __init__(self):
#         self.queue = []
#     def add(self,node):
#         if len(self.queue) == 0:
#             self.queue.append(node)
#         else:
#             added = 0
#             for i in range(0,len(self.queue)):
#                 if node.f <= self.queue[i].f:
#                     self.queue.insert(i,node)
#                     added = 1
#             if added == 0:
#                 self.queue.append(node)
        
#     def display(self):
#         for i in range(0,len(self.queue)):
#             print(self.queue[i].data)
#     def remove(self):
#         data_value = self.queue[0].data
#         f_value = self.queue[0].f
#         self.queue.pop(0)
#         return data_value
    
#     def length(self):
#         return len(self.queue)
        