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

#Cell2 
#this cell is mostly file declarations but singleCluster knows these so skip
#sciFileLoc = string of location of target science file
#txtFileLoc = string of location of runEAA output for target scifile
#myPixScale = pixel scale as an int
def run(sciFileLoc,txtFileLoc,myPixScale,maskFileLoc,segFileLoc):
	filenames=np.loadtxt(txtFileLoc,dtype='str')
	hdu=fits.open(sciFileLoc)
	hdr=hdu[0].header
	holdphots=[hdr['PHOTFLAM'],hdr['PHOTPLAM']]
	hdu.close()
	
	apers=np.array([0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
	aper = 0.5*apers/myPixScale
	
	mags=[]
	sigs=[]
	
	for x in filenames:
	#    infile='../emptyApertureAnalysis_share/aperflux/'+str(x)
    		infile=str(x)
    		mag,sig=depthcalc.depth(infile,holdphots)
    		mags.append(mag)
    		sigs.append(sig)
    		
    	#skip ploting
    	#CELL 3
    	    		
	rmss,aper1=depthcalc.rmscalc(sciFileLoc,maskFileLoc,segFileLoc,apers,myPixScale)
	rmsvals=rmss*aper1
	print('RMS of original sci image, redward',rmss)	
    	
    	#CELL 4 
	modelb=models.Polynomial1D(degree=2,c0=0.0)
	modelb.c0.fixed=True
	fitter_poly=fitting.LinearLSQFitter()
	best_blue=fitter_poly(modelb,aper,sigs)
	print('2nd order polynomial for cluster image')
	print(best_blue)
	return best_blue
    		
    		
