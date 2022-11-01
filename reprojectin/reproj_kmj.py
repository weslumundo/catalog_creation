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
#11/1/22
#GHR - not sure why these are indexed 1,2,3 and not 0,1,2
#GHR - change variable names to be "reference" and "target" where
#"reference" is the image that contains the pixel grid we want to
#match to and "target" is the object we will be transforming.
fileblue=sys.argv[1]   #short wavelength image - change to "target"
filered=sys.argv[2]   #long wavelength image - change to "reference", e.g. fileref and file targ
fileout=sys.argv[3]    #output image
print("Opening a file")
print(filered)
hrp=fits.open(filered)
print("Opening a file")
print(fileblue)
hop=fits.open(fileblue)

#do the reprojecting
#This takes the hop image and reprojects it to match the hrp header.  
print("Starting reproject_exact")
array2,footprint1= reproject_exact(hop,hrp[0].header)
print("Finished reproject_exact")

#this outputs the reprojected image .  It currently writes the red header to the reprojected file
#we need to:
#1. copy the blue header to a new structure
#2. replace the WCS keywords with those from the red header
#3. use this new header as the one we write to the file.  This preserves all of the filter-specific
#information but includes the right WCS header keywords
#We want to replace the following header keywords: WCSAXES, CRPIX1, CRPIX2, CRVAL1, CRVAL2, CTYPE1, CTYPE2, ORIENTAT, VAFACTOR, CD1_1, CD1_2, CD2_1, CD2_2
#for example, hrp[0].header['CD1_1'] contains the value for that header item
#copy the header
bucket=hop[0].header
#These are the columns to change
toChange=['WCSAXES', 'CRPIX1', 'CRPIX2', 'CRVAL1', 'CRVAL2', 'CTYPE1', 'CTYPE2', 'ORIENTAT', 'VAFACTOR', 'CD1_1', 'CD1_2', 'CD2_1', 'CD2_2']
for i in toChange:
    bucket[i]=hrp[0].header[i]

#write out the new reprojected array (array2) to a fits file using the original header with the modified WCS keywords that now match the reference header
fits.writeto(fileout, array2, bucket, overwrite=True)
print('done reprojectin sci')

####Now do the transformation for the weight files
#GHR - not sure if it necessary to rename fileblue to tmpblue since replace (below) shouldn't modify the original filename it is applied to
tmpblue=fileblue
#tmplist=tmpblue.split('/')
#tmpname=tmplist[len(tmplist)-1]
#whtfileblue=tmpname.replace('_sci.fits','_wht.fits')

#GHR - makes a new file name replacing the "sci" extension with a
#"wht" extension.  This is there so that we don't need to give the wht
#file on input but can make it from the name of the science file.
#This assumes that they have the same root.
#target
whtfileblue=tmpblue.replace('_sci.fits','_wht.fits')

#reference
tmpred=filered
#tmprlist=tmpred.split('/')
#tmprname=tmprlist[len(tmprlist)-1]
#whtfilered=tmprname.replace('_sci.fits','_wht.fits')
whtfilered=tmpred.replace('_sci.fits','_wht.fits')

#GHR - I am not sure why she splits the filename for the weight file
#and not for the image file.  Seems you don't need this as long as the
#path is given on input for all files.

#this makes a new output file
tmpo=fileout
#split path up into individual directories
tmpolist=tmpo.split('/')
#pick the last element in that list as the filename
tmponame=tmpolist[len(tmpolist)-1]
#make new filename
outwht=tmponame.replace('.fits','_wht.fits')

#repeats the same steps as for the science image.
print("Opening a file")
print(whtfileblue)
wb=fits.open(whtfileblue)
print("Opening a file")
print(whtfilered)
wr=fits.open(whtfilered)
whtarray2,footprintwht=reproject_exact(wb,wr[0].header)
#copy the blue header and overwrite some of the red header values onto it.
whtbucket=wb[0].header
for i in toChange:
    whtbucket[i]=wr[0].header[i]
fits.writeto(outwht,whtarray2,wr[0].header,overwrite=True)
print('done reprojectin wht')
