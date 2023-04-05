'''
Purpose

Prosess the output of EAA

Inputs
sciFileLoc = location of science file

txtFileLoc = location of a txt file containg the locations of EAA output

myPixScale = pixel scale in arcsec/pixel

maskFileLoc = location of mask file created by maskitextra in generateNormal 

segFileLoc = location of segmentation image created by source extractor

graphOutputLoc = location + basename of all graph outputs
ie. /home/graphs/fig will put all graphs in folder /home/graphs and all graphs will have names like fig1.png or fig_sig.png

Output
GRAPHOUTPUTNAME#.png
collection of graphs showing a histogram of fluxes and the corresponding gaussian overlayed

GRAPHOUTPUTNAME_gaussian_analysis.png
all gaussians normalized to 1 displayed on the same graph

GRAPHOUTPUTNAME_sig.png
Graph showing the average uncertianty for each apperture size and the polynomial described by the cvalues  

'''
#Goal of this file

#convert Working_Depth.ipynb
#output C1 and C2 values for error calculation

#Cell 1
#imports
import numpy as np
import math
import astropy.table
import matplotlib as mpl
import matplotlib.pyplot as plt
import os,random,time
import matplotlib.backends.backend_pdf
from matplotlib.backends.backend_pdf import PdfPages
from astropy.io import fits
import scipy.stats as ss
from astropy.modeling import models, fitting
import sys
from array import array
import pylab as pl
from IPython.display import IFrame
import depthcalc
import calculatin as calc
from scipy.stats import norm

def gaussian(x, mu, sig):
	#calculate simple gaussian
	myret = np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
	#return (myret/(sig*math.sqrt(2*math.pi)))
	return myret

#Cell2 
#this cell is mostly file declarations but singleCluster knows these so skip
#sciFileLoc = string of location of target science file
#txtFileLoc = string of location of runEAA output for target scifile
#myPixScale = pixel scale as an int
def run(sciFileLoc,txtFileLoc,myPixScale,maskFileLoc,segFileLoc,graphOutputLoc):
	filenames=np.loadtxt(txtFileLoc,dtype='str')
	hdu=fits.open(sciFileLoc)
	hdr=hdu[0].header
	holdphots=[hdr['PHOTFLAM'],hdr['PHOTPLAM']]
	hdu.close()
	
	apers=np.array([0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
	aper = 0.5*apers/myPixScale
	
	mags=[]
	sigs=[]
	means=[]
	factor=[]
	
	globalMax = 0
	count = 0 #keep track of the number of figures made
	
	for x in filenames:
	#    infile='../emptyApertureAnalysis_share/aperflux/'+str(x)
		infile=str(x)
		mag,sig,mean=depthcalc.depth(infile,holdphots)
		mags.append(mag)
		sigs.append(sig)
		means.append(mean)
		flux=depthcalc.depthFlux(infile,holdphots)
		rangeval=max([-min(flux),max(flux)])
		globalMax=max(globalMax,rangeval)
		bins = np.linspace(-rangeval, rangeval, 100)
		(n, bins2, patches) = plt.hist(flux, bins.copy(), alpha=0.5, label='y')
		#TODO: normalize the gaussian
		plt.plot(bins.copy(),max(n)*gaussian(bins.copy(), mean, sig))
		factor.append(max(n))
		plt.xlim((-1,1))
		plt.ylim((0,100))
		plt.legend(loc='upper right')
		plt.title('Fluxes in Apperatures of size '+str(aper[count]))
		count+=1
		plt.xlabel('Flux (e-/s)')
		plt.ylabel('Number')
		plt.savefig(graphOutputLoc+str(count)+".png")
		plt.clf()
	
	print("Generating Gaussians")	
	plt.legend(loc='upper right')
	plt.title('Compilation of all Gausians')
	bins = np.linspace(-globalMax, globalMax, 100)
	for i in range(0,len(means)):
		plt.plot(bins,gaussian(bins.copy(), means[i], sigs[i]))
	plt.savefig(graphOutputLoc+"_gaus_analysis"+".png")
	plt.clf()
    	
    	#calculate the RMS of the original science images
	rmss,aper1=depthcalc.rmscalc(sciFileLoc,maskFileLoc,segFileLoc,apers,myPixScale)
	rmsvals=rmss*aper1
	print('RMS of sci image',rmss)

    	
    	#CELL 4 
	modelb=models.Polynomial1D(degree=2,c0=0.0)
	modelb.c0.fixed=True
	fitter_poly=fitting.LinearLSQFitter()
	best_blue=fitter_poly(modelb,aper,sigs)
	print('2nd order polynomial for cluster image')
	print(best_blue)
    		
    	#CELL 3
    	
    	#generate a sigma v apperature pixle size plot
	plt.plot(aper1,sigs,'r*',label='STDEV of actual aperture data')
	plt.plot(aper1,best_blue(aper1),color='y',label='best fit using c values')
	plt.title('Sigma vs linear size')
	plt.xlabel('Linear size (pixels)')
	plt.ylabel('Sigma (e-/s)')
	plt.legend(loc='upper left')
	#plt.yscale('log')
	plt.ylim(bottom=0,top=0.5)
	#plt.xlim(left=0,right=100)
	
	#save fig and return c vals
	plt.savefig(graphOutputLoc+"_sig.png")
	#plt.show()

	#clear plot
	plt.clf()

	#plot histagrams of apperature flux

	#return c vals	
	return best_blue
    		
    		
