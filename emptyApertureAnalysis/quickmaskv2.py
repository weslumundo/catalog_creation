import numpy as np
import os
import sys
import astropy
from astropy.io import fits

'''

PURPOSE

Create an image that is multipled by a mask whose zero values indicate
no data.  In practice, a generic routine that multiplies two FITS images

INPUT


Takes the object subtracted image produced by SExtractor and
multiplies it by the mask created by maskitextrav2.py.  The mask tells
where this is and is not data.

The input is not specific to a mask and image.  The variables in this
code just call them as such.

OUTPUT 

The output image is set to zero (using the no-data mask values)
wherever there is no data.


'''


def run(objsubFileLoc,maskFileLoc,objsubMaskFileLoc,ow = True):
	objsubim=objsubFileLoc
	maskim=maskFileLoc
	oshdu=astropy.io.fits.open(objsubim)
	maskhdu=astropy.io.fits.open(maskim)

	objsubdata=oshdu[0].data
	maskdata=maskhdu[0].data

	osmdata=objsubdata*maskdata
	hdout=fits.PrimaryHDU(osmdata,oshdu[0].header)
	#tmpfile=objsubim
	#tmplist=tmpfile.split('/')
	#tmpname=tmplist[len(tmplist)-1]
	#outname=tmpname.replace('.fits','')
	#newname=outname+'_maskd.fits'
	print("Writing ObjSubMask to ", objsubMaskFileLoc)
	hdout.writeto(objsubMaskFileLoc, overwrite = ow)
