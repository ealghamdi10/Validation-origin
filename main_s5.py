from s1_bfs.graph import predicate_finder
from s3_IProxy.P_T_Proxy import ParentTraceProxy, getTrace
from s5_Alice_Bob.AB1 import AliceBob, guardeAB, changeAB
from s5_Alice_Bob.AB2 import AliceBob2, changeAB2
from s4_Semantics.Rule import Rule
from s4_Semantics.S_Program import SoupProgram
from s4_Semantics.S_Semantics import SoupSemantics
from s4_Semantics.Str2Tr import Str2Tr
from s1_bfs.graph import bfs

if __name__ == '__main__':
     '''
     ABconf = AliceBob()
     iC = ABconf
     prog = SoupProgram(iC)
     # générer les règles pour AliceBob
     for i in range(3):
          for j in range(3):
               if i != j:
                    prog.add(Rule('{} vers {}'.format(i, j), guardeAB(i, j), changeAB(i, j)))
     # for k in range(len(prog.rules)):
     #     print(prog.rules[k])
   
     s = SoupSemantics(prog)
     translater = Str2Tr(s)
     dict = {}
     ptp = ParentTraceProxy(translater, dict)
     [p, found, count, target], known = predicate_finder(ptp, iC.AB_on_entry)
     print(getTrace(dict, target))
     '''

     ABconf=AliceBob2()
     iC = ABconf
     prog = SoupProgram(iC)
     # générer les règles pour A&Bob2
     for i in range(5):
          for j in range(5):
               if i!=j:
                    prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB2(i,j), changeAB2(i,j)))

     s = SoupSemantics(prog)
     translater = Str2Tr(s)

     o = [s]
     bfs(translater, o, iC.AB2_on_entry2)

     '''
     dict={}
     ptp=ParentTraceProxy(translater, dict)
     [p, found, count, target], known = predicate_finder(ptp, iC.AB2_on_entry)
     print(getTrace(dict, target))
     '''