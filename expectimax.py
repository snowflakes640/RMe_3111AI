import math
class Expectimax():
    def __init__(self):
        self.terminal_value = {
        "E" : [3, 0.5],
        "F" : [12, 0.5],
        "G" : [8, 0.5],
        "H" : [2, 0.5],
        "I" : [4, 0.5],
        "J" : [6, 0.5]
        }
        self.adj_list = {
            "A" : ["B", "C", "D"],
            "B" : ["E", "F"],
            "C" : ["H", "G"],
            "D" : ["I", "J"]
        }
    
    
    def exp_value(self, state):
        total_value = 0
        
        if state in self.terminal_value:
            return self.terminal_value[state][0]    
        
        else:
            for node in self.adj_list[state]:
                value = self.max_value(node)* self.terminal_value[node][1]
                total_value += value
            return total_value



    def max_value(self, state):
        if state in self.terminal_value:
            return self.terminal_value[state][0]
        value = -math.inf
        for node in self.adj_list[state]:
            value = max(value, self.exp_value(node))
        return value


ai = Expectimax()

print(ai.max_value('A'))