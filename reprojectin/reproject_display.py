import os
import numpy as np
from astropy.visualization import simple_norm
from astropy.io import fits
from matplotlib import pyplot as plt

class Display:
    def __init__(self):
        pass
    #class exists to use image_display method, doesn't need any attributes

    def _add_plot(self, fig, pos, data, norm, shape):
        #internal method, generates a new plot in the figure using input position and data points
        
        fig.add_subplot(pos)  
        plt.imshow(data, 'viridis', norm=norm, origin='lower')
        
        if shape == 'default':
            #displays the full image
            
            plt.xticks(np.arange(0, data.shape[0], step = 1000), fontsize = 6)
            plt.yticks(np.arange(0, data.shape[1], step = 1000), fontsize = 6)
            
        elif shape == 'center':
            #displays a 200x200px zoom centered at the image center
            
            applied_shape = []
            for i in data.shape:
                #divides image size in half to find center value, then writes new image bounds
                
                temp = i//2
                applied_shape.append(temp-100)
                applied_shape.append(temp+100)
            
            #limits image to desired shape
            plt.xlim(applied_shape[0], applied_shape[1])
            plt.ylim(applied_shape[2], applied_shape[3])
            plt.xticks(np.arange(applied_shape[0], applied_shape [1], step = 25), fontsize = 6)
            plt.yticks(np.arange(applied_shape[2], applied_shape [3], step = 25), fontsize = 6)
            
        else:
           #displays a 200x200px zoom off-center as different sample
            
            applied_shape = []
            for i in data.shape:
                #divides image size in half to find center value, then writes new image bounds
                
                temp = i//2
                applied_shape.append(temp-200)
                applied_shape.append(temp)
                
            #limits image to desired shape
            plt.xlim(applied_shape[0], applied_shape[1])
            plt.ylim(applied_shape[2], applied_shape[3])
            plt.xticks(np.arange(applied_shape[0], applied_shape [1], step = 25), fontsize = 6)
            plt.yticks(np.arange(applied_shape[2], applied_shape [3], step = 25), fontsize = 6)
            
        plt.grid(linewidth = 0.5)
        plt.clim(0,0.2)
    
    def image_display(self, file_ref, file_out):

        fig = plt.figure(figsize=(10,10))
        
        ref_data = fits.getdata(file_ref)
        out_data = fits.getdata(file_out)

        ref_norm = simple_norm(ref_data,'asinh', max_percent=95)
        out_norm = simple_norm(out_data,'asinh', max_percent=95)
        
        #top left
        self._add_plot(fig, 231, ref_data, ref_norm, 'default')
        plt.title('Full Reference', fontsize=8)
        
        #bottom left
        self._add_plot(fig, 234, out_data, out_norm, 'default')
        plt.title('Full Output', fontsize=8)
        plt.clim(0,0.1)
        
        #top middle
        self._add_plot(fig, 232, ref_data, ref_norm, 'center')
        plt.title('200x200px Reference, Centered', fontsize=8)
        
        #bottom middle
        self._add_plot(fig, 235, out_data, out_norm, 'center')
        plt.title('200x200px Output, Centered', fontsize=8)
        plt.clim(0,0.1)
        
        #top right
        self._add_plot(fig, 233, ref_data, ref_norm, 'offcenter')
        plt.title('200x200px Reference, Off-center', fontsize=8)
        
        #bottom right
        self._add_plot(fig, 236, out_data, out_norm, 'offcenter')
        plt.title('200x200px Output, Off-center', fontsize=8)
        plt.clim(0,0.1)
        
        #fix spacing to prevent image overlap
        plt.subplots_adjust(bottom=0.1, top=0.9, hspace=0.32)
        plt.show()
