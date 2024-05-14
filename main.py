import math
import ast
import distance

def main():
    '''
    Input state has to be in format of List 
    '''

    target = input("Please enter the target state(Default is Eight Puzzle): ")
    if not target:
        target = [1,2,3,4,5,6,7,8,0]
    else:
        target = ast.literal_eval(target)
    
    if (math.sqrt(len(target)).is_integer()) == False:
        print("Please Enter a Squared matrix in this puzzle problem: ")
        return 

    dim = int(math.sqrt(len(target)))
    
    initial = input("Please enter the initial state: ") 
    if not initial:
        print("initial state can't be empty")
        return
    else:
        initial = ast.literal_eval(initial)
        
    if (math.sqrt(len(initial)).is_integer() & (initial != "")) == False:
        print("Initial state should be in a suitable format and can't be empty")
        return
    if (dim != int(math.sqrt(len(initial)))):
        print("The dimension of the target state should be same as the initial state which is a squared matrix")
        return
    distance_name = input("Please enter the distance state: ") or "UCS"
    name_list = ['UCS','Misplaced','Manhatten']
    if distance_name not in name_list:
        print("distance name should be one of three UCS, Misplaced and Manhatten")
        return 
    a = distance.general_search(initial,target, distance_name)
    b = distance.path(a)
    for j in b:
        print("")
        for i in range(dim):
            print(j[i*dim:(i+1)*dim])
        print("")
    print("successful!")
    exit()
    
if __name__ == "__main__":
    main()