"""
Ethan Jones
01/12/2025

Create a class that pulls data from google maps api.

"""
import os
import time
import requests
from PIL import Image

class Puller:

    def __init__(self):

        self.path = os.getcwd()

        pass
    
    def get_api(self):

        api_path = self.path + '/keys.txt'

        with open(api_path) as f:
            out = f.readlines()[1:]

        return out[0]
    
    def get_coordinate_list(self,top_right,bottom_left):
        """
        Based on coordinates provided create a list of tupples for lat/lon. 

        Args:
            All attributes specified in class.
        """

        # Create lat/lon Values
        lat_top_right = float(top_right[0])
        lon_top_right = float(top_right[1])
        lat_btm_left = float(bottom_left[0])
        lon_btm_left  = float(bottom_left[1])

         # Start with top right point
        lat_lon_returned = []
        i,ii=  lat_top_right,lon_top_right 
        
        # Run until the lat/lon are less than the bottom left corner
        while i > lat_btm_left or ii > lon_btm_left:

            # Start at the right
            ii = lon_top_right
            

            # Run until all the way to left
            while ii > lon_btm_left:
            
                # One step to left
                ii = ii - 0.00019

                # Return data
                tup = (str(i),str(ii))
                lat_lon_returned.append(tup)
        
            # One step down
            i = i - 0.00017

        return lat_lon_returned
    
    def request_image(self,coordinates):
        """

        """
        
        # call api key
        key = self.get_api()

        # handel singular value
        if len(coordinates) == 1:

            # set the name for locally saving file
            lat_name,lon_name = point[0].replace(".","_"), point[1].replace("-","_").replace(".","_")

            # set path
            path_ = self.path + '/images'
            path_ = path_ + f'/park_{lat_name}_{lon_name}.png'

            # set url
            url = f'https://maps.googleapis.com/maps/api/staticmap?center={point[0]},{point[1]}&zoom=21&size=800x800&maptype=satellite&key={key}'
                        
            with Image.open(requests.get(url, stream=True).raw) as img:
                img.save(fp = path_, format = f'png')

        # handel list
        else:
            for point in coordinates:
                try:

                    # set the name for locally saving file
                    lat_name,lon_name = point[0].replace(".","_"),point[1].replace("-","_").replace(".","_")

                    # set path
                    path_ = self.path + '/data/images'
                    path_ = path_ + f'/park_{lat_name}_{lon_name}.png'

                    print(path_)

                    # set url
                    url = f'https://maps.googleapis.com/maps/api/staticmap?center={point[0]},{point[1]}&zoom=21&size=800x800&maptype=satellite&key={key}'
                        
                    with Image.open(requests.get(url, stream=True).raw) as img:
                        img.save(fp = path_, format = f'png')
                    
                    time.sleep(5)

                except:
                    print(f"failed at {point}")
