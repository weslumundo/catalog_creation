from reproject_sub import Reproject
import sys

#takes user input file names
file_ref = sys.argv[2]
file_targ = sys.argv[1]
file_out = sys.argv[3]

#reproject with the sci files using Reproject class
r_sci = Reproject(file_ref, file_targ, file_out)
r_sci.file_check()
r_sci.reprojector()
print("SCI files reprojected.")

#locate the wht files by changing the string Python looks for
wht_file_ref = file_ref.replace('_sci.fits','_wht.fits')
wht_file_targ = file_targ.replace('_sci.fits','_wht.fits')
wht_file_out = file_out.replace('_sci.fits','_wht.fits')

#Asks the user if they want WHT files reprojected
VALID = 0
while VALID == 0:
    user_response = input("Reproject associated WHT files? Y/N : ")
    user_response = user_response.upper()
    
    if user_response == "Y":
    
        #reproject with the wht files using Reproject class
        r_wht = Reproject(wht_file_ref, wht_file_targ, wht_file_out)
        r_wht.file_check()
        r_wht.reprojector()
        print("WHT files reprojected.")
        VALID = 1
        
    elif user_response == "N":
        VALID = 1
    
    else:
        print("Invalid entry, please enter Y or N.")

#asks the user if they want reference/output displayed 
VALID = 0
while VALID == 0:
    user_response = input("Display reprojected and reference images as comparison? Y/N : ")
    user_response = user_response.upper()
    
    if user_response == "Y":
    
        #displays images using Display class method
        r_sci.image_display()
        VALID = 1
        
    elif user_response == "N":
        VALID = 1
    
    else:
        print("Invalid entry, please enter Y or N.")        

        
print("Exit")
