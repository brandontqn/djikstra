# Initialize test data
test_values = [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]]
test_n = 5
test_start = (1,4)
test_goal = (3,2)

least_cost_path = []

# Helper functions
def left(start_loc, test_values):
    if(start_loc[0] != 0):
        return (start_loc[0]-1, start_loc[1], test_values[start_loc[0]-1][start_loc[1]])

def right(start_loc, test_values, n):
    if(start_loc[0] != n-1):
        return (start_loc[0]+1, start_loc[1], test_values[start_loc[0]+1][start_loc[1]])

def up(start_loc, test_values, n):
    if(start_loc[1] != n):
        return (start_loc[0], start_loc[1]+1, test_values[start_loc[0]][start_loc[1]+1])

def down(start_loc, test_values):
    if(start_loc[1] != 0):
        return (start_loc[0], start_loc[1]-1, test_values[start_loc[0]][start_loc[1]-1])

# Finds the least cost path from a given starting node to a given goal node
### possibly not shortest path in edge cases?
def path_find(n, start_loc, goal_loc, values, least_cost_path):
    # Reached goal location
    if(start_loc[0] == goal_loc[0] and start_loc[1] == goal_loc[1]):
        cost = 0
        for i in least_cost_path:
            cost += i[2]
            print("(" + repr(i[0]) + "," + repr(i[1]) + ") Cost:" + repr(i[2]))
        print("Total cost of path: " + repr(cost))
        print("Number of steps: " + repr(len(least_cost_path)))
    # If current node is one position away from goal node, move directly there
    elif(start_loc[0] == goal_loc[0] and abs(start_loc[1]-goal_loc[1])):
        if(start_loc[1] > goal_loc[1]):
            new_node = ((down(start_loc, test_values)[0]),down(start_loc, test_values)[1], down(start_loc, test_values)[2])
            least_cost_path.append(new_node)
            path_find(n, new_node, goal_loc, values, least_cost_path)
        else:
            new_node = ((up(start_loc, test_values, n)[0]), up(start_loc, test_values, n)[1], up(start_loc, test_values, n)[2])
            least_cost_path.append(new_node)
            path_find(n, new_node, goal_loc, values, least_cost_path)
    elif(start_loc[1] == goal_loc[1] and abs(start_loc[0]-goal_loc[0])):
        if(start_loc[0] > goal_loc[0]):
            new_node = ((left(start_loc, test_values)[0]),left(start_loc, test_values)[1], left(start_loc, test_values)[2])
            least_cost_path.append(new_node)
            path_find(n, new_node, goal_loc, values, least_cost_path)
        else:
            new_node = ((right(start_loc, test_values, n)[0]), right(start_loc, test_values, n)[1], right(start_loc, test_values, n)[2])
            least_cost_path.append(new_node)
            path_find(n, new_node, goal_loc, values, least_cost_path)
    # Start location is further (wrt x) from origin, we want to move left, reducing x-coordinate
    elif(start_loc[0] > goal_loc[0]):
        # Start location is further (wrt y) from origin, we want to move down, reducing y-coordinate
        if(start_loc[1] > goal_loc[1]):
            if(left(start_loc, test_values)[2] > down(start_loc, test_values)[2]):
                new_node = ((down(start_loc, test_values)[0]),down(start_loc, test_values)[1], down(start_loc, test_values)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
            else:
                new_node = ((left(start_loc, test_values)[0]),left(start_loc, test_values)[1], left(start_loc, test_values)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
        # Start location is closer (wrt y from origin, we want to move up, increasing y-coordinate)
        else:
            if(left(start_loc, test_values)[2] > up(start_loc, test_values, n)[2]):
                new_node = ((up(start_loc, test_values, n)[0]),up(start_loc, test_values, n)[1], up(start_loc, test_values, n)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
            else:
                new_node = ((left(start_loc, test_values)[0]),left(start_loc, test_values)[1], left(start_loc, test_values)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
    # Start location is closer (wrt x) to origin, we want to move right, increasing x-coordinate
    else:
        # Start location is further (wrt y) from origin, we want to move down, reducing y-coordinate
        if(start_loc[1] > goal_loc[1]):
            if(right(start_loc, test_values, n)[2] > down(start_loc, test_values)[2]):
                new_node = ((down(start_loc, test_values)[0]),down(start_loc, test_values)[1], down(start_loc, test_values)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
            else:
                new_node = ((right(start_loc, test_values, n)[0]),right(start_loc, test_values, n)[1], right(start_loc, test_values, n)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
        # Start location is closer (wrt y from origin, we want to move up, increasing y-coordinate)
        else:
            if(right(start_loc, test_values, n)[2] > up(start_loc, test_values, n)[2]):
                new_node = ((up(start_loc, test_values, n)[0]),up(start_loc, test_values, n)[1], up(start_loc, test_values, n)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)
            else:
                new_node = ((right(start_loc, test_values, n)[0]),right(start_loc, test_values, n)[1], right(start_loc, test_values, n)[2])
                # print("(" + repr(new_node[0]) + "," + repr(new_node[1]) + ") Cost:" + repr(new_node[2]))
                least_cost_path.append(new_node)
                path_find(n, new_node, goal_loc, values, least_cost_path)

path_find(test_n, test_start, test_goal, test_values, least_cost_path)
