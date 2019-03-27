# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:59:36 2019

@author: tomsa
"""

import numpy as np 
import copy
import numpy.random as rnd
import ParticleSwarmUtility as PSU

 


def particleswarm(f,bounds,p,c1,c2,vmax,tol):
    '''
    DESCRIPTION
    see https://en.wikipedia.org/wiki/Particle_swarm_optimization
    
    INPUTS
    f           :function to be optimized
    bounds      :bounds of each dimension in form [[x1,x2],[x3,x4]...]
    p           :number of particles
    c1          :adjustable parameter
    c2          :adjustable parameter
    vmax        :maximum particle velocity
    tol         :tolerance for exit condition 
    
    OUTPUTS
    swarm_best  : coordinates of optimal solution, with regards to exit
                  conditions
    '''
    print('Currently placing particles and giving them random \
    velocities...')
    d,particle_pos, particle_best, swarm_best, particle_velocity, \
        local_best, pos_val \
    = PSU.initiation(f,bounds,p) #initializing various arrays
    old_swarm_best=[0]*d
    c3=c1+c2
    K=2/(abs(2-c3-np.sqrt((c3**2)-(4*c3)))) #creating velocity weighting factor
    it_count=0
    while abs(f(old_swarm_best)-f(swarm_best))>tol: #exit condition 

        it_count+=1 
        if it_count>1000: #every 1000 iterations...
                        #create 'conflict' within the swarm and 
                        #give all particles random velocities
            print('Particles are too friendly! Creating conflict...')
            for j in range(p): #iterating ovre the number of particles
                particle_velocity[j]=[(rnd.uniform(-abs(bounds[i][1]-bounds[i][0])\
                    ,abs(bounds[i][1]-bounds[i][0]))) for i in range(d)]
                    #adding random velocity values for each dimension
            it_count=0 #reset iteration count
        
        for i in range(p): #iterates over each particle
            rp,rg=rnd.uniform(0,1,2) #creates two random numbers between 0-
            particle_velocity[i,:]+=(c1*rp*(particle_best[i,:]-particle_pos[i,:]))
            particle_velocity[i,:]+=(c2*rg*(local_best[i,:]-particle_pos[i,:]))
            particle_velocity[i,:]=particle_velocity[i,:]*K
            if particle_velocity[i].any() > vmax : #is any velocity is greater than vmax
                    particle_velocity[i,:]=vmax #set velocity to vmax
            #all of the above is regarding updating the particle's velocity
            #with regards to various parameters (local_best, p_best etc..)
            particle_pos[i,:]+=particle_velocity[i,:] #updating position
            
            PSU.withinbounds(bounds,particle_pos[i]) #if particle is out of bounds

            particle_fitness=f(particle_pos[i]) 
        
            if particle_fitness < pos_val[i]:
                particle_best[i,:]=particle_pos[i,:] #checking if new best
                pos_val[i]=particle_fitness
                f_swarm_best=f(swarm_best)
                if particle_fitness < f_swarm_best: 
                    old_swarm_best=swarm_best[:]
                    swarm_best=copy.deepcopy(particle_best[i,:]) 
                    print('current function value: ',f(swarm_best))

        local_best=PSU.local_best_get(particle_pos,pos_val,p)


    return print('Optimum at: ',swarm_best,'\n','Function at optimum: ',f(swarm_best)) 


                
f=PSU.Rosenbrock
dimensions=10
dimension_bounds=[-2,2]
bounds=[0]*dimensions #creating 5 dimensional bounds
for i in range(dimensions):
    bounds[i]=dimension_bounds

#creates bounds [[x1,x2],[x3,x4],[x5,x6]....]    
    
p=60 #shouldn't really change 
vmax=(dimension_bounds[1]-dimension_bounds[0])*0.75
c1=2.8 #shouldn't really change
c2=1.3 #shouldn't really change
tol=0.00000000000001

particleswarm(f,bounds,p,c1,c2,vmax,tol)            
                
                
    