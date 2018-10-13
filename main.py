import networkx as nx
import matplotlib.pyplot as plt

class Vision_Map(object):
    G = nx.Graph()
    edglist = []
    point = []
    width_list = []
    n = 0
    m = 0

    def __init__(self,start_n=0):
        self.read_map()
        if start_n == 1:
            for i in range(1,self.n+1):
                self.point.append(i)
        else:
            for i in range(0,self.n):
                self.point.append(i)
        self.G.add_nodes_from(self.point)
        #G = nx.Graph(self.edglist)


    def read_map(self):
        with open('map.txt') as f:
            lines = f.readlines()
            first_line = lines[0].split(" ")
            self.n = int(first_line[0])
            self.m = int(first_line[1])
            for i in range(1,len(lines)):
                line = lines[i].split(" ")
                s = int(line[0])
                e = int(line[1])
                c = int(line[2])
                self.width_list.append(c)
                self.edglist.append((s,e,c))
        self.G.add_weighted_edges_from(self.edglist)
        #self.G.add_edges_from(self.edglist)

    def draw(self):
        position = nx.circular_layout(self.G)
        nx.draw_networkx_nodes(self.G, position, nodelist=self.point, node_color="r")
        nx.draw_networkx_edges(self.G, position,width=self.width_list)
        nx.draw_networkx_labels(self.G, position)
        plt.show()

if __name__=="__main__":
    Amap = Vision_Map(1)
    Amap.draw()

