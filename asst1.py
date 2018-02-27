# Returns true if tuple is found in the List
def find_node(node, list):
    for index, item in enumerate(list):
        if(item[0] == node):
            return True, item, index
    return False, False, False

# Implements Djikstra's algorithm to find the least cost path from start_loc to goal_loc
def path_find(n, start_loc, goal_loc, values):
    # Decreasing node coordinates by 1 to match standard zero-index convention
    start_loc = (start_loc[0]-1,start_loc[1]-1)
    goal_loc = (goal_loc[0]-1,goal_loc[1]-1)

    # Tuples stored are of the form (current node, parent node, shortest known cost to get to current node)
    # Visited keeps tracks of which nodes have been visited
    # S keeps track of which nodes we know have the least possible cost from our start location
    visited = []
    S = [(start_loc, None, 0)]
    least_cost_path = []

    for node in S:
        # Check if we can expand LRUD without going out of range
        if(node[0][0] > 0):
            # Check if the node to the Left of current node has been visited
            left_node = (node[0][0]-1, node[0][1])
            # Only perform actions on LEFT node if it's not in S, (i.e. left node may potentially be updated with a lower cost)
            if(not find_node(left_node, S)[0]):
                if(find_node(left_node, visited)[0]):
                    # Compare the (cost of current node + immediate cost of LEFT node) to (the current total cost of LEFT node)
                    if(node[2]+values[left_node[1]][left_node[0]] < find_node(left_node, visited)[1][2]):
                        # Assign LEFT node cost of current node + immediate cost of LEFT node
                        i = find_node(left_node, visited)[2]
                        visited[i] = (visited[i][0], node[0], node[2]+values[left_node[1]][left_node[0]])
                else:
                    # LEFT node hasn't been visited yet, add it to visited list
                    visited.append((left_node, node[0], node[2]+values[left_node[1]][left_node[0]]))

        if(node[0][0] < n-1):
            right_node = (node[0][0]+1, node[0][1])
            if(not find_node(right_node, S)[0]):
                if(find_node(right_node, visited)[0]):
                    if(node[2]+values[right_node[1]][right_node[0]] < find_node(right_node, visited)[1][2]):
                        i = find_node(right_node, visited)[2]
                        visited[i] = (visited[i][0], node[0], node[2]+values[right_node[1]][right_node[0]])
                else:
                    visited.append((right_node, node[0], node[2]+values[right_node[1]][right_node[0]]))

        if(node[0][1] > 0):
            down_node = (node[0][0], node[0][1]-1)
            if(not find_node(down_node, S)[0]):
                if(find_node(down_node, visited)[0]):
                    if(node[2]+values[down_node[1]][down_node[0]] < find_node(down_node, visited)[1][2]):
                        i = find_node(down_node, visited)[2]
                        visited[i] = (visited[i][0], node[0], node[2]+values[down_node[1]][down_node[0]])
                else:
                    visited.append((down_node, node[0], node[2]+values[down_node[1]][down_node[0]]))

        if(node[0][1] < n-1):
            up_node = (node[0][0], node[0][1]+1)
            if(not find_node(up_node, S)[0]):
                if(find_node(up_node, visited)[0]):
                    if(node[2]+values[up_node[1]][up_node[0]] < find_node(up_node, visited)[1][2]):
                        i = find_node(up_node, visited)[2]
                        visited[i] = (visited[i][0], node[0], node[2]+values[up_node[1]][up_node[0]])
                else:
                    visited.append((up_node, node[0], node[2]+values[up_node[1]][up_node[0]]))

        # Adding the least cost node into set S
        if(visited != []):
            s_node = min(visited, key = lambda t: t[2])
            # Remove s_node from visited once it's been added into set S, we check this condition above
            S.append(s_node)
            visited.remove(s_node)

        # Once goal_loc is added into S, return the least_cost_path to goal_loc
        if(s_node[0] == goal_loc):
            curr_node = s_node #goal_loc
            while(curr_node[0] != start_loc):
                # Appending the node coordinates+1 to match our assignment criteria of starting at 1-index
                least_cost_path.append((curr_node[0][0]+1,curr_node[0][1]+1))
                # Set current node to it's parent node, iterating down the line till we get to start_loc
                curr_node = find_node(curr_node[1], S)[1]
                # Append the start_loc to least_cost_path
            least_cost_path.append((curr_node[0][0]+1,curr_node[0][1]+1))
            # Return the reversed list, [start_loc, path... , goal_loc]
            return least_cost_path[::-1]

# Initialize test data
# test_values = [[4,3,3,4,2], # row 1, Lowest
#                 [2,4,4,2,2],
#                 [3,4,5,3,2],
#                 [2,3,4,5,2],
#                 [4,3,3,2,4]] # row 5, Highest
# test_n = 5
# test_start = (1,1)
# test_goal = (5,4)

# correct answer should be:
# [ (1,1), (2,1), (3,1), (4,1), (4,2), (5,2), (5,3), (5,4) ]
# cost = 25
# My cost = 16

# path = path_find(test_n, test_start, test_goal, test_values)
# print(path)
