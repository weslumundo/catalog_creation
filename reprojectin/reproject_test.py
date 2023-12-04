
from _test_sub import Catalogs
#from regions import Regions


# extract two catalogs- one from the reprojection, one from the reference
# i think these output as astropy tables

# REMEMBER- calculations are on pg. 12 of stuff notebook
# red/targ/reprojected img
# psf = 0.3063arcsec
# px per arcsec = 1px/0.1000008arcsec
# psf in px = 3.0635px

#blue/ref img
# psf = 0.1326arcsec
# px per arcsec = 1px/0.0500004arcsec
# psf in px = 2.6521px

ref = Catalogs()
rep = Catalogs()

ref_sources = ref.make_cat('j020548m5829-f606w_drc_sci.fits', 2.6521)
print('Reference sources found.')
#reproj_sources = rep.make_cat('reproject-output2_sci.fits', 3.0635)
#print('Reprojected sources found.')

#i can save these as fits files

#ref.source_check('ref_sources_deblendtest.reg', 20, 'j020548m5829-f606w_drc_wht.fits')
#print('DS9 regions file for reference sources created.')
#rep.source_check('reproj_regions.reg', 20)
#print('DS9 regions file for reprojected sources created.')

match = ref.matching(ref_sources)

# for every source in the reference img, find closest source in x-y position
# in the reprojection

# nested for loop (CLASS METHOD)
    #for item in list 1
        #for item in list 2
        # if it matches list 1, save matches to new txt file (or table)
        # and remove item from list 2. then break so list 1 moves to the next item
        
# select by parameter. for item in result (CLASS METHOD) 
#   loop thru results of last process, copy and save matches w/in
#   parameters (starting w/ 2arcsec) to Another new list (or table)

#make set of 4 plots- handle this after catalog creation and matching works


