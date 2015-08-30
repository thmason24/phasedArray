# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys

#desired beam angle
theta=0

#set spacing
spacing = 1
numEl   = 30
#phase increment
incPhase=1
#set wave length
waveL = 0.5
waveL=waveL*2*np.pi
phase_samp = 20
phase_samp_list = np.linspace(0,np.pi,phase_samp)

#Function to generate plot
def plotBeam(spacing,numEl,waveL,incPhase,phase_samp):
    #intialize array
    antArray = []
    #add array for phase additions
    phaseAdd = []
    for i in range(0,numEl):
        antArray.append([i*spacing - ((numEl-1)*spacing)/2,0])
        phaseAdd.append(i*incPhase)
    ants=np.array(antArray)
    
    #create focus grid
    rangeLim=500
    XrangeLim = 200
    numPoints=100
    
    r = np.linspace(0,rangeLim,numPoints)
    x = np.linspace(0,XrangeLim,numPoints)
    #center
    x = x - x[-1]/2
    xx, rr = np.meshgrid(x,r,sparse=False)
    z=np.zeros(xx.shape)
    # calculate beam intensity
    
    for (ix,ir) , i in np.ndenumerate(rr):
        #iterate through antennas, 
        pos = [xx[ix,ir], rr[ix,ir]]
        posMat=np.tile(pos,[len(antArray),1])    
        #calculate distances
        distance=np.linalg.norm(ants-posMat, axis=1)
        #integrate over 4 samples of phase
        for phase in phase_samp_list:
            temp = 0
            for index, dist in enumerate(distance):
                temp += np.cos(dist/waveL*2*np.pi + phaseAdd[index] + phase)
            z[ix,ir] += temp**2
        z[ix,ir] += z[ix,ir]/phase_samp
    plt.figure()
    plt.pcolor(xx,rr,z,cmap='gray')
    plt.colorbar()
    plt.scatter(ants[:,0],ants[:,1],marker='.',color='b')
    #plt.scatter(ants[:,0],ants[:,1],marker='.',color='b')

plotBeam(spacing,numEl,waveL,0,phase_samp)
plotBeam(spacing,numEl,waveL,0.1,phase_samp)
plotBeam(spacing,numEl,waveL,0.2,phase_samp)
plotBeam(spacing,numEl,waveL,0.3,phase_samp)
plotBeam(spacing,numEl,waveL,0.4,phase_samp)
plotBeam(spacing,numEl,waveL,-0.1,phase_samp)
plotBeam(spacing,numEl,waveL,-0.2,phase_samp)
plotBeam(spacing,numEl,waveL,-0.3,phase_samp)
plotBeam(spacing,numEl,waveL,-0.4,phase_samp)
plotBeam(spacing,numEl,waveL,2*np.pi,phase_samp)