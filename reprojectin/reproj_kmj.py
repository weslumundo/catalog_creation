import numpy as np
from reproject import reproject_exact
import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.io import fits
from astropy.convolution import Gaussian2DKernel
from astropy.convolution import convolve
import sys

#reprojects a short wavelength ("blue") image onto a longer wavelength ("red") image
#reproject uses the image header to determine the reprojection, and so relies on
#an accurate WCS in both images

#takes three inputs at the command line
fileblue=sys.argv[1]   #short wavelength image
filered=sys.argv[2]   #long wavelenght image
fileout=sys.argv[3]    #output image
print("Opening a file")
print(filered)
hrp=fits.open(filered)
print("Opening a file")
print(fileblue)
hop=fits.open(fileblue)

#do the reprojecting
print("Starting reproject_exact")
array2,footprint1= reproject_exact(hop,hrp[0].header)
print("Finished reproject_exact")

#this outputs the reprojected image .  It currently writes the red header to the reprojected file
#we need to:
#1. copy the blue header to a new structure
#2. replace the WCS keywords with those from the red header
#3. use this new header as the one we write to the file.  This preserves all of the filter-specific
#information but includes the right header
#We want to replace the following header keywords: WCSAXES, CRPIX1, CRPIX2, CRVAL1, CRVAL2, CTYPE1, CTYPE2, ORIENTAT, VAFACTOR, CD1_1, CD1_2, CD2_1, CD2_2
#for example, hrp[0].header['CD1_1'] contains the value for that header item 
fits.writeto(fileout, array2, hrp[0].header, overwrite=True)
print('done reprojectin sci')


tmpblue=fileblue
#tmplist=tmpblue.split('/')
#tmpname=tmplist[len(tmplist)-1]
#whtfileblue=tmpname.replace('_sci.fits','_wht.fits')
whtfileblue=tmpblue.replace('_sci.fits','_wht.fits')

tmpred=filered
#tmprlist=tmpred.split('/')
#tmprname=tmprlist[len(tmprlist)-1]
#whtfilered=tmprname.replace('_sci.fits','_wht.fits')
whtfilered=tmpred.replace('_sci.fits','_wht.fits')

tmpo=fileout
tmpolist=tmpo.split('/')
tmponame=tmpolist[len(tmpolist)-1]
outwht=tmponame.replace('.fits','_wht.fits')

print("Opening a file")
print(whtfileblue)
wb=fits.open(whtfileblue)
print("Opening a file")
print(whtfilered)
wr=fits.open(whtfilered)
whtarray2,footprintwht=reproject_exact(wb,wr[0].header)
fits.writeto(outwht,whtarray2,wr[0].header,overwrite=True)
print('done reprojectin wht')
