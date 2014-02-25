import networkx as nx
from networkx import linalg
import pylab
import numpy.linalg
eigenvalues = numpy.linalg.eigvals
T1 = nx.DiGraph()

##ex A->C->B->A
#T1.add_edge(1,2)
#T1.add_edge(2,3)
#T1.add_edge(3,1)
#



##ex A,B,C all connected
#T1.add_edge(4,5)
#T1.add_edge(4,6)
#T1.add_edge(5,6)
#T1.add_edge(5,4)
#T1.add_edge(6,5)
#T1.add_edge(6,4)
#


##ex A->B,C 
T1.add_edge(7,8)
T1.add_edge(7,9)


nx.draw(T1)
pylab.show()
laplacian = linalg.laplacianmatrix.directed_laplacian_matrix(T1)


e = eigenvalues(laplacian)
print("laplacian is")
print(laplacian)
print ("eigenvalues are")
print(e)