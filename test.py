
"""
Ethan Jones
01/12/2025

ML project, identifying trees in balboa park based on google maps api. Localized version.
Intented to be a small scale version of project. All data is locally stored. Baseline model is created and fit.

Purpose is to understand image pipeline details. Next iteration will leverage clould computing and databases.

To effectivley leverage those, and include considerations the current localized proof of concept is created.

-- Task 1: data creation module
params: api variable, number of images
action: call class with variable and images. Creates localized dataset.

-- Task 2: raw to processed data
params: dataset location
action: creates bounding boxes for trees, method for annotating tree type.
This will allow users to annotate tree types to feed into the model. 

-- Task 3: simple baseline model
params: dataset, annotations, model parameters
action: a simple baseline model is trained and tested on the dataset. 
"""

from data.data_puller import Puller
from data.data_prepper import XmlAdder


def BalboaParkPuller(start,stop):
    '''
    Get Coordinate List:
          This is an exuaghstive list for all of Balboa Park. This
          returns thousands of images. Since this is a localized
          version of the project, a limit for number of images, indicated by
          the start and stop parameters, are used.
    '''

    # call the puller
    puller = Puller()
    
    top_right,bottom_left = ('32.741004', '-117.149224'), ('32.737794', '-117.159011')
    out = puller.get_coordinate_list(top_right,bottom_left)

    # export images to the data/image file
    puller.request_image(out[start:stop])

def clean_data(data_folder,purge):

    # located the folder
    xa = XmlAdder(data_folder)

    if purge == True:
        
        # if needed, purge
        xa.purger() 
        
    else:
        
        # index the existing data
        xa.index_current_xml('xml_index_2025_03_15.csv')

        # add dummy xml files
        xa.creater()


start,stop = 500,510
#BalboaParkPuller(start,stop)
clean_data(data_folder = 'images',
           purge=False)

