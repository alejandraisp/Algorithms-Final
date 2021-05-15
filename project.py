from math import inf
from math import log2
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
        return self.edges[(i,j)][0]

    def prob(self, i, j):
        return self.edges[(i,j)][1]




     def Viterbi(self, s, v, count):
        # base case to check if finished check sounds

        if len(s) == 0:
            return v

            for i in self.vertices[v]:
                if self.sigma(v, i) == s[count]:
                    res = self.Viterbi(s[count + 1:], i, count + 1)
                    if res != False:
                        list = [v]
                        return list.append(res)

            return False




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

        #for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):
            found = False
            orow = row
            for k in self.vertices[path[orow][0]]:
                  if self.sigma(path[orow][0], k) == s[j - 1]:
                        found = True
                        row = 0
                        while table[row][0] != k:
                            row += 1
                        # calculate the optimal conpounding probability using the table and max method
                        p = self.prob(path[orow][0], k) + int(table[orow][j])

                        if int(table[row][j + 1]) < p:
                            table[row][j + 1] = p
                            path[row][j + 1] = path[orow][0]

            #append the probability p to the table and the vertex q to the pat


        # look for the identifier found to return either NO-SUCH-PATH or the sublist of the path
        if found == False:
            print("NO-SUCH-PATH!\n")
        else:
            prob = 0
            for i in range(len(key_list)):
                prob = max(prob, int(table[i][len(s) + 1]))


            row = 0
            while int(table[row][len(s) + 1]) != prob:
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


    G1 = create_graph_1()


    G1.Viterbiprob('scgb', 'u')

    G1.Viterbi('scgb', 'u', 0)
