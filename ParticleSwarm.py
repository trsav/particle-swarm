# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:59:36 2019

@author: tomsa
"""

import numpy as np 
import copy
import numpy.random as rnd
import time
import ParticleSwarmUtility as PSU

def particleswarm(f,bounds,p,w,c1,c2,vmax,tol):
    '''
    DESCRIPTION
    see https://en.wikipedia.org/wiki/Particle_swarm_optimization
    
    INPUTS
    f           :function to be optimized
    bounds      :bounds of each dimension in form [[x1,x2],[x3,x4]...]
    p           :number of particles
    w           :adjustable parameter
    c1          :adjustable parameter
    c2          :adjustable parameter
    vmax        :maximum particle velocity
    tol         :tolerance for exit condition 
    
    OUTPUTS
    swarm_best  : coordinates of optimal solution, with regards to exit
                  conditions
    '''
    d,particle_pos, particle_best, swarm_best, particle_velocity\
    = PSU.initiation(f,bounds,p) #initializing various arrays
    old_swarm_best=[0]*d
    while abs(f(old_swarm_best)-f(swarm_best))>tol: #exit condition 
        for i in range(p): #iterates over each particle
            rp,rg=rnd.uniform(0,1,2) #creates two random numbers between 0-1
            particle_velocity[i,:]=w*particle_velocity[i,:]
            particle_velocity[i,:]+=(c1*rp*(particle_best[i,:]-particle_pos[i,:]))
            particle_velocity[i,:]+=(c2*rg*(swarm_best[:]-particle_pos[i,:]))
            if particle_velocity[i].any() > vmax :
                particle_velocity[i,:]=0
            #all of the above is regarding updating the particle's velocity
            #with regards to various parameters (swarm_best, p_best etc..)
            particle_pos[i,:]+=particle_velocity[i,:] #updating position
            if PSU.withinbounds(bounds,particle_pos[i])==False:
                particle_velocity[i,:]=0
            if f(particle_pos[i]) < f(particle_best[i]):
                particle_best[i,:]=particle_pos[i,:] #checking if new best
                if f(particle_best[i]) < f(swarm_best): 
                    old_swarm_best=swarm_best[:]
                    swarm_best=copy.deepcopy(particle_best[i,:]) 
                    print('current function value: ',f(swarm_best))
                    #checking if there's a new swarm best
    return print('Optimum at: ',swarm_best,'\n','Function at optimum: ',f(swarm_best)) 


                
                
                
                
                
                
                
    