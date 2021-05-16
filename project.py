from math import inf
from math import log
import numpy as np


class Vertex:

    def __init__(self,id):
        self.attributes = {}
        self.attributes['id'] = id
        self.probability = 0

    def __str__(self):
        return str(self.attributes)

    def new_copy(self):
        return Vertex(self.attributes['id'])

    def set(self,key,value):
        self.attributes[key] = value

    def get(self,key):
        return self.attributes[key]


class Graph:

    def __init__(self):
        self.vertices = {}
        self.id_to_v = {}
        self.edges = {}


    def add_vertex(self, i):
        self.id_to_v[i.get('id')] = i
        self.vertices[i.get('id')] = []

    def id_to_v(self, id):
        return self.id_to_v[id]

    def add_edge(self, i, j, sigma, prob):
        self.vertices[i.get('id')].append(j.get('id'))
        self.edges[(i.get('id'),j.get('id'))] = []
        self.edges[(i.get('id'),j.get('id'))].append(sigma)
        self.edges[(i.get('id'),j.get('id'))].append(-log(prob))

    def sigma(self, i, j):
        try:
            return self.edges[(i,j)][0]
        except:
            return None

    def prob(self, i, j):
        try:
            return self.edges[(i,j)][1]
        except:
            return None




    def Viterbi(self, s, v):
        # base case to check if finished check sounds

        if len(s) == 0:
            return v

        for i in self.vertices[v]:
            if self.sigma(v, i) == s[0]:
                res = self.Viterbi(s[1:], i)
                if res != False:
                    list1 = [v]
                    for x in res:
                        list1.append(x)
                    return list1
        return False



    def build_table(self, s, table, path, stage = 1):
        # finish state
        if stage == len(s):
            return table, path

        # fill next column
        for rowIndex in range(len(table)):
            if path[rowIndex][stage + 1] != '0':
                # this means table[rowIndex][0] is the vertex to go next from
                for nextVertex in self.vertices[table[rowIndex][0]]:
                    # find the next row
                    for nextRow in range(len(table)):
                        try:
                            if self.sigma(path[rowIndex][0], path[nextRow][0]) == s[stage]:
                                p = self.prob(path[rowIndex][0], path[nextRow][0]) + float(table[rowIndex][stage+1])

                                path[nextRow][stage+2] = path[rowIndex][0]
                                table[nextRow][stage+2] = p
                        except:
                            print("hello")

        return self.build_table(s,table,path, stage+1)


    def Viterbiprob(self, s, v):

        #having the table record the probability and path record the exact path
        key_list = self.vertices.keys()

        table = [['0' for i in range(len(s) + 2)] for j in range(len(key_list))]
        path = [['0' for i in range(len(s) + 2)] for j in range(len(key_list))]

        j = 0
        for i in key_list:
            table[j][0] = i
            path[j][0] = i
            j += 1



        row = 0
        while path[row][0] != v:
            row += 1


        for j in range(1, 2):
            found = False
            orow = row
            for k in self.vertices[path[orow][0]]:
                  if self.sigma(path[orow][0], k) == s[j - 1]:
                        found = True
                        row = 0
                        while table[row][0] != k:
                            row += 1
                        # calculate the optimal conpounding probability using the table and max method
                        p = self.prob(path[orow][0], k) + float(table[orow][j])

                        if float(table[row][j + 1]) > p or float(table[row][j + 1]) == 0:
                            table[row][j + 1] = p
                            path[row][j + 1] = path[orow][0]

            table, path = self.build_table(s, table, path)

            #append the probability p to the table and the vertex q to the pat


        # look for the identifier found to return either NO-SUCH-PATH or the sublist of the path
        found = False

        prob = 100
        for i in range(len(key_list)):
            if float(table[i][len(s) + 1]) != 0:
                prob = min(prob, float(table[i][len(s) + 1]))
                found = True

        if found == False:
            print("NO-SUCH-PATH!\n")
        else:

            row = 0
            while float(table[row][len(s) + 1]) != prob:
                row += 1

            list = []
            list.append(path[row][0])
            for i in range (len(s) + 1, 1, -1):
                list.append(path[row][i])
                orow = row
                row = 0

                while path[row][0] != path[orow][i]:
                    row += 1

            return list[::-1]




    def create_graph_1():
    G = Graph()

    for i in ['u','v','w','x','y','z']:
        G.add_vertex(Vertex(i))

    for (v1,v2, sigma, prob) in [('u','x', 's', 0.4),('u','v', 's', 0.6),('x','v', 'b', 0.2),('v','y', 'c', 0.8),
                                 ('y','x','g', 0.1),('w','y','h' ,0.2),('w','z', 'h', 0.1)]:

        G.add_edge(G.id_to_v[v1],G.id_to_v[v2], sigma, prob)

    return G

    def create_graph_2():
    G = Graph()

    for i in ['u','v','w','x','y','z']:
        G.add_vertex(Vertex(i))

    for (v1,v2, sigma, prob) in [('u','w', 's', 0.6),('u','x', 's', 0.4),('u','v', 's', 0.4),('x','v', 'b', 0.2),('v','y', 'c', 0.2),
                                 ('y','x','g', 0.1),('w','y','c' ,0.8),('w','z', 'h', 0.1)]:

        G.add_edge(G.id_to_v[v1],G.id_to_v[v2], sigma, prob)

    return G


    G1 = create_graph_1()

    G2 = create_graph_2()

    G1.Viterbiprob('scgb', 'u')

    G1.Viterbi('scgb', 'u')

    G1.Viterbiprob('sbgb', 'u')

    G1.Viterbi('schb', 'u')

    G2.Viterbiprob('scgb', 'u')

    
