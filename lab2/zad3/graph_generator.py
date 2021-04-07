import networkx as nx
import random
def generate_erdos(n,p=0.3):
    graph = nx.erdos_renyi_graph(n,p)
    while not nx.is_connected(graph):
        graph = nx.erdos_renyi_graph(n,p)
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

def generate_bridge(n, p=0.3):
    n = n // 2
    graph1 = nx.erdos_renyi_graph(n,p)
    while not nx.is_connected(graph1):
        graph1 = nx.erdos_renyi_graph(n,p)
    graph2 = nx.erdos_renyi_graph(n,p)
    while not nx.is_connected(graph2):
        graph2 = nx.erdos_renyi_graph(n,p)
    
    bridge_left = random.choice(list(graph1.nodes))
    bridge_right = random.choice(list(graph2.nodes))
    bridge_right += n

    e = 10

    s = random.choice(list(graph1.nodes))
    t = random.choice(list(graph2.nodes)) + n
    while (s == bridge_left and t == bridge_right) or (s == bridge_right and t == bridge_left):
        s = random.choice(list(graph1.nodes))
        t = random.choice(list(graph2.nodes)) + n
    with open("graph.txt", 'w') as file:
        file.write(f"{s} {t} {e}\n")
        for (x,y) in graph1.edges():
            file.write(f"{x} {y} {1}\n")
        for (x,y) in graph2.edges():
            file.write(f"{x + n} {y + n} {1}\n")
        file.write(f"{bridge_left} {bridge_right} {1}\n")
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



        
        
