import os
import numpy as np
from scipy.stats import scoreatpercentile
from astropy.visualization import simple_norm
from astropy.io import fits
from matplotlib import pyplot as plt

class Display:
    def __init__(self):
        pass
    #class exists to use image_display method, does not need any attributes
    
    def image_display(self,file_ref,file_out):

        #reads in file data 
        ref_data = fits.getdata(file_ref)
        out_data = fits.getdata(file_out)
        
        #plots reference image 
        plt.subplot(211)
        norm = simple_norm(ref_data,'asinh', max_percent=95)
        plt.imshow(ref_data,'viridis',origin='lower',norm=norm)
        plt.title("Reference Image")
        plt.clim(0,0.2)
        
        #plots output image
        plt.subplot(212)
        norm = simple_norm(out_data,'asinh',max_percent=95)
        plt.imshow(out_data,'viridis',origin='lower',norm=norm)
        plt.title("Reprojected Output")
        plt.clim(0,0.2)
        
        #plots colorbar
        plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9, hspace=0.32)
        cax = plt.axes([0.70, 0.1, 0.075, 0.8])
        plt.colorbar(cax=cax)
        
        plt.show()