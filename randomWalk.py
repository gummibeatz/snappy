# A, B, C
import pylab
import networkx as nx
import numpy as np
import random as rd

T1 = nx.DiGraph()

#ex A->C->B->A


    
T1.add_edge(0,1)
T1.add_edge(1,2)
T1.add_edge(2,0)

for n in range(1, len(T1.nodes()) +1):
    T1.add_node(n, ct =0)
    
print T1.nodes(data = True)[1][1]


ts = 10

numnodes = 3 

startnode = np.random.randint(low = 0, high =2, size = 1)[0]
#print startnode , T1.successors(startnode)
current = startnode

for t in range(1, 4):
    nxt = rd.choice(T1.successors(current))
    # if statement to create all successors. 
    # while loop for random choice of succesors, if ct ==1 .
    # ends if randomizes to never been walked on node or used up all nodes
    #while T1.nodes(data =True)[nxt][1]['ct'] == 1:
    #    nxt = rd.choice(T1.successors(current))
    T1.add_node(current, ct=1)
    current = nxt
    print T1.nodes(data = True)[1][1]['ct']


#nx.draw(T1)
#pylab.show()
