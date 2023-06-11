#final
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp
import sys
sys.setrecursionlimit(100000)       #to increase recursion limit

#80000+ nodes
node_adjlist = nx.read_adjlist('Slashdot0902.txt',create_using=nx.Graph(),nodetype=int)   #reading file in adjecency list
#print(node_adjlist)
#node_adjlist = nx.read_adjlist('facebook_combined.txt',create_using=nx.Graph(),nodetype=int)   #reading file in adjecency list

#if nx.is_weighted(node_adjlist):
    #print("BFS does not work on weigted graphs\n")
    #exit()

#else:
 #   print("\nBFS would work for this Data Set:\n")


visited_nodes = [] #visited nodes list initialized
queue = []  #BFS queue initialized

f = open("DFS_file.txt", "w")
f2 = open("DFS_queues.txt","w")

visited_nodes = set() #to keep a track of the nodes visited

def dfs(visited_nodes, graph, node):  #function for DFS 
    if node not in visited_nodes:       #only adding nodes which are not visited
        print (node)                       #printing all the nodes which are in the way
        f.write(str(node))                  #writing in file
        f.write(" ")

        visited_nodes.add(node)             #visited nodes are not checked again (marked)
        f2.write("\nNode is added to visited queue : ")
        f2.write(str(node))

        for neighbour_node in graph[node]:  
            dfs(visited_nodes, graph, neighbour_node)   #for each neighbour node dfs is runned again

#main (driver code)
print("Output after running DFS")
dfs(visited_nodes, node_adjlist, 0)

f.close()   #files are closed
f2.close()