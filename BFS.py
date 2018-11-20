# sample graph implemented as a dictionary
import re


# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start, end):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start]= 0    # depth of start node is 0

    visited= [start]     # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be checked
    while queue:
       # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)

                if(neighbour == end):
                    print("##### found")
                    print(levels[node]+1)
                    continue
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
                # print(neighbour, ">>", levels[neighbour])

    # print(levels)

    return explored

if __name__ == "__main__":
    graph = dict()
    fname = './data/graph.txt'
    with open(fname) as f:
        content = f.readlines()

    for i in range(len(content)):
        line =  re.sub("\s+", ",", content[i].strip()).split(',')
        start = line[0].strip()
        end = line[1].strip()
        cost = int(line[2].strip())
        if start not in graph.keys():
            graph[start] = []
        if end not in graph.keys():
            graph[end] = []
        if end not in graph[start]:
            graph[start].append(end)
        
        if start not in graph[end]:
            graph[end].append(start)

    # print(graph)
    bfs_connected_component(graph, '52', '29')


# ans = bfs_connected_component(graph,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
# print(ans)