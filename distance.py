import heapq
import copy
import math

class Node:
    """
    Define function to make node 
    State is the state of the puzzle which should be a list with different length depending on the puzzle
    gx, hx are the two distance metrics, gx is the cost from the inital state to the current state,
    hx is the distance from the current state to the goal state. fx is the sum of them.
    When we choose the front node, we choose the node with smallest fx. 
    """
    def __init__(self, state, parent=None, gx=0, hx=0):
        self.state = state
        self.parent = parent
        self.gx = gx
        self.hx = hx
        self.fx = gx + hx

    def __lt__(self, other):
        return self.fx < other.fx
        
    def __eq__(self, other):
        return self.state == other.state

def uniform_cost_search(start, goal):
    """
    The heuristic function of UCS is just 0 which is equivalent to the BFS
    """
    return 0

def misplaced_tile(start, goal):
    """
    The heuristic function of misplaced distance is the sum of different elements between the current state to the goal state
    """
    output = 0
    for i in range(len(start)):
        if (start[i]!=0) & (start[i] != goal[i]):
            output += 1
    return output 

def manhatten_distance(start, goal):
    """
    The heuristic function of manhatten distance is the sum of cost required from the different elements to the correct location in the goal. 
    """
    output = 0
    for i in range(len(start)):
        if (start[i]!=0) & (start[i] != goal[i]):
            output = output + abs(i//3 - goal.index(start[i])//3)+ abs(i%3 - goal.index(start[i])%3)
    return output 


def expand(node, dim, goal, function_name):
    """
    The expand function is used to expand the current node, is same as find the child node of the current node. 
    dim: which decide the type of the game you want to play. Like 8 puzzles the dim would be 3. 15 puzzles the dim would be 4
    function_name: the heuristic function would be used to store in the node. 
    """
    neighbors = []
    
    index = node.state.index(0)
    row = index//dim #transform the 1d list into 2d matrix, find out the row and col index of the NULL value. 
    col = index%dim
    dr = [[0, 1], [0, -1], [1, 0], [-1, 0]] # the set of the direction of the next step
    
    for i in dr:
        new_zero = [x + y for x, y in zip([row, col], i)]
        new_state = node.state.copy()
        if ((new_zero[0]>=0) & (new_zero[1]>=0) & (new_zero[0]<dim) & (new_zero[1]<dim)):#to decide whether the move is outof the cube
            new_state[dim*new_zero[0]+new_zero[1]] = 0
            new_state[index] = node.state[dim*new_zero[0]+new_zero[1]] #switch NULL value and next possible direction 
            neighbors.append(Node(new_state, parent = node, gx = node.gx+1, hx = function_name(new_state, goal))) #save the child node
            
    return neighbors
    
def general_search(start, goal, distance = "UCS"):
    """
    The main function used to do the serach
    Start is the initial state input by the user, which should be a n**2 length list 
    Goal is the target state input by the user, which should also be a n**2 length list 
    Distance: the type of the heuristci function, the value should be one of "UCS", "Misplaced", "Manhatten"
    """
    function_dict = {
        'UCS': uniform_cost_search,
        'Misplaced': misplaced_tile,
        'Manhatten': manhatten_distance
    }
    function_name = function_dict[distance]
    dim = int(math.sqrt(len(start)))
    visited = []
    leaf = []
    heapq.heappush(leaf, Node(start, hx = function_name(start, goal))) #Add the initial state to the leaf nodes list.
    goal_node = Node(goal)

    while leaf:
        current_node = heapq.heappop(leaf)#Pop the node with the shortest distance to the goal state based on the different heuristic function
        if current_node == goal_node:
            return current_node
        current_nodes = expand(current_node, dim, goal, function_name)
        for node in current_nodes:
            if node in visited:
                break
            heapq.heappush(leaf, node)
    return "Failure" #If the leaf nodes list is empty. Then return Failure
    
def path(node):
    output = []
    while node:
        output.append(node.state)
        node = node.parent
    output = output[::-1]
    return output

