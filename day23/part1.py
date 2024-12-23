from collections import defaultdict

def parseInput(filename):
    dictionary = defaultdict(set)
    with open(filename, 'r') as file:
        for line in file:
            c1, c2 = line.strip().split("-")
            dictionary[c1].add(c2)
            dictionary[c2].add(c1)
    return dictionary
        
graph = parseInput('input.txt')
triangles = set()
nodes = sorted(graph.keys())

# if node and a neighbor have a neighbor with intersection, its a triangle
for node in nodes:
    for neighbor in graph[node]:
        intersects = graph[node].intersection(graph[neighbor])
        for i in intersects:
            triangles.add(tuple(sorted((node, neighbor, i))))

# get rid of triangle with no t
validTriangles = []
for triangle in triangles:
    if any(node.startswith('t') for node in triangle):
        validTriangles.append(triangle)

print(len(validTriangles))