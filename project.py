from math import inf
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
        self.vertices[i.attributes['id']].append(j.attributes['id'])
        self.edges[(i.attributes['id'],j.attributes['id'])].append(sigma)
        self.edges[(i.attributes['id'],j.attributes['id'])].append(prob)

    def sigma(self, i, j):
        return self.edges[(i.attributes['id'],j.attributes['id'])][0]

    def prob(self, i, j):
        return self.edges[(i.attributes['id'],j.attributes['id'])][1]



    def Viterbi(self, s, v, count):
        if len(s) == 0:
            self.list.append(v.get('id'))

        else:
            found = False

            for i in self.vertices[v.attributes['id']]:
                if self.sigma((v.attributes['id'], i)) == s[count] and found == False:
                    self.list.append(v.get('id'))
                    j = self.id_to_v[i]
                    found = True
                    Viterbi(self, s[count:], j, count + 1)

        if found == False:
            print("NO-SUCH-PATH!\n")
        else:
            return self.list



    def Viterbiprob(self, s, v, count):
