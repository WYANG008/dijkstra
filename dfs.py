import re
level = 3
if __name__ == "__main__":
    graph = dict()
    costMap = dict()
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

        if start not in costMap.keys():
            costMap[start] = dict()
        if end not in costMap.keys():
            costMap[end] = dict()
        costMap[start][end] = cost
        costMap[end][start] = cost

    visitedNode = []
    for i in range(len(graph['52'])):
        level1Node = graph['52'][i]
        visitedNode.append(level1Node)
        for j in range(len(graph[level1Node])):
            level2Node = graph[level1Node][j]
            if(level2Node not in visitedNode):
                visitedNode.append(level2Node)
                for k in range(len(graph[level2Node])):
                    level3Node = graph[level2Node][k]
                    if(level3Node == '29'):
                        print('found a path', '52', level1Node, level2Node, level3Node)
    # for(i in range(len(3))):
    #     print('level ' + i)

