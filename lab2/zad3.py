import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from graph_generator import *


class Circuit:
    def __init__(self, file):
        self.load_data(file)
        self.kirchoff_circuit()

    def load_data(self, file):
        self.graph = nx.Graph()
        with open(file, 'r') as f:
            lines = f.read().split('\n')
            sem_edge = lines[0].split()
            s = sem_edge[0]
            t = sem_edge[1]
            e = sem_edge[2]
            self.graph.add_edge(s,t, R = 0, E = e)
            id = 0
            for edge in lines[1:]:
                if edge == '':
                    continue
                (x,y,r) = edge.split()
                if x == s and y == t:
                    continue
                else:
                    self.graph.add_edge(x,y, R = r, E = -1, id = id, n_to = -1, n_from = -1, I=None)
                    id += 1
        
        

    def draw_circuit(self):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_nodes(self.graph,pos)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edges(self.graph, pos)
        labels = nx.get_edge_attributes(self.graph,'R')
        nx.draw_networkx_edge_labels(self.graph,pos,edge_labels=labels)
        plt.show()
    
    def kirchoff_circuit(self):
        n = self.graph.number_of_edges() - 1
        A = np.zeros((n,n))
        B = np.zeros(n)
        cycles = nx.cycle_basis(self.graph)
        row = 0
        for cycle in cycles:
            cycle.append(cycle[0])

            for i in range(len(cycle) - 1):
                x, y = cycle[i], cycle[i+1]
                edge = self.graph.edges[x,y]
                if edge['E'] != -1:
                    B[row] = edge['E']
                    continue
                ## if we are on this edge first time or we are going the same way
                if edge['n_to'] == -1 or edge['n_to'] == y:
                    edge['n_from'], edge['n_to'] = x,y
                    A[row][edge['id']] = edge['R']
                else:
                    A[row][edge['id']] = float(edge['R']) * (-1)
            row += 1
        for node in self.graph.nodes:
            is_st = False
            for (x,y) in self.graph.edges(node):
                edge = self.graph.edges[x,y]
                if edge['E'] != -1:
                    is_st = True
                    break
            if is_st:
                continue
            for (x,y) in self.graph.edges(node):
                edge = self.graph.edges[x,y]
                A[row][edge['id']] = 1 if node == edge['n_to'] else -1
            row += 1

        I = np.linalg.solve(A,B)
        

        for (x,y) in self.graph.edges():
            edge = self.graph.edges[x,y]
            if (edge['E'] != -1):
                continue
            edge['I'] = I[edge['id']] 

        self.dgraph = nx.DiGraph()
        
        for (x,y) in self.graph.edges():
            edge = self.graph.edges[x,y]
            if (edge['E'] != -1):
                self.dgraph.add_edge(x,y, I=math.inf)
                self.dgraph.add_edge(y,x, I=math.inf)
            else:
                n_from, n_to = edge['n_from'], edge['n_to']
                i = round(I[edge['id']], 2)
                if i < 0:
                    i *= -1
                    n_from, n_to = n_to, n_from
                self.dgraph.add_edge(n_from,n_to, I=i)

    def draw_result(self):
        if nx.check_planarity(self.dgraph)[0]:
            pos = nx.planar_layout(self.dgraph)
        else:
            pos = nx.spring_layout(self.dgraph)
        nx.draw_networkx_nodes(self.dgraph,pos)
        nx.draw_networkx_labels(self.dgraph, pos)
        nx.draw_networkx_edges(self.dgraph, pos)
        labels = nx.get_edge_attributes(self.dgraph,'I')
        nx.draw_networkx_edge_labels(self.dgraph,pos,edge_labels=labels)
        plt.show()
        
while 1:    
    generate_grid(5)
    test = Circuit("graph.txt")
    test.draw_result()


