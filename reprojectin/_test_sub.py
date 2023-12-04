
from astropy.io import fits
from astropy.convolution import convolve
from astropy.coordinates import SkyCoord
from astropy.table import Table
import astropy.units as u
import math
import numpy as np
from photutils.background import Background2D, MedianBackground
from photutils.segmentation import SourceCatalog, SourceFinder, make_2dgaussian_kernel




class Catalogs:
    def __init__(self):
        pass

    def make_cat(self, filename, psf): #take input file paths and calc'd psf
        with fits.open(filename) as hdul:
            self.data = hdul[0].data

            # produce a background and background noise image
            bkg_estimator = MedianBackground()
            bkg = Background2D(self.data, (50,50), filter_size=(3,3), bkg_estimator=bkg_estimator)
            self.subt_data = self.data - bkg.background # save the cleaned data for easy access
            
            threshold = 1.5*bkg.background_rms # detection threshold

            # convolve data
            kernel = make_2dgaussian_kernel(psf, size=5) # changed FWHM=3.0 to the psf per image
            self.convolved_data = convolve(self.subt_data, kernel)
            
            # finds and deblends sources
            finder = SourceFinder(npixels=10, deblend=True, nlevels=32, contrast=0.3, progress_bar=False)
            segment_map = finder(self.convolved_data, threshold)
            
            # generate and return catalog
            cat = SourceCatalog(self.subt_data, segment_map, convolved_data=self.convolved_data)
            self.sources = cat.to_table()
        return self.sources
    
    def _pull_wht(self, filename_wht): 
        with fits.open(filename_wht) as hdul: # open the wht file
            wht_data = hdul[0].data # get wht data as an array
            dmax = np.max(wht_data) # get the max value
            exptime_map = wht_data/dmax # gives a map of values 0-1, effective exposure time map
        whts = [] # empty list to store wht values
        for obj in self.sources: # go through every detected source
            obj_x = round(obj['xcentroid']) - 1 # match the detected source with its wht
            obj_y = round(obj['ycentroid']) - 1
            wht_val = exptime_map[obj_y][obj_x] # add the wht to the list
            whts.append(wht_val)
            
        self.sources['exptime'] = whts # add all whts to a new column describing relative exposure time
        print('Exposure times added to catalogue.')


    def matching(self, ref_cat):   
        ref_coordcat = SkyCoord(ra=ref_cat['xcentroid'],dec=ref_cat['ycentroid'])
        print(ref_coordcat)
    
    def source_check(self, filename, rad, filename_wht):
        with open(filename, 'w') as file:
            file.write('# Region file format: DS9 version 4.1\n')
            file.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n')
            file.write('physical\n')
            self._pull_wht(filename_wht) # get exposure times for all sources
            row_idx = 0
            for row in self.sources:
                if self.sources['exptime'][row_idx] > 0.05: # removes false detections caused by noise
                    x = self.sources['xcentroid'][row_idx]
                    y = self.sources['ycentroid'][row_idx]
                    line = 'circle('+str(x)+','+str(y)+','+str(rad)+')\n'
                    file.write(line)
                row_idx += 1

            
        