# Particle Swarm Optimization within Python

## Particle Swarm Background
Particle Swarm optimization is first attributed by Kennedy, Eberhar and Shi in their 1995 paper 'Particle Swarm Optimization. It locates the minimum of a function why creating a number of 'particles'. These particles store their best position has been as well as also storing the global best position. 
It is this combination of local and global information that gives rise to 'swarm intelligence'.

Within an iteration, a particle will update it's position slightly towards both the swarm best and it's personal best. With eventually the particles converging on the global minimum.

### Limitations of current implimentation

Currently the algorithm is set to terminate when the difference in the value of the function evaluated at the swarm's best position changes less than a certain tolerance value. 
This could be changed at a later date to a more 'clever' solution. 

There are also three important parameters (w,c1,c2) that define how much a particle moves towards the swarm best and it's best. 
There has been much discussion over a 'standard' for these parameters (See Bratton, Kennedy: Defining a Standard for Particle Swarm Optimization (2007)) but in reality each problem will perform better with different conditions. 
Optimizing these parameters takes the form of a meta-optimization problem.

The 'Topology' of a particle swarm also bears an influence on how the swarm behaves. Here, all particles are 'connected' with each other through their knowledge of the swarm best. A common adaptation to this is that the swarm best is replaced with the the best position of itself and it's two neighbours. It results in a slower convergence, but allows the swarm to not terminate prematurely. 

 <img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/PSOtopology.png" width="400"> Bratton, Kennedy (2007)

It is something that hopefully will be implimented soon here.

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
    vmax        :maximum particle velocity
    
    OUTPUTS
    swarm_best  : coordinates of optimal solution, with regards to exit
                  conditions
```

## Example

With the ParticleSwarmUtility.py and ParticleSwarm.py files within the same directory.
Running the following:
```
f=Rosenbrock

dimensions=5
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=[-5,5]
p=5
vmax=4 
w=0.6 
c1=2.8
c2=1.3
tol=0.00000001

particleswarm(f,bounds,p,w,c1,c2,vmax,tol)

```
Produces the following outputs:
```
Optimum at:  [0.99997687 0.99997492 0.99985836 0.99975199 0.99954017]
Function at optimum:  1.2193992644178545e-06

```

## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)
