import numpy as np
from reproject import reproject_exact
import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.convolution import Gaussian2DKernel
from astropy.convolution import convolve
import sys

fileblue=sys.argv[1]
filered=sys.argv[2]
fileout=sys.argv[3]
print("Opening a file\n")
print(filered)
hrp=fits.open(filered)
print("Opening a file\n")
print(fileblue)
hop=fits.open(fileblue)
print("Starting reproject_exact\n")
array2,footprint1= reproject_exact(hop,hrp[0].header)
print("Finished reproject_exact\n")

fits.writeto(fileout, array2, hrp[0].header, overwrite=True)
print('done reprojectin sci')


tmpblue=fileblue
tmplist=tmpblue.split('/')
tmpname=tmplist[len(tmplist)-1]
whtfileblue=tmpname.replace('_sci.fits','_wht.fits')

tmpred=filered
tmprlist=tmpred.split('/')
tmprname=tmprlist[len(tmprlist)-1]
whtfilered=tmprname.replace('_sci.fits','_wht.fits')


tmpo=fileout
tmpolist=tmpo.split('/')
tmponame=tmpolist[len(tmpolist)-1]
outwht=tmponame.replace('.fits','_wht.fits')

print("Opening a file\n")
print(whtfileblue)
wb=fits.open(whtfileblue)
print("Opening a file\n")
print(whtfilered)
wr=fits.open(whtfilered)
whtarray2,footprintwht=reproject_exact(wb,wr[0].header)
fits.writeto(outwht,whtarray2,wr[0].header,overwrite=True)
print('done reprojectin wht')
