import networkx as nx
import random
def generate_erdos(n,p):
    graph = nx.erdos_renyi_graph(n,p)
    while not nx.is_connected(graph):
        G = nx.erdos_renyi_graph(n,p)
    e = 10
    s = random.choice(list(graph.nodes))
    t = random.choice(list(graph.nodes))
    while s == t or graph.has_edge(s, t):
        s = random.choice(list(graph.nodes))
        t = random.choice(list(graph.nodes))
    with open("graph.txt", 'w') as file:
        file.write(f"{s} {t} {e}\n")
        for (x,y) in graph.edges():
            file.write(f"{x} {y} {1}\n")
        file.close()

def generate_cubic(n):
    graph = nx.random_regular_graph(3,n)
    e = 10
    s = random.choice(list(graph.nodes))
    t = random.choice(list(graph.nodes))
    while s == t or graph.has_edge(s, t):
        s = random.choice(list(graph.nodes))
        t = random.choice(list(graph.nodes))
    with open("graph.txt", 'w') as file:
        file.write(f"{s} {t} {e}\n")
        for (x,y) in graph.edges():
            file.write(f"{x} {y} {1}\n")
        file.close()

def generate_grid(n):
    graph = nx.grid_2d_graph(n,n)
    e = 10
    s = random.choice(list(graph.nodes))
    t = random.choice(list(graph.nodes))
    while s == t or graph.has_edge(s, t):
        s = random.choice(list(graph.nodes))
        t = random.choice(list(graph.nodes))
    with open("graph.txt", 'w') as file:
        file.write(f"{s[0]*n + s[1]} {t[0]*n + t[1]} {e}\n")
        for (x,y) in graph.edges():
            file.write(f"{x[0] * n + x[1]} {y[0] * n + y[1]} {1}\n")
        file.close()
def generate_small_world(n):
    graph = nx.connected_watts_strogatz_graph(n, n//2, 1)
    e = 10
    s = random.choice(list(graph.nodes))
    t = random.choice(list(graph.nodes))
    while s == t or graph.has_edge(s, t):
        s = random.choice(list(graph.nodes))
        t = random.choice(list(graph.nodes))
    with open("graph.txt", 'w') as file:
        file.write(f"{s} {t} {e}\n")
        for (x,y) in graph.edges():
            file.write(f"{x} {y} {1}\n")
        file.close()



        
        
