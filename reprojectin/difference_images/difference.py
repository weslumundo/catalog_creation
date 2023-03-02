from astropy.io import fits
import sys

def main():
    img1 = sys.argv[1]
    img2 = sys.argv[2]
    fd = fits.FITSdiff(img1, img2)
    print(fits.report())
    
main()