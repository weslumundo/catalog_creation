Last Updated Nov. 29, 2022

PURPOSE
   Creates a new image by reprojecting a reference image onto a target image.
Currently using reproject_interp module.

INPUT
   User inputs the file paths of the reference and target images, as well as
a name for the generated reprojection. All inputs must be .sci files.

OUTPUT (more info needed)
   Outputs a .sci and .wht file for the generated reprojection.

NOTES
- needs error handling for bad files/incompatible file types/no wht files found
- build a flag into method that lets user optionally plot the reference and
  target side-by-side to check effectiveness 
