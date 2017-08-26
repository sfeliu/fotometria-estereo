import networkx as nx
import matplotlib.pyplot as plt
import sys
import subprocess
import StringIO

#dibuja los dos grafos, resaltando las aristas que pertenecen al MCS
#no dibuja los nodos de grado 0, dado que construye el grafo a partir de las aristas

def pertenece(edge,gmap,MCS):
    try:
        index0 = gmap.index(edge[0])
    except ValueError:
        return False

    try:
        index1 = gmap.index(edge[1])
    except ValueError:
        return False

    edgeMapped1 = (index0,index1)
    edgeMapped2 = (index1,index0)
    #print(str(edge)+" "+str(edgeMapped1))
    return (edgeMapped1 in MCS) or (edgeMapped2 in MCS)

def draw_graph(MCS,graph,gmap,gN):
    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        #si estan en el mcs
        if pertenece(edge,gmap,MCS):
            G.add_edge(edge[0], edge[1],color='red')
        else:
            G.add_edge(edge[0], edge[1],color='black')

    # draw graph
    pos = nx.shell_layout(G)

    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    
    plt.figure(gN)

    nx.draw(G, pos, edges=edges, edge_color=colors,width=2)


# draw example
if (len(sys.argv)-1 < 2) :
    print("uso: %s ./ejecutable input " % sys.argv[0])
    exit(1)

ejecutable = sys.argv[1]
entrada = sys.argv[2]

resultado = subprocess.check_output(ejecutable+" < "+entrada, shell=True)

result = StringIO.StringIO(resultado)

with open(entrada,'r') as f:

    first_line = f.readline().strip()
    sizes = [int(word) for word in first_line.split()]
    g1 = [None] * sizes[1]
    g2 = [None] * sizes[3]

    i = 0
    for line in f:
        if i < sizes[1]:
            g1[i] = tuple([int(word) for word in line.split()])
        else:
            g2[i-(sizes[1])] = tuple([int(word) for word in line.split()])
        i += 1

first_line = result.readline().strip()
sizes = [int(word) for word in first_line.split()]

second_line = result.readline().strip()
g1map = [int(word) for word in second_line.split()]

third_line = result.readline().strip()
g2map = [int(word) for word in third_line.split()]

aristasMCS = [None] * sizes[1]
i = 0
for line in result:
        aristasMCS[i] = tuple([int(word) for word in line.split()])
        i += 1
"""
print(g1)
print(g2)
print(g1map)
print(g2map)
print(aristasMCS)
"""
draw_graph(aristasMCS,g1,g1map,1)
draw_graph(aristasMCS,g2,g2map,2)
plt.show()