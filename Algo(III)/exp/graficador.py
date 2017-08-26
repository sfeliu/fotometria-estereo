import networkx as nx
import matplotlib.pyplot as plt
import sys
import subprocess
import matplotlib.backends.backend_pdf

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
    
    plt.subplot(1,2,gN)#.annotate('optimalidad: ' + nodos + 'tiempo: ' + elapsed, xy=(1, 1))

    nx.draw(G, pos, edges=edges, edge_color=colors,width=2)

def parseGrafos(entrada):
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

        grafos = [None] * sizes[1] + [None] * sizes[3]
        grafos[0] = g1
        grafos[1] = g2

    return grafos

def parseMCS(mcs):
    with open(mcs,'r') as result:

        #result = StringIO.StringIO(f)

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

        mcsSalida = [int(word) for word in second_line.split()] + [int(word) for word in second_line.split()] + [None] * sizes[1]
        mcsSalida[0] = g1map
        mcsSalida[1] = g2map
        mcsSalida[2] = aristasMCS

    return mcsSalida

def main(argv):
    salidaArchivo = argv[0]
    salidaArchivo = salidaArchivo[:-3]

    grafos = parseGrafos(argv[0])
    g1 = grafos[0]
    g2 = grafos[1]

    mcsSalida = parseMCS(argv[1])

    g1map = mcsSalida[0]
    g2map = mcsSalida[1]
    aristasMCS = mcsSalida[2]

    elapsed = argv[2]
    nodos = argv[3]
    aristas = argv[4]

    draw_graph(aristasMCS,g1,g1map,1)
    draw_graph(aristasMCS,g2,g2map,2)

    if (nodos > 0 or aristas > 0):
        plt.figure(1).suptitle('optimalidad: nodos' + nodos +'% aristas: ' + aristas + '%  -  tiempo: ' + elapsed, fontsize=12)
    else:
        plt.figure(1).suptitle('tiempo: ' + elapsed, fontsize=12)

    pdf = matplotlib.backends.backend_pdf.PdfPages(salidaArchivo+'.pdf')
    #for fig in range(1, plt.figure().number): ## will open an empty extra figure :(
    pdf.savefig( 1 )
    pdf.close()
    
    plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
