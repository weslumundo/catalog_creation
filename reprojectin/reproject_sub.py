from astropy.io import fits
from reproject_display import Display
from reproject import reproject_interp
import os

class Reproject:
    def __init__(self, file_ref, file_targ, file_out):
        
        # stores user input file names as private members
        self._img_ref = file_ref
        self._img_targ = file_targ
        self._file_out = file_out
        # header name constants
        self._TO_CHANGE = ['WCSAXES', 'CRPIX1', 'CRPIX2', 'CRVAL1', 'CRVAL2', 'CTYPE1', 'CTYPE2', 'ORIENTAT', 'VAFACTOR', 'CD1_1', 'CD1_2', 'CD2_1', 'CD2_2']  
        
    def file_check(self): # makes sure entered files can be reprojected
        
        TO_CHECK = [self._img_ref, self._img_targ]
        cwd = os.getcwd() # gets user's current working directory
        
        for item in TO_CHECK:
            path = cwd + "\\" + item
            
            if os.path.isfile(path) == False: # checks if entered files exist in current working directory
                raise Exception ("File", item, " does not exist. Please make sure the file name is entered correctly.")
                
            name, extension = os.path.splitext(item)
            
        if extension != '.fits': # checks if entered files are .fits type
            raise Exception ("File", item, "is an incompatible type. Please only enter .fits files.")
    
    def image_display(self): #creates Display object and inputs file names, then calls display method
        
        print("Plotting images... This may take a few minutes.")
        disp = Display()
        disp.image_display(self._img_ref, self._file_out)
    
    def reprojector(self):
        
        print("Opening files...")
        self._img_ref = fits.open(self._img_ref)
        self._img_targ = fits.open(self._img_targ)
        print("Files opened.")
     
        print("Starting reproject_interp...")
        array_reproj, footprint_sci = reproject_interp(self._img_targ, self._img_ref[0].header)
        print("Finished reproject_interp.")
        
        #copies header data to be used in reprojected image
        targ_head = self._img_targ[0].header
        for item in self._TO_CHANGE:
            targ_head[item] = self._img_ref[0].header[item]
            
        fits.writeto(self._file_out, array_reproj, targ_head, overwrite=True)
        print("Reprojection complete!")
