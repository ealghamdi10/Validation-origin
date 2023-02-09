from s1_bfs.graph import predicate_finder
from s3_IProxy.P_T_Proxy import ParentTraceProxy, getTrace
from s4_Semantics.Rule import Rule
from s4_Semantics.S_Program import SoupProgram
from s4_Semantics.S_Semantics import SoupSemantics
from s4_Semantics.Str2Tr import Str2Tr
from s5_Alice_Bob.AB2 import AliceBob2

#  Alice & Bob avec Drapeau
from s5_Alice_Bob.conf2 import Conf2
from s5_Alice_Bob.ISS import InputSoupSemantics
from s5_Alice_Bob.StepSynchProduct import StepSynchronousProduct


def test():
    # alice & Bob
    ABconf = AliceBob2()
    iC = ABconf
    prog = SoupProgram(iC)
    # générer les règles pour AliceBob2
    for i in range(5):
        for j in range(5):
            if i != j:
                prog.add(Rule('{} vers {}'.format(i, j), ABconf.guardeAB2(i, j), ABconf.changeAB2(i, j)))

    #s = SoupSemantics(prog)
    p =SoupSemantics(prog)

    # acceptation :
    conf=Conf2()
    guarde=lambda i,c : c.PC==1

    def guarde2(i, c):
        return c.PC == 1 and not (2 in i.source.conf[2]) and not (2 in i.source.conf[2])

    def a2(i, c):
        c.PC=2

    def fct_de_test(n):
        #print(n[0].conf)
        return (2 in n[0].conf[2]) and (1 in n[0].conf[1])
        #return (2 in n[0].conf[2]) and (1 in n[0].conf[2])
        #return True

    programg=SoupProgram(conf)
    programg.add(Rule('ne rien faire', guarde, None))
    programg.add(Rule('avancer', guarde2, a2))
    m=InputSoupSemantics(programg)

    ## SSP
    ssp=StepSynchronousProduct(p, m)
    # l=ssp.initial()
    translater = Str2Tr(ssp)
    dict = {}
    ptp = ParentTraceProxy(translater, dict)
    [p, found, count, target], known = predicate_finder(ptp, fct_de_test)
    if found:
        print(getTrace(dict, target))

test()