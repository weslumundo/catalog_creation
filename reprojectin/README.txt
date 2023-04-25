Last Updated March. 26, 2023

PURPOSE
   Creates a new image by reprojecting a reference image onto a target image.
Currently using reproject_interp module.

INPUT
   User inputs the file paths of the reference and target images, as well as
a name for the generated reprojection. Input files should be a SCI or WHT file.  

   The reprojection is performed using the WCS information in the FITS header and 
will only be as good as that information.  Therefore high astrometric accuracy
is required in the FITS header.

OUTPUT (more info needed)
   Outputs a SCI and WHT file for the generated reprojection. The output fits files
have the new header information.

DEPENDENCIES
   Requires Python modules astropy and reproject. Please make sure these modules are
present or install them using pip before running reproject_main.py.

==============================
TO USE
   Place files to reproject in the same folder as reproject_main.py. Make sure 
the files are not zipped and their names end in _sci.fits (e.g. example_sci.fits). If 
you have WHT files to reproject, move them to the same location and use the same 
names used for the SCI files, ending in _wht.fits (e.g. example_wht.fits). Run 
command reproject_main.py [target image] [reference image] [desired name of output] in
terminal, with the output name following the same naming convention (e.g. output_sci.fits).
   
NOTES
- reference and output display still needs work
- add example of how to run code here
- have system ask user if wht file names are correct
- update code comments!
