import numpy as np
import os
import sys
import astropy
from astropy.io import fits
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
