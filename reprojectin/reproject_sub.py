from astropy.io import fits
from reproject import reproject_interp

class Reproject:
    def __init__(self, file_ref, file_targ, file_out):
        
        # stores user input file names as private members
        self._img_ref = file_ref
        self._img_targ = file_targ
        self._file_out = file_out
        # header name constants
        self._TO_CHANGE = ['WCSAXES', 'CRPIX1', 'CRPIX2', 'CRVAL1', 'CRVAL2', 'CTYPE1', 'CTYPE2', 'ORIENTAT', 'VAFACTOR', 'CD1_1', 'CD1_2', 'CD2_1', 'CD2_2']    
    
    def reprojector(self): #DE - add error handling for bad input
        
        print("Opening files...")
        self._img_ref = fits.open(self._img_ref)
        self._img_targ = fits.open(self._img_targ)
        print("Files opened.")
        
        # currently using reproject_interp, can be changed to use reproject_exact later
        print("Starting reproject_interp...")
        array_reproj, footprint_sci = reproject_interp(self._img_targ, self._img_ref[0].header)
        print("Finished reproject_interp.")
        
        #copies header data to be used in reprojected image.
        #header is copied from target image and only changed WCS values are updated
        targ_head = self._img_targ[0].header
        for item in self._TO_CHANGE:
            targ_head[item] = self._img_ref[0].header[item]
            
        #writes out reprojected image and updated header    
        fits.writeto(self._file_out, array_reproj, targ_head, overwrite=True)
        print("Reprojection complete!")
