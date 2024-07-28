def is_safe(vertex, graph, colours, colour):
    for neighbor in graph[vertex]:
        if colours[neighbor] == colour:
            return False
    return True

def graph_colouring(graph, colours, vertex, num_colours):
    if vertex == len(graph):
        return True

    for colour in range(1, num_colours + 1):
        if is_safe(vertex, graph, colours, colour):
            colours[vertex] = colour
            if graph_colouring(graph, colours, vertex + 1, num_colours):
                return True
            colours[vertex] = 0
    
    return False

def can_be_coloured(graph, num_colours):
    colours = [0] * len(graph)
    if graph_colouring(graph, colours, 0, num_colours):
        return colours
    else:
        return None

# Representing the graph as an adjacency list
graph = {
    0: [1, 2, 3, 4, 5],
    1: [0, 10, 7],
    2: [0, 6, 8],
    3: [0, 7, 9],
    4: [0, 8, 10],
    5: [0, 9, 6],
    6: [2, 5, 7, 10],
    7: [1, 3, 6, 8],
    8: [2, 4, 7, 9],
    9: [3, 5, 8, 10],
    10: [1, 4, 6, 9]
}

# Number of colours (Apricot, Brown, Cyan)
num_colours = 3

# Checking if the graph can be coloured

result = can_be_coloured(graph, num_colours)
if result:
    print("The graph can be coloured using", num_colours, "colours.")
    print("The colours for each vertex are:", result)
else:
    print("The graph cannot be coloured using", num_colours, "colours.")