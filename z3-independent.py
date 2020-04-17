import itertools
import z3 

# Read input file. The first line is the
# number of nodes. The remaining lines should
#pairs of numbers each pair denoting an edge
f=open("graph1.txt","r")
n=int((f.readline()).split()[0])
rest=f.read()
lines=rest.splitlines()
edges=[tuple(map(int,line.split())) for line in lines]

#create space for n variables 
vars=[None]*n

#create n z3 Boolean variables
for i in range(0,n):
   vars[i]= z3.Bool("x"+str(i))

# looking for independent set of size 4
k=4
# we need all combinations of n-k+1 variables
comb=n-k+1
#instantiate a z3 solver
solver=z3.Solver()
#crearte an Or clause for each combination of n-k+1 variables
for c in itertools.combinations(vars,comb):
   solver.add(z3.Or(c))
# Add constraints on the edges   
for (s,e) in edges:
   solver.add(z3.Or(z3.Not(vars[s]),z3.Not(vars[e])))

if(solver.check()==z3.sat):
    print("Found and IS of size {}".format(k))
    m=solver.model()
    for d in m.decls():
        if(m[d]==True):
            print(d.name())

else:
   print("No IS of size {} exits".format(k))
