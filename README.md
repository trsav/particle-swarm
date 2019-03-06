# Particle Swarm Optimization within Python
Simulated Annealing is implimented over an arbitary number of dimensions, and included are utilities for plotting the optimization trajectory as well as function value over time.

## Particle Swarm Background


### Limitations of current implimentation

### Prerequisites

Python 3.0 is required. The ParticleSwarmUtility.py file must be in the same directory as the ParticleSwarm.py file in order to enable the utility to be used.

## Function Use
``` 
    INPUTS
    f           :function to be optimized
    bounds      :bounds of each dimension in form [[x1,x2],[x3,x4]...]
    p           :number of particles
    w           :adjustable parameter
    c1          :adjustable parameter
    c2          :adjustable parameter
    
    OUTPUTS
    swarm_best  : coordinates of optimal solution, with regards to exit
                  conditions
```

## Example

With the ParticleSwarmUtility.py and ParticleSwarm.py files within the same directory.
Running the following:
```
f=Rosenbrock #setting function to be optimized
dimensions=5 
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=[-5,5]
p=50 #number of particles
#the three particle swarm parameters:
w=0.6 
c1=2.8
c2=1.3

particleswarm(f,bounds,p,w,c1,c2)
```
Produces the following outputs:
```
Optimum at:  [0.99934111 0.99912605 0.99834905 0.99673156 0.993232  ]
Function at optimum:  4.113161417643173e-05

```

 


    
## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)
