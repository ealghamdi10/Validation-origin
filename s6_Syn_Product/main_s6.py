from main_s4 import hanoi_on_entry1
from s1_bfs.graph import predicate_finder
from s3_IProxy.P_T_Proxy import ParentTraceProxy, getTrace
from s4_Semantics.AConfig import AConfig
from s4_Semantics.Rule import Rule
from s4_Semantics.S_Program import SoupProgram
from s4_Semantics.S_Semantics import SoupSemantics
from s4_Semantics.Str2Tr import Str2Tr
from s5_Alice_Bob.conf2 import Conf2, Conf3
from s5_Alice_Bob.ISS import InputSoupSemantics
from s5_Alice_Bob.StepSynchProduct import StepSynchronousProduct
from s5_Alice_Bob.Stutter import Stutter

g1=lambda i,c : c.PC==1
def a1(i, c):
    c.PC=1

g2=lambda i,c: c.PC==1 and i.action is Stutter()
def a2(i, c):
    c.PC=2

g3=lambda c : c.PC=='a'
def a3(c):
    c.PC='b'

def fct_de_test(n):
    print(n)
    return True
 #  à droite
conf=Conf2()
program=SoupProgram(conf)
program.add(Rule('règle 1', g1, a1))
program.add(Rule('règle 2', g2, a2))
p=InputSoupSemantics(program)

# à gauche
confg=Conf3()
programg=SoupProgram(confg)
programg.add(Rule('R1', g3, a3))
m=SoupSemantics(programg)
ssp=StepSynchronousProduct(m,p)

def test():

    l=ssp.initial()

    step, rule=ssp.enabledActions(l[0])[0][0]

    #action=?
    source=(ssp.lhs, ssp.rhs)
    res=ssp.execute((step, rule), source)
    print(res)

def test2():
    translater = Str2Tr(ssp)
    dict = {}
    ptp = ParentTraceProxy(translater, dict)
    [p, found, count, target], known = predicate_finder(ptp, fct_de_test)
    print(getTrace(dict, target))

test2()