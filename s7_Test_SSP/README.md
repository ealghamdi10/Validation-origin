###### This is a code implementation for the step-synchronous product (SSP) of two soup programs, in which the first program models the behavior of two agents (Alice and Bob) and the second  program models the environment they are in. The purpose of the code is to find a trace that satisfies a given property, which is encoded as a function fct_de_test.

The code contains the following modules:

`s1_bfs.graph.predicate_finder`: implements a breadth-first search algorithm to find a trace that satisfies the property.

`s3_IProxy.P_T_Proxy.ParentTraceProxy`: builds a proxy between a trace and its parent.

`s3_IProxy.P_T_Proxy.getTrace`: retrieves the trace from the parent trace proxy.

`s4_Semantics.Rule`: defines the structure of a rule.

`s4_Semantics.S_Program`: defines a soup program as a collection of rules.

`s4_Semantics.S_Semantics`: defines the behavior of a soup program as a transition system.

`s4_Semantics.Str2Tr`: maps a string to a trace.

`s5_Alice_Bob.AB2`: defines the behavior of Alice and Bob.

`s5_Alice_Bob.conf2`: defines the environment the agents are in.

`s5_Alice_Bob.ISS`: defines the transition system of the environment.

`s5_Alice_Bob.StepSynchProduct`: defines the step-synchronous product of the two soup programs.

The test function is the entry point of the code. It first creates a soup 
program for the behavior of Alice and Bob and another soup program for the environment. 
Then, it creates the SSP of the two soup programs and finds a trace that satisfies the 
property **fct_de_test** by calling predicate_finder. The found trace is printed if it exists.
