Last Updated March. 2, 2023

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
   
NOTES
- needs error handling for bad files/incompatible file types/no wht files found
- build a flag into method that lets user optionally plot the reference and
  target side-by-side to check effectiveness
- push file for difference image creation
