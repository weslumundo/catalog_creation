#		singleClusterError.py
#	Input:  target science file(reprojected and convoluted)
#		target weight file (reprojected)
#
#	#These outputs will be located in the same folder as the science file
#	Output: folder with output of empty apperature analysis for several apperature sizes
#		txt file with location of each of those apperatures
#		Segmentation Image
#		Mask Image

#for now lets assume this code is run off command line, with this format
# singleClusterError.py ScienceFileLocation
# we will use the folder the file is in as the output location
# we will use kmj's naming assumptions to find the weight file

#replace('_sci.fits','_wht.fits')
#NAMING ASSUMPTIONS:
#Science Files end in '_sci.fits'
#Weight Files are in the same directory and have the same exact name except for the ending
#Weight Files should end in '_wht.fits'
#The default_objsub_norm.sex is in the same folder as this file
#The exported version of maskitextra.py is in the same folder as this file

import sys
from astropy.io import fits
import maskitextrav2 as maskitextra
import os
import quickmaskv2 as quickmask

#define class for Error Generation
class singleClustorErr:
	#define variables here
	scienceFileLocation = ""
	weightFileLocation = ""
	scienceFile = 0
	weightFile = 0
	normalizedImageLocation = ""
	normalizedImage = 0
	objectSubImageLocation = ""
	objectSubImage = 0
	objectSubMaskImageLocation = ""
	objectSubMaskImage = 0
	maskImageLocation = ""
	maskImage = 0
	segmentationImageLocation = ""
	segmentationImage = 0
	outputDir = "" #output of eAA only
	outputBase = "" #base folder for everything
	outputLocation = ""
	outputTxtLocation = ""
	outputTxt = 0 
	objsubSex = ""
	
	#the self is some python witchcraft, just pretend it isnt there
	def __init__(self, myScienceFileLocation):
		#WES: consider adding code here to deal with files that have a different ending, like'_sci_reprj.fits'
		
		self.objsubSex = "default_objsub_norm.sex"
		
		
		#assign default values based on science file name
		self.scienceFileLocation = myScienceFileLocation
		self.weightFileLocation = myScienceFileLocation.replace('_sci.fits','_wht.fits')
		self.normalizedImageLocation = myScienceFileLocation.replace('_sci.fits','_nrm.fits')
		self.objectSubImageLocation = myScienceFileLocation.replace('_sci.fits','_objSub.fits')
		self.objectSubMaskImageLocation = myScienceFileLocation.replace('_sci.fits','_objSubMask.fits')
		self.maskImageLocation = myScienceFileLocation.replace('_sci.fits','_mask.fits')
		self.segmentationImageLocation = myScienceFileLocation.replace('_sci.fits','_seg.fits')
		self.outputTxtLocation = myScienceFileLocation.replace('_sci.fits','.txt')
		
		#we need the name of the cluster for the outputDir
		#split the filename at slashes and use the last piece
		#potential opsys conflict here, maybe this is just linux only code
		nameLocationList = myScienceFileLocation.split('/')
		#stole this idea from KMJ
		self.outputDir = nameLocationList[len(nameLocationList)-1].replace('_sci.fits','_apprFlux')
		#quickly find the 'root' folder
		myRoot = ""
		for i in range(0,len(nameLocationList)-1):
			myRoot += nameLocationList[i] + "/"
		self.outputBase = myRoot
		self.outputLocation = self.outputBase+self.outputDir+"/"

		
	#creates the Normalized and Masked files, if passed true it will overwrite at these locations	
	def generateNormal(self):
		#first step is to run maskitextra.py
		#this function takes the science and the weight files and generates a normalized image and a masked image at the locations passed into the function.
		maskitextra.run(self.scienceFileLocation,self.weightFileLocation,self.normalizedImageLocation,self.maskImageLocation)
	
	
	#create the ObjectSubtracted Image and the Segmentation Image and store them at their predefined locations.	
	def generateObjSub(self):	
		myCom = "sex" + " " + self.normalizedImageLocation + " -c " + self.objsubSex +" -CHECKIMAGE_NAME " + self.objectSubImageLocation + "," + self.segmentationImageLocation
		print(myCom)
		temp=os.system(myCom)  
	
	def generateObjSubMask(self):
		quickmask.run(self.objectSubImageLocation,self.maskImageLocation,self.objectSubMaskImageLocation)

myError = singleClustorErr(sys.argv[1])
#this is where the user has the chance to manually change any of the defaults defined in init 
myError.generateNormal()		
myError.generateObjSub()
myError.generateObjSubMask()
		
		
		
