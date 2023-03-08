import math
class Minimax():
    def __init__(self, terminal_value, adj_list):
        self.terminal_value = terminal_value
        self.adj_list = adj_list
    def min_value(self, state):
        if state in self.terminal_value:
            return self.terminal_value[state]
        
        value = math.inf
        for node in self.adj_list[state]:
            value = min(value, self.max_value(node))
        return value
    
    def max_value(self, state):
        if state in self.terminal_value:
            return self.terminal_value[state]
        
        value = -math.inf
        for node in self.adj_list[state]:
            value = max(value, self.min_value(node))
        return value
# terminal_value = {
#             "D" : 8,
#             "E" : 2,
#             "F" : 5,
#             "G" : 6
#         }
terminal_value = {
            "D" : 8,
            "E" : 2,
            "H" : 7,
            "I" : 5,
            "G" : 6
        }
# adj_list = {
#             "A" : ["B", "C"],
#             "B" : ["D", "E"],
#             "C" : ["F", "G"]
#         }
adj_list = {
            "A" : ["B", "C"],
            "B" : ["D", "E"],
            "C" : ["F", "G"],
            "F" : ["H", "I"]
        }

tst1 = Minimax(terminal_value, adj_list)
print(tst1.max_value("A"))
