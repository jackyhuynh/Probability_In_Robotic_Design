import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    import numpy
    new_beliefs = []
    
    new_grid = numpy.asarray(beliefs) # Transform list to numpy to get the dimension   
    row = new_grid.shape[0] # get number of row
    col = new_grid.shape[1] # get number of columns
    
    beliefs = [] # clear belief
    for i in range(row):
        new_row=[]
        for j in range(col):
            new_row.append(1./(row*col))
        beliefs.append(new_row)
    
    
    for i in range(row):
        new_row=[]
        for j in range(col):
            hit = (color == grid[i][j])
            # print(hit)
            new_row.append(beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss))
          
        # Append the new row to the new belief array
        new_beliefs.append(new_row)
    
    # test 
    # print("test newbelief after 1st hit transformation")
    # print(new_beliefs)
    
    s = 0
    # Sum all the belief property 
    for i in range(row):
        for j in range(col):
            s += new_beliefs[i][j]
    
    # Create the new probability table
    for i in range(row):
        for j in range(col):
            new_beliefs[i][j]=new_beliefs[i][j]/s

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    #print(height,width)
    
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    
    #print(new_G)
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            
            print("cell value ", cell , " ,j value is:" , j)
            new_i = (i + dy ) % height
            print("new i value ", new_i , " ,i value is:" , i)
            new_j = (j + dx ) % width
            print("new j value ", new_j , " ,j value is:" , j)
            pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
            
            
    return blur(new_G, blurring)