# Particle Swarm Optimization within Python
<p align="center">
<img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/movie.gif" width="300"> <img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/movie2.gif" width="300"> 
</p>


## Particle Swarm Background

Particle Swarm optimization is first attributed by Kennedy, Eberhar and Shi in their 1995 paper 'Particle Swarm Optimization'. It locates the minimum of a function by creating a number of 'particles'. These particles store their best position as well as also storing the global best position. 
It is this combination of local and global information that gives rise to 'swarm intelligence'.

Within an iteration, a particle will update it's position slightly towards both the swarm best and slightly towards it's personal best. With eventually the particles converging on (hopefully) the global minimum.

Mathematically this position update is defined as follows: 

 <p align="center">
   <img src="https://render.githubusercontent.com/render/math?math=v_i^{t %2B 1}=\omega v_i^t %2B \phi_br_b(x_{i_b}-x_i) %2B \phi_gr_g(g_b-x_i)">
 </p>
  <p align="center">
   <img src="https://render.githubusercontent.com/render/math?math=x_i^{t %2B 1}=x_i^t %2B v_i^t">
   </p>
   
These equations become clear when presented in a simple 2 variable scenario: 
<p align="center">
<img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/PS1.png" width="400"> <img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/PS2.png" width="400">
</p>

Initially every particle is given a random velocity vi, and the function is evaluated for every particle. 
Each particle is now 'aware' of it's previous best position as well as the global best position. On the first iteration it's previous best position is obviously it's current position so this term doesn't come into play until the second iteration. 

It's current velocity is first scaled by a factor of w in order to ensure particle velocities don't grow exponentially over each iteration.

The term <img src="https://latex.codecogs.com/gif.latex?\phi_br_b(x_{i_b}-x_i)" title="\phi_br_b(x_{i_b}-x_i)" /> then represents the vector from the particles position, towards it's previous best position. It is scaled by a constant <img src="https://latex.codecogs.com/gif.latex?\phi_b" title="\phi_b" /> (Here I've sometimes referred to this as c1) and a random value <img src="https://latex.codecogs.com/gif.latex?r_b" title="r_b" /> between 0 and 1 (uniformly distributed). This random scaling provides the stochastic element of this optimization scheme.

Likewise <img src="https://latex.codecogs.com/gif.latex?\phi_gr_g(g_b-x_i)" title="\phi_gr_g(g_b-x_i)" /> represents the vector from the particles position towards the swarms best position, again scaled by a constant <img src="https://latex.codecogs.com/gif.latex?\phi_g" title="\phi_g" /> and a random variable <img src="https://latex.codecogs.com/gif.latex?r_g" title="r_g" />. Varying these phi (or c) parameters effect how locally or globally the particle explores the search space. A higher value will provide a larger vector and therefore the particle will take into account that aspect more than another. 

It's seen in the second graph the effect of lining up these vectors and then the final step of moving the particle to it's new position. 



<img align="right" src="https://github.com/TomRSavage/ParticleSwarm/blob/master/Sty.gif" width="400">



### Current implimentation

Currently the algorithm is set to terminate when the difference in the value of the function evaluated at the swarm's best position changes less than a certain tolerance value. 

There are important aspects within this code; such as limiting a particle's velocity to vmax, or if a particle exits the bounds it gets contrained to the edge, that have been implimented.

There are also two important parameters (c1,c2) that define how much a particle moves towards the swarm best and it's best. 
There has been much discussion over a 'standard' for these parameters (See Bratton, Kennedy: Defining a Standard for Particle Swarm Optimization (2007)) but in reality each problem will perform better with different conditions.  Here they are set to 2.3 and 1.8 respectively, as suggested by Bratton and Kennedy.
Optimizing these parameters takes the form of a meta-optimization problem.

 <img align="left" src="https://github.com/TomRSavage/ParticleSwarm/blob/master/PSOtopology.png" width="400">
 

The 'Topology' of a particle swarm also bears an influence on how the swarm behaves. Here, each particle has knowledge about it's two neighbour's positions. This is then that particle's 'global best'. This is known as the ring topology, and was initially deemed to converge too slowly. However it stops the particles becoming too focused on the global best point and converging prematurely. Through this shared knowledge the particles are more likely to find the global optimum.

 I found that even with this topology, the search for the optimum sometimes ground to a halt. I put this down to all the particles becoming too close and their velocities becoming too low.

 To solve this problem, I simply added a random velocity to all particles every 1000 iterations. Effectively causing a 'conflict' within the swarm and pushing them all along a bit. This seemed to solve the problem fairly effectively. 
 Upon further research similar solutions have been implemented under the term 'craziness', also adding an extra stochastic element to stop the particles from stagnating. 



### Limitations
Recently (~2010) there has been an effort to simplify ever more complicated particle swarm algorithms, with good reason. There is an obvious trade off for computing time and effectiveness of an algorithm, and for some cases the loss in performance is made up for in the gain in computational time. 
 For this reason I've decided to stick to the commonly used ring topology, with the implimentations described above.

### Effect of swarm conflict and topologies
<p align="center">
<img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/Graph.PNG" width="400"><img src="https://github.com/TomRSavage/ParticleSwarm/blob/master/GraphZoom.PNG" width="400">
</p>
 The above figure shows how whilst using a global topology initially provides faster convergence, it stagnates very quickly. A local topology, whilst initially slower allows the particles to converge on the global minimum. 
 The effect of the added conflict is also clear, ensuring the particles do not become complacent and allowing them to reach the global minimum albeit at a slower pace.

### Prerequisites

Python 3.0 is required. The ParticleSwarmUtility.py file must be in the same directory as the ParticleSwarm.py file in order to enable the utility to be used.

## Function Use
``` 
    INPUTS
    f           :function to be optimized
    bounds      :bounds of each dimension in form [[x1,x2],[x3,x4]...]
    p           :number of particles
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
f=PSU.Rosenbrock
dimensions=10
dimension_bounds=[-5,5]
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=dimension_bounds
    
p=30
vmax=(dimension_bounds[1]-dimension_bounds[0])
c1=2.8 #shouldn't really change
c2=1.3 #shouldn't really change
tol=0.00000000000001

particleswarm(f,bounds,p,c1,c2,vmax,tol)

```
Produces the following outputs:
```
Optimum at:  [1.00000132 0.99997581 0.99995583 0.99989929 0.99977618 0.99953611
 0.99906464 0.99812545 0.99625688 0.99248657]
 Function at optimum:  1.9022223352164056e-05

```

## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)
