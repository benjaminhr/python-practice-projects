#A dictionary named graph, with lists inside
#Integers renamed as strings
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

#Function for BFS
def breadth_first_search(graph, start, end):
    #Maintain a queue of paths
    queue = []
    #Push the first path into the queue
    queue.append([start])
    while queue:
        #Get the first path from the queue
        path = queue.pop(0)
        #Get the last node from the path
        node = path[-1]
        #If path found return the path to that node
        if node == end:
            return path
        #Calculates for all adjacent nodes
        #Construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

#Returns shortest path from node '1' to node '3'
print breadth_first_search(graph, '1', '7')
