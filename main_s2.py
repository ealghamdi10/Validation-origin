import copy
from s1_bfs.graph import *
from s1_bfs.bfs import *
from s2_abstraite.nbits import NBits
from s2_abstraite.noeud import Noeud
from s2_abstraite.TransitionRelation import TransitionRelation
from s2_abstraite.HanoiGraph import HanoiGraph
from s2_abstraite.HanoiConfiguration import HanoiConfiguration
from s2_abstraite.test import monNext


def f1(s, v, acc):
    acc[0]+=1
     #if v==10:
     #    return True
    return False

def testNBits():
    graphe=NBits([3], 4)
    #print(graphe.next(graphe.roots()[0]))
    print(bfs(NBits([3],4), [0], f1, None, None))

def testHanoi():
    tours=HanoiConfiguration(3,3)
    #print(tours.next([[1,2,3],[],[]]))
    #print(tours.roots())
    hanoi_graphe=HanoiGraph(tours)
    #print(hanoi_graphe.next(hanoi_graphe.roots()))
    #print(hanoi_graphe.next(hanoi_graphe.roots()))
    print(bfs(hanoi_graphe, [0], hanoi_graphe.hanoi_on_entry, None, None))

if __name__=="__main__":
    testHanoi()