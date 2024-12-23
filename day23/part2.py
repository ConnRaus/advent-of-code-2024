import networkx as nx 
# kinda cheating i guess, but i wanted to learn to use networkx
# after reading about others using it on r/adventofcode

def parseInput(filename):
    graph = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            c1, c2 = line.strip().split("-")
            graph.add_edge(c1, c2)
    return graph

def findLargestClique(graph):
    cliques = list(nx.find_cliques(graph))
    largestClique = max(cliques, key=len)
    return largestClique

graph = parseInput('input.txt')
largestClique = findLargestClique(graph)

password = ','.join(sorted(largestClique))
print(password)