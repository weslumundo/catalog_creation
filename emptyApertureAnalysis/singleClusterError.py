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
#Assumes the user wants the txt file in the directory that outputBase points toward(sci file root), not the directory in the txtLocationVariable [THIS SHOULD BE CHANGED]


import sys
from astropy.io import fits
import maskitextrav2 as maskitextra
import os
import quickmaskv2 as quickmask
import runEAAfunc as runEAA
sys.path.append('../depthcalculation/')
import workingDepthSingle

#define class for Error Generation
class singleClustorErr:
	#define variables here
	scienceFileLocation = ""
	weightFileLocation = ""
	normalizedImageLocation = ""
	objectSubImageLocation = ""
	objectSubMaskImageLocation = ""
	maskImageLocation = ""
	segmentationImageLocation = ""
	apprFluxName = "" #base name for apprFlux files
	outputBase = "" #base folder for everything
	#outputLocation = ""
	outputTxtLocation = ""
	outputTxtName = ""
	objsubSex = ""
	pixScale = 0.1
	cvalues = 0
	baseName=""
	cvaluesLocation = ""
	
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
		self.outputTxtLocation = myScienceFileLocation.replace('_sci.fits','_apprFlux.txt')
		self.graphLocation = myScienceFileLocation.replace('_sci.fits','_fig')
		
		#we need the name of the cluster for the apprFluxName
		#split the filename at slashes and use the last piece
		#potential opsys conflict here, maybe this is just linux only code
		nameLocationList = myScienceFileLocation.split('/')
		#stole this idea from KMJ
		self.apprFluxName = nameLocationList[len(nameLocationList)-1].replace('_sci.fits','_apprFlux')
		self.outputTxtName = nameLocationList[len(nameLocationList)-1].replace('_sci.fits','_apprFlux.txt')
		
		self.baseName = nameLocationList[len(nameLocationList)-1].replace('_sci.fits','')
		cName = nameLocationList[len(nameLocationList)-1].replace('_sci.fits','_cvalues.txt')
		 
		#quickly find the 'root' folder
		myRoot = ""
		for i in range(0,len(nameLocationList)-1):
			myRoot += nameLocationList[i] + "/"
		self.outputBase = myRoot
		#self.outputLocation = self.outputBase+self.apprFluxName+"/"
		
		#attach cvaluelocation to output folder
		self.cvaluesLocation = self.outputBase + cName
		

		
	#creates the Normalized and Masked files, if passed true it will overwrite at these locations	
	def generateNormal(self):
		#first step is to run maskitextra.py
		#this function takes the science and the weight files and generates a normalized image and a masked image at the locations passed into the function.
		maskitextra.run(self.scienceFileLocation,self.weightFileLocation,self.normalizedImageLocation,self.maskImageLocation)
	
	
	#create the ObjectSubtracted Image and the Segmentation Image and store them at their predefined locations.	
	def generateObjSub(self):
		#this is the source extractor comand to generate an ObjSub image and a SegImage	
		myCom = "sex" + " " + self.normalizedImageLocation + " -c " + self.objsubSex +" -CHECKIMAGE_NAME " + self.objectSubImageLocation + "," + self.segmentationImageLocation
		print(myCom)
		temp=os.system(myCom)  
	
	def generateObjSubMask(self):
		quickmask.run(self.objectSubImageLocation,self.maskImageLocation,self.objectSubMaskImageLocation)

	def setPixScale(self, scale):
		self.pixScale = scale
	
	def setObjSex(self, name):
		self.objsubSex = name
		
	def startEAA(self):
		runEAA.run(self.objectSubMaskImageLocation,self.apprFluxName,self.pixScale)

	def generateTxt(self):
		#TODO: come up with a better solution
		myCom = "ls $PWD/aperflux/"+self.apprFluxName+"_emptyaperflux_*.dat >"+self.outputTxtName
		myComRM = "rm " +self.outputBase+self.outputTxtName
		myCom2 = "mv "+self.outputTxtName+" "+self.outputBase
		temp=os.system(myCom)
		temp=os.system(myComRM)
		temp=os.system(myCom2) 
		
	def generateC(self):
		self.cvalues =  workingDepthSingle.run(self.scienceFileLocation,self.outputTxtLocation,self.pixScale,self.maskImageLocation,self.segmentationImageLocation,self.graphLocation)
		

	def begin(self):
		#This function autoruns the singleClusterErr process
		self.preEAA()
		self.startEAA()
		self.postEAA()
		print("---Finished---")
		
	def preEAA(self):
		self.generateNormal()		
		self.generateObjSub()
		self.generateObjSubMask()
	
	def postEAA(self):
		self.generateTxt()
		self.generateC() 
		self.outputC()
		
	def genText(self):
		#TODO: check for existing data
		#creates the contents of the cvalue output file
		mySciFile=fits.open(myError.scienceFileLocation)
		myHeader=mySciFile[0].header	
		myOut  = ""
		myOut += "Name\t"+self.baseName+'\n'
		myOut += "c0\t"+str(self.cvalues.c0.value)+'\n'
		myOut += "c1\t"+str(self.cvalues.c1.value)+'\n'
		myOut += "c2\t"+str(self.cvalues.c2.value)+'\n'
		myOut += "exptime\t"+str(round(myHeader['EXPTIME']))+'\n'
		myOut += "cluster\t"+myHeader['TARGNAME']+'\n'
		myOut += "band\t"+myHeader['FILTER']+'\n'
		return myOut

	def outputC(self):
		myFile = open(self.cvaluesLocation,"w")
		myFile.write(self.genText())
		myFile.close()

myError = singleClustorErr(sys.argv[1])
#this is where the user has the chance to manually change any of the defaults defined in init 

#program expects sciencefile pixscale sexfile in that order

#did user provid pixscale?
if(len(sys.argv)>2):
	myError.setPixScale(sys.argv[2])
else:
	#if no set default
	myError.setPixScale(0.1)

#did user provide sexfile?
if(len(sys.argv)>3):
	myError.setObjSex(sys.argv[3])
	#if no default already set elsewhere

myError.begin()
	
#TESTING
#myError.postEAA()
#myError.scienceFileLocation = 0

	
		
		
