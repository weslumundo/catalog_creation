from reproject_sub import Reproject
import sys

#takes user input file names
file_ref = sys.argv[2]
file_targ = sys.argv[1]
file_out = sys.argv[3]

#reproject with the sci files using Reproject class
r_sci = Reproject(file_ref, file_targ, file_out)
r_sci.reprojector()

#locate the wht files by changing the string Python looks for
wht_file_ref = file_ref.replace('_sci.fits','_wht.fits')
wht_file_targ = file_targ.replace('_sci.fits','_wht.fits')
wht_file_out = file_out.replace('_sci.fits','_wht.fits')

#reproject with the wht files using Reproject class
r_wht = Reproject(wht_file_ref, wht_file_targ, wht_file_out)
r_wht.reprojector()
