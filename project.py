from math import inf
from math import log2
import numpy as np


class Vertex:

    def __init__(self,id):
        self.attributes = {}
        self.attributes['id'] = id
        self.list = []
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


#    attach the information of the sound and probability while adding the edge

    def add_edge(self, i, j, sigma, prob):
        self.vertices[i.get('id')].append(j.get('id'))
        self.edges[(i.get('id'),j.get('id'))].append(sigma)
        self.edges[(i.get('id'),j.get('id'))].append(log2(prob))

    def sigma(self, i, j):
        return self.edges[(i.get('id'),j.get('id'))][0]

    def prob(self, i, j):
        return self.edges[(i.get('id'),j.get('id'))][1]



    def Viterbi(self, s, v, count):
        # base case to check if finished check sounds
        if len(s) == 0:
            self.list.append(v.get('id'))

        # identifier for whether the path is found
        else:
            found = False

        #for every neighbor vertex check whether satisfy the sound; if yes, append the
        #vertex to the list and teace its neighbor next recursively
            for i in self.vertices[v.get('id')]:
                if self.sigma((v.get('id'), i)) == s[count] and found == False:
                    self.list.append(v.get('id'))
                    j = self.id_to_v[i]
                    found = True
                    Viterbi(self, s[count:], j, count + 1)

        # return NO-SUCH-PATH if found is false, if it is true, return the list
        if found == False:
            print("NO-SUCH-PATH!\n")
        else:
            return self.list





    def Viterbiprob(self, s, v):

        #having the table record the probability and path record the exact path
        table = [0]
        path = [0, v]

        for i in range(1, len(s)):
            found = False
            p = -10000000
            for j in range(1, i + 1):
                for k in self.vertices[path[j].get('id')]:
                    if self.sigma((path[j].get('id'), k)) == s[j - 1]:
                        found = True
                        q = self.id_to_v[k]
                        # calculate the optimal conpounding probability using the table and max method
                        p2 = prob(self, path[j], q) + table [j - 1]
                        p = max(p, p2)    # with coresponding vertex q but dont know how to do it????????????

            #append the probability p to the table and the vertex q to the path
            table.append(p)
            path.append(q)

        # look for the identifier found to return either NO-SUCH-PATH or the sublist of the path
        if found == False:
            print("NO-SUCH-PATH!\n")
        else:
            return path[1:]
