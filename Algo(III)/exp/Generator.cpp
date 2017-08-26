    #include <iostream>
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>   
    #include <list>
    #include <map>
    #include <string>
    #include <sstream>
    #include <vector>
    #include <math.h>       /* log2 */

    using namespace std;

    typedef pair<int,int> edge;
    typedef list<edge> Graph;

    /*
    For this module, Graphs will be represented as a list of integer pairs. In this representation, edges can be repeated 
    with no further checking from the Graph. It may also contain an edge as (a,b) and (b,a) in the same list.
    Note that in this representation, nodes are defined only if the appear used by an edge.
    */


/*
    INTERFACE:
    
    -string input conversion

        getinputStringFromGraphs

    -Graph generation
    
        GeneratePathGraph   

        GenerateCompleteGraphOfSize

        GenerateStar
        GenerateCentipede
        
        GenerateRandomlyConnectedGraph
        GenerateListBasedRandomlyConnectedGraph

        GenerateTree

        GenerateGraphFromMaxClique
        GenerateGraphFromMinClique

        GenerateComplementGraphPair

    EXAMPLE:
    
    Graph* graph1 = GenerateCompleteGraphOfSize(5);
    Graph* graph2 = GeneratePathGraph(10);
    string inputForYourMethods  = getinputStringFromGraphs(graph1,graph2);
    

*/


    /*=====================================================================================*/
    /*=====================================================================================*/
    /*
        Test Function. Prints in the standard output the content of a density map.
        A density map relates each node of a graph with it's density.
    */
    void printDensityMap(map<int,int>* densityMap){
        for (map<int,int>::iterator it=densityMap->begin(); it!=densityMap->end(); ++it){
            std::cout <<"Node#"<< it->first << ": " << it->second << '\n';
        }
    }

    /*
        Test Function. Prints in the standard output the content of a graph.
    */
    void printGraph(Graph* graph){
        for (Graph::iterator it=graph->begin(); it!=graph->end(); ++it){
            std::cout <<"("<< it->first << "," << it->second <<")"<< '\n';
        }    
    }

    /*
        Test Function. Prints in the standard output the content of a graph in another format.
    */
    void printGraph2(Graph* graph){
        cout<<endl;
        cout<<(graph->size()+1)<<":";
        for (Graph::iterator it=graph->begin(); it!=graph->end(); ++it){
            std::cout << (it->first+1) << "-" << (it->second+1) <<",";
        }    
    }

    /*
        Returns true only if a given graph contains an edge
        that uses both given nodes.
    */
    bool containsEdge(Graph* graph, int node1 , int node2){
        for (Graph::iterator it=graph->begin(); it!=graph->end(); ++it){
            if((it->first == node1) &&  (it->second == node2 ) || (it->second == node1) &&  (it->first == node2 ) ){
                return true;
            }
        }
        return false;
    }


    /*
        Given a graph, it returns a string with the input format for the exercises
    */
    string getinputStringFromGraphs(Graph* firstGraph, Graph* secondGraph){
        // Get max node of first Graph (amount of nodes)
        int maxNode1 =0;
        for (Graph::iterator it=firstGraph->begin(); it!=firstGraph->end(); ++it){
            if(it->first > maxNode1){
                maxNode1 = it->first;
            }
            if(it->second > maxNode1){
                maxNode1 = it->second;
            }
        }

        // Get max node of second Graph (amount of nodes)
        int maxNode2 =0;
        for (Graph::iterator it=secondGraph->begin(); it!=secondGraph->end(); ++it){
            if(it->first > maxNode2){
                maxNode2 = it->first;
            }
            if(it->second > maxNode2){
                maxNode2 = it->second;
            }
        }

        maxNode1++;
        maxNode2++;
        
        //create a stream to store result
        stringstream stream;
        
        //first line should contain amount of nodes and edges of each graph
        stream<<""<<(maxNode1)<<" "<<(firstGraph->size())<<" "<<(maxNode2)<<" "<<(secondGraph->size())<<"\n";
        
        //next, each edge should be printed (one per line)
        for (Graph::iterator it=firstGraph->begin(); it!=firstGraph->end(); ++it){
            stream<<""<<(it->first)<<" "<<(it->second)<<"\n";
        }
        
        for (Graph::iterator it=secondGraph->begin(); it!=secondGraph->end(); ++it){
            stream<<""<<(it->first)<<" "<<(it->second)<<"\n";
        }
        return stream.str();
    }

    /*=====================================================================================*/
    /*=====================================================================================*/
    /*
        Given an amount of nodes and a probability value, it builds a graph where the 
        probability of two nodes being connected is given by this value
    */
    Graph* GenerateRandomlyConnectedGraph(int amountOfNodes, int interconnectionProbability){
        //Initializations
        Graph* result = new Graph();
        srand (time(NULL));
        
        for(int i = 0; i<amountOfNodes;i++){
            for(int j = i+1; j<amountOfNodes; j++){
                //each iteration a call is made (between 0 and 100)
                //if value is smaller than probability, the connection is made
                int call = rand() % 100;
                if(call<interconnectionProbability){
                    result->push_back(make_pair(i,j));
                }
            }
        }
        
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/
    /*
        Generates a complete graph of given size where all nodes are connected
    */
    Graph* GenerateCompleteGraphOfSize(int amountOfNodes){
        Graph* result = new Graph();
        for(int i = 0; i<amountOfNodes;i++){
            for(int j = i+1; j<amountOfNodes; j++){
                result->push_back(make_pair(i,j));
            }
        }
        return result;
    }

    /*=====================================================================================*/
    /*=====================================================================================*/
    void randomlyFillGraph(Graph* graph, int graphSize,int nodesToAdd, int edgesToAdd){
        srand (time(NULL));

    //first add all nodes with 1 edge. finally fill randomlly:


        int lastAddedNode = graphSize;
        while(lastAddedNode < graphSize + nodesToAdd){
            int node1 = (lastAddedNode+1);
            int node2 = (rand() % lastAddedNode);
            graph->push_back(make_pair(node1,node2));
            lastAddedNode++;
            edgesToAdd--;
        }

        int attempts = 0;
        while(edgesToAdd>0){

            int firstNode = (rand() % (graphSize + nodesToAdd-2)); 
            int secondNode =(rand() % (graphSize + nodesToAdd-2)); 
            if((firstNode != secondNode) && (!containsEdge(graph,firstNode,secondNode)) ){
                graph->push_back(make_pair(firstNode,secondNode));
                edgesToAdd--;
                attempts = 0;
            }else{
                attempts++;
            }
            if(attempts > 2*(graphSize+nodesToAdd) ){
                break;
            }

        }
    }

/*
    Generates a graph where it ensures that it's clique has at least a size of minCliqueSize.
*/
    Graph* GenerateGraphFromMinClique(int amountOfNodes, int amountOfEdges, int minCliqueSize){
        
        //    First we generate clique with size ´minCliqueSize´
        Graph* result = GenerateCompleteGraphOfSize(minCliqueSize);

        /*
        Now that we have a complete graph with ´minCliqueSize´ size, we will extend it
        by randomly adding nodes to it until we complete the desired total size
        */

        int nodesToAdd = amountOfNodes - minCliqueSize; 
        //amount of nodes that i have to add to reach a solution with 'amountOfNodes' nodes
        
        randomlyFillGraph(result,minCliqueSize,nodesToAdd,amountOfEdges-(minCliqueSize*(minCliqueSize-1)/2));
        
        //cout<<result->size()<<":";
        
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/

/*
    Fills the given map with the density of each node of the graph
*/
    void registerNodeDensity(Graph* graph, map<int,int>* densityMap){
        Graph::const_iterator iterator;
        for ( iterator = graph->begin( ) ; iterator != graph->end( ) ; iterator++ ){
            
            //if first node already in map, increase value. If not, initialize it
            if(densityMap->find(iterator->first) != densityMap->end()){
                (*densityMap)[iterator->first] = ((*densityMap)[iterator->first])+1;
                
            }else{
                (*densityMap)[iterator->first] = 1;
            }

            //if second node already in map, increase value. If not, initialize it
            if(densityMap->find(iterator->second) != densityMap->end()){
                (*densityMap)[iterator->second] = ((*densityMap)[iterator->second])+1;
            }else{
                (*densityMap)[iterator->second] = 1;
            }
        }
    }
    
/*
    Given a graph, it adds the given amount of nodes. Then it starts connecting all nodes, making
    sure that no node suprasses the density limit. The density map is used for this
*/
    void FillGraphWithDensityLimit(Graph* graph, int graphSize,int nodesToAdd, int edgesToAdd,int densityLimit,map<int,int>* densityMap){
        srand (time(NULL));

    //first add all nodes by connecting them with existing nodes
        int lastAddedNode = graphSize;
        while(lastAddedNode < graphSize + nodesToAdd){
            
            //add new edge with new node
            int node1 = (lastAddedNode+1); //new node
            int node2 = (rand() % graphSize); // some existing node
            graph->push_back(make_pair(node1,node2));

            //update density map
            (*densityMap)[node1] = 1;
            (*densityMap)[node2] = (*densityMap)[node2]+1;
            lastAddedNode++;
            edgesToAdd--;
        }

    //Now the remaining amount of edges need to be added. for this a random pair of nodes is 
    // chosen. The new edge is added only if the corresponding densities are ok.

    // Because this is random, there's a chance that all densities are saturated before total
    // amount of edges are added. The algorythm has a fixed amount of failure attempts.
    // If this limit is met, the iteration stops.
        int attempts = 0;
        while(edgesToAdd>0){

            int firstNode = (rand() % (nodesToAdd))+graphSize-1; 
            int secondNode =(rand() % (nodesToAdd))+graphSize-1; 
            if((firstNode != secondNode) && (!containsEdge(graph,firstNode,secondNode)) && ((*densityMap)[firstNode]<densityLimit) && ((*densityMap)[secondNode]<densityLimit) ){
                graph->push_back(make_pair(firstNode,secondNode));
                (*densityMap)[firstNode] = (*densityMap)[firstNode]+1;
                (*densityMap)[secondNode] = (*densityMap)[secondNode]+1;
                edgesToAdd--;
                attempts = 0;
            }else{
                attempts++;
            }
            if(attempts > 2*(graphSize+nodesToAdd) ){
                break;
            }

        }
    }

/*
    Generates a graph whith a fixed max clique. This is achieved by adding the clique 
    and completing the required amount of nodes and edges ensuring that no node has 
    a density higher than the clique size -1. This way a bigger clique can never be formed.
*/    
    Graph* GenerateGraphFromMaxClique(int amountOfNodes, int amountOfEdges, int maxCliqueSize){
        
        //    First we generate clique with size ´minCliqueSize´
        Graph* result = GenerateCompleteGraphOfSize(maxCliqueSize);

        map<int,int>* densityMap = new map<int,int>();
        registerNodeDensity(result,densityMap);


        /*
        Now that we have a complete graph with ´minCliqueSize´ size, we will extend it
        by randomly adding nodes to it until we complete the desited total size
        */

        int nodesToAdd = amountOfNodes - maxCliqueSize; 
        //(amount of nodes that need to be added to reach a solution with 'amountOfNodes' nodes
        
        FillGraphWithDensityLimit(result,maxCliqueSize,nodesToAdd,amountOfEdges-(maxCliqueSize*(maxCliqueSize-1)/2),(maxCliqueSize-1),densityMap);

        return result;
    }

    /*=====================================================================================*/
    /*=====================================================================================*/
/*
    Simply generates a path of given length
*/
    Graph* GeneratePathGraph(int length){
        Graph* result = new Graph();
        for(int i = 0; i<length;i++){
            result->push_back(make_pair(i,i+1));
        }
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/
/*
    For the following functions, a struct must be used to store additional information 
    about a tree graph: It's root node and the last used node (highest in number)
*/
    struct graphStruct{
        Graph* graph;
        int rootNode;
        int lastNode;
    };

/*
    These functions adds all the nodes of the second tree to the first one 
    ( node numbers of the second graph are modified when added to the first
    one to ensure uniqueness)
*/
    void fuseGraphs(graphStruct graphstruct1,graphStruct graphstruct2){
        
        for (Graph::iterator it = graphstruct2.graph->begin(); it!=graphstruct2.graph->end(); ++it){
            graphstruct1.graph->push_back(
                make_pair(  (it->first+graphstruct1.lastNode) ,   (it->second+graphstruct1.lastNode) )
                );
        }

    }

/*
    Generates a tree with one level of a given amount of nodes
*/
    graphStruct generateOneLevelTree(int amountOfNodes){
        
        //Generate graph
        Graph* graph = new Graph();
        for(int i = 0; i<amountOfNodes;i++){
            graph->push_back(  make_pair(0 , i+1 ) );
        }

        //fill structure
        graphStruct resultStruct;
        resultStruct.graph = graph;
        resultStruct.rootNode = 0;
        resultStruct.lastNode = amountOfNodes+1;

        return resultStruct;
    }

/*
*/
    graphStruct generateTreeStruct(int amountOfLevels, int nodesPerLevel){
        srand (time(NULL));

        //start with a one-leveled tree
        int amountOfNodes = nodesPerLevel;
        graphStruct resultStruct = generateOneLevelTree(amountOfNodes);
        int level = 1;

        // until the required amount of levels is met, 
        // the tree will grow by one level each iteration
        int nodesForThisLevel;
        while(level <amountOfLevels){

            //set the amount of nodes for the new level
            nodesForThisLevel = nodesPerLevel;
            
            //add a new root to the tree and update structure
            int newRoot = resultStruct.lastNode;
            resultStruct.graph->push_back(  make_pair(newRoot , resultStruct.rootNode ) );
            resultStruct.rootNode = newRoot;
            resultStruct.lastNode = resultStruct.lastNode+1;
            
            // generate new subtrees and link them to the new root
            for(int i = 0;i<nodesForThisLevel;i++){

                //generate new tree
                graphStruct tmpStruct = generateTreeStruct(level,nodesPerLevel);

                //add it to the result tree
                fuseGraphs(resultStruct,tmpStruct);

                //link with the root
                resultStruct.graph->push_back(make_pair(resultStruct.rootNode,(tmpStruct.rootNode+resultStruct.lastNode)));
                
                //update structure
                resultStruct.lastNode = resultStruct.lastNode + tmpStruct.lastNode;
                
            }
            level++;
        }
        
        return resultStruct;    
    }


    Graph* GenerateTree(Graph* result, int root, int amountOfNodes){
        if(2*root+1<amountOfNodes){
        result->push_back(  make_pair(root , 2*root+1));
        GenerateTree(result,2*root+1,amountOfNodes);
        }
        if(2*root+2<amountOfNodes){
        result->push_back(  make_pair(root , 2*root+2));
        GenerateTree(result,2*root+2,amountOfNodes);
        }
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/
/*
    Generate a star graph (this is equivalent to a one level tree)
*/
    Graph* GenerateStar(int density){
        Graph* result = new Graph();

        for(int i = 0; i<density;i++){
            result->push_back(make_pair(0,i+1));
        }
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/

/*
    Given the last node used in a raph, it adds a star graph to it
*/
    void addStar(int nodeCounter,int nodesToAdd,Graph* graph){
        
        for(int i = 0; i<nodesToAdd;i++){
            graph->push_back(make_pair(nodeCounter,nodeCounter+i+1));
        }
    }

/*
    Generates a graph of 'length' star graphs with a random density each
*/
    Graph* GenerateCentipede(int length,int Density){
        int nodeCounter = 0;
        Graph* result = new Graph();
        
        int nodesToAdd = Density;
        addStar(nodeCounter,nodesToAdd,result);

        for(int i = 1; i< length;i++){
        //    result->push_back(make_pair(nodeCounter,nodeCounter+nodesToAdd+1));
            nodeCounter += nodesToAdd+1 ;
            nodesToAdd = Density;
            addStar(nodeCounter,nodesToAdd,result);
        }
        return result;
    }

    Graph* GenerateCentipedeUnidos(int length,int Density){
        int nodeCounter = 0;
        Graph* result = new Graph();
        
        int nodesToAdd = Density;
        addStar(nodeCounter,nodesToAdd,result);

        for(int i = 1; i< length;i++){
            result->push_back(make_pair(nodeCounter,nodeCounter+nodesToAdd+1));
            nodeCounter += nodesToAdd+1 ;
            nodesToAdd = Density;
            addStar(nodeCounter,nodesToAdd,result);
        }
        return result;
    }
    /*=====================================================================================*/
    /*=====================================================================================*/
    /*
        Similar to generateRandomlyConnectedGraph, but instead of recieving one probability
        value, it recieves a list of values from wich randomly chooses each time. This rsults
        in a 'more random' graph.
    */
    Graph* GenerateListBasedRandomlyConnectedGraph(int amountOfNodes, int interconnectionProbabilities[],int arraySize){
        //Initializations
        Graph* result = new Graph();
        srand (time(NULL));
        
        for(int i = 0; i<amountOfNodes;i++){
            for(int j = i+1; j<amountOfNodes; j++){
                int call = rand() % 100;
                int interconnectionProbability = interconnectionProbabilities[rand()%arraySize];
                if(call<interconnectionProbability){
                    result->push_back(make_pair(i,j));
                }
            }
        }
        
        return result;
    }


    /*=====================================================================================*/
    /*=====================================================================================*/
/*
    Splits a complete graph of 'amountOfNodes' nodes in two graphs. 
    Returns a pair with a pointer to each graph.
*/
    pair<Graph*,Graph*> GenerateComplementGraphPair(int amountOfNodes){
        //Initializations
        Graph* firstGraph = new Graph();
        Graph* secondGraph = new Graph();
        pair<Graph*,Graph*> result;
        srand (time(NULL));
        
        for(int i = 0; i<amountOfNodes;i++){
            for(int j = i+1; j<amountOfNodes; j++){
                //each iteration a call is made (between 0 and 100)
                //if value is odd it is added to one graph.
                //otherwise it is added to the other
                int call = rand() % 100;
                if(call%2==1){
                    firstGraph->push_back(make_pair(i,j));
                }else{
                    secondGraph->push_back(make_pair(i,j));
                }
            }
        }

        //Add graphs to the result
        result.first = firstGraph;
        result.second = secondGraph;

        //The union of resulting graphs will be the complete graph corresponding
        //to 'amountOfNodes'.
        return result;
    }

    void generateBaseCoGraphZero(graphStruct& result, int amountOfNodes){
    
            result.lastNode = amountOfNodes;
            result.rootNode = 0;
            result.graph = new Graph();

    }

    void generateBaseCoGraphOne(graphStruct& result, int amountOfNodes){

        result.lastNode = amountOfNodes;
        result.rootNode = 0;
        result.graph = new Graph();

        if(amountOfNodes>1 ){
            result.graph->push_back(make_pair(amountOfNodes-2,amountOfNodes-1));
        }

    }

    void generateBaseCoGraphTwo(graphStruct& result,int amountOfNodes){
         srand (time(NULL));
         result.lastNode = amountOfNodes;
         result.rootNode = 0;
         result.graph = new Graph();

         if(amountOfNodes > 2){
            
            int call = rand() % 100;
            if((call%2==1) || (amountOfNodes==3) ){
                result.graph->push_back(make_pair(amountOfNodes-2,amountOfNodes-1));
                result.graph->push_back(make_pair(amountOfNodes-3,amountOfNodes-1));
            }else{
                result.graph->push_back(make_pair(0,1));
                result.graph->push_back(make_pair(2,3));
            }
        }

    }

    void generateBaseCoGraphThree(graphStruct& result,int amountOfNodes){
        srand (time(NULL));
        result.lastNode = amountOfNodes;
        result.rootNode = 0;
        result.graph = new Graph();

        if(amountOfNodes > 2){
            
            int call = rand() % 100;
            if((call%2==1) || (amountOfNodes==3) ){
                result.graph->push_back(make_pair(0,1));
                result.graph->push_back(make_pair(0,2));
                result.graph->push_back(make_pair(1,2));
            }else{
               result.graph->push_back(make_pair(0,1));
               result.graph->push_back(make_pair(0,2));
               result.graph->push_back(make_pair(0,3));
            }
        }

    }

    void generateBaseCoGraphFour(graphStruct& result,int amountOfNodes){
            srand (time(NULL));
            result.lastNode = amountOfNodes;
            result.rootNode = 0;
            result.graph = new Graph();

            if(amountOfNodes > 3){

                int call = rand() % 100;
                if(call%2==0){
                    result.graph->push_back(make_pair(0,1));
                    result.graph->push_back(make_pair(0,2));
                    result.graph->push_back(make_pair(0,3));
                    result.graph->push_back(make_pair(1,3));
                }else{
                    if(call%2==1){
                        result.graph->push_back(make_pair(0,1));
                        result.graph->push_back(make_pair(0,2));
                        result.graph->push_back(make_pair(3,1));
                        result.graph->push_back(make_pair(3,2));
                    }else{
                        result.graph->push_back(make_pair(0,1));
                        result.graph->push_back(make_pair(0,2));
                        result.graph->push_back(make_pair(0,3));
                        result.graph->push_back(make_pair(3,2));
                    }
                }
             }

    }

    void generateBaseCoGraph(graphStruct& result, int amountOfNodes,int amountOfEdges){

        result.lastNode = -1;
        result.rootNode = -1;
        result.graph = 0;
        switch(amountOfEdges){
            case 0:
                generateBaseCoGraphZero(result, amountOfNodes);
            break;

            case 1:
                generateBaseCoGraphOne(result, amountOfNodes);
            break;

            case 2:
                generateBaseCoGraphTwo(result, amountOfNodes);
            break;

            case 3:
                generateBaseCoGraphThree(result, amountOfNodes);
            break;

            case 4:
                generateBaseCoGraphFour(result, amountOfNodes);
            break;
        }
    }
    /*=====================================================================================*/
    /*=====================================================================================*/

    void addGraphs(graphStruct& graphstruct1, graphStruct& graphstruct2){

        //connect all nodes of the first graph with all nodes of second

        for(int i = 0; i<graphstruct1.lastNode; i++){
            for(int j = 0; j<graphstruct2.lastNode; j++){
                graphstruct1.graph->push_back(make_pair(i ,graphstruct1.lastNode+j ));
            }
        }

        //add all edges of second graph
        for (Graph::iterator it = graphstruct2.graph->begin(); it!=graphstruct2.graph->end(); ++it){
            graphstruct1.graph->push_back(
                make_pair(  (it->first+graphstruct1.lastNode) , (it->second+graphstruct1.lastNode) )
            );
        }

        //adjust last node
        graphstruct1.lastNode+= graphstruct2.lastNode;
    }

    void complementGraph(graphStruct& graphstruct1 ){
        Graph* newList = new Graph();
        for(int i = 0; i< graphstruct1.lastNode;i++){
            for(int j = i+1; j< graphstruct1.lastNode;j++){
                if(!containsEdge(graphstruct1.graph,i,j)){
                    newList->push_back(make_pair(i ,j ));
                }
            }
        }
        delete graphstruct1.graph;
        graphstruct1.graph = newList;
    }

   graphStruct GenerateCoGraph(int amountOfNodes, int amountOfEdges){
        
        graphStruct gs;

        if(amountOfEdges < 5){
            
            gs.lastNode = -1;
            gs.graph = new Graph();

            generateBaseCoGraph(gs,amountOfNodes,amountOfEdges);

            return gs;

        }else{
            srand (time(NULL));
            int call;
            int edges = 0;
            int nodes = 0;
            int edgesToCreate = (rand() % 5)+1;
            int nodesToCreate = 4*edgesToCreate;
            
            generateBaseCoGraph(gs,nodesToCreate,edgesToCreate);
            edges = gs.graph->size();
            nodes = gs.lastNode;

            cout<<"HERE"<<endl;
            
            while((edges < amountOfEdges) && (nodes < amountOfNodes)){
                edgesToCreate = (rand() % 5)+1;
                nodesToCreate = 4*edges;

                graphStruct gsConstruct;
                generateBaseCoGraph(gsConstruct,nodesToCreate,edgesToCreate);

                call = rand() % 100;

                if((call % 2) == 1){
                    fuseGraphs(gs,gsConstruct);
                    cout<<"Union"<<endl;
                }else{
                    addGraphs(gs,gsConstruct);
                    cout<<"Adition"<<endl;
                }
                
                call = rand() % 100;
                if((call % 4) == 0){
                    complementGraph(gs);
                    cout<<"Complement"<<endl;
                }
                
                cout<<"HERE2"<<endl;
                
                edges = gs.graph->size();
                nodes = gs.lastNode;
                cout<<edges<<"|"<<amountOfEdges<<"        "<<nodes<<"|"<<amountOfNodes<<endl;
            }
            return gs;
        }
        
    }

    /*=====================================================================================*/
    /*=====================================================================================*/

    /*=====================================================================================*/
    /*=====================================================================================*/


int posicion(const vector<int>& V, int i){
    if(V.size() == 0) return 1;
    int p;
    for (p = 0; p < V.size(); ++p){
        if (i == V[p]) return p;
    }
    return p;
}

Graph* bipartito(int n, int aristas){//nodos debe ser par
    Graph* result = new Graph();
    srand (time(NULL));
    vector<vector<int> > agregados(n/2);
    while(aristas > 0){
        for (int i = 0; i < n/2; ++i){
            int prob = rand() % 2;
            if(prob==0){
                int vecino = n/2 + (rand() % n/2);
                if(posicion(agregados[i],vecino) >= agregados[i].size()){
                    aristas--;
                    result->push_back(  make_pair(i,vecino) );
                    agregados[i].push_back(vecino);
                }
            }
        }
    }
    return result;
}


    /*=====================================================================================*/
    /*=====================================================================================*/



int main(int argc, char const *argv[])
{

    /*    EJEMPLO COGRAFOS
     pair<Graph*,Graph*> myPair = GenerateComplementGraphPair(5);
    printGraph2(myPair.first);
    cout<<endl;
    printGraph2(myPair.second);
    */

int tipo1 = atoi(argv[1]);
    int size1 = atoi(argv[2]); //tamaño del grafo (salvo en Centipede)
    int aristas1 = atoi(argv[3]); //cant aristas, poner lo que sea para tipo1<7

    int tipo2 = atoi(argv[4]);
    int size2 = atoi(argv[5]); //tamaño del grafo (salvo en Centipede)
    int aristas2 = atoi(argv[6]); //cant aristas, poner lo que sea para tipo2<7

    Graph* graph1;
    Graph* graph2;

    switch(tipo1){
    case 1: graph1 = GenerateCompleteGraphOfSize(size1); 
            break;
    case 2: graph1 = GeneratePathGraph(size1);
            break;
    case 3: graph1 = GenerateStar(size1);
            break;
    case 4: graph1 = GenerateCentipede(size1/(aristas1+1),aristas1);
            break;
    case 5: graph1 = GenerateRandomlyConnectedGraph(size1,50);
            break;
    case 6: {int arrayProb1[4] = {20,40,60,80};
            graph1 = GenerateListBasedRandomlyConnectedGraph(size1,arrayProb1,4);
            break;}
    case 7: graph1 = GenerateGraphFromMaxClique(size1,aristas1,round(size1/4));
            break;
    case 8: graph1 = GenerateGraphFromMinClique(size1,aristas1,round(size1/4));
            break;
    case 9: {Graph* result1 = new Graph();
            graph1 = GenerateTree(result1,0,size1);
            break;}
    case 10: graph1 = bipartito(size1,aristas1);
            break;
    case 11: graph1 = GenerateCentipedeUnidos(size1/(aristas1+1),aristas1);
            break;
    }

        switch(tipo2){
    case 1: graph2 = GenerateCompleteGraphOfSize(size2); 
            break;
    case 2: graph2 = GeneratePathGraph(size2);
            break;
    case 3: graph2 = GenerateStar(size2);
            break;
    case 4: graph2 = GenerateCentipede(size2/(aristas2+1),aristas2);
            break;
    case 5: graph2 = GenerateRandomlyConnectedGraph(size2,50);
            break;
    case 6: {int arrayProb2[4] = {20,40,60,80};
            graph2 = GenerateListBasedRandomlyConnectedGraph(size2,arrayProb2,4);
            break;}
    case 7: graph2 = GenerateGraphFromMaxClique(size2,aristas2,round(size2/4));
            break;
    case 8: graph2 = GenerateGraphFromMinClique(size2,aristas2,round(size2/4));
            break;
    case 9: {Graph* result2 = new Graph();
            graph2 = GenerateTree(result2,0,size2);
            break;}
    case 10: graph2 = bipartito(size2,aristas2);
            break;
    case 11: graph2 = GenerateCentipedeUnidos(size2/(aristas2+1),aristas2);
            break;
    }

    string inputForYourMethods  = getinputStringFromGraphs(graph1,graph2);

    cout << inputForYourMethods;
    return 0;
}
