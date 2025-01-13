"""
Ethan Jones
01/12/2025

Create a class that pulls data from google maps api.
"""
import os

class puller:

    def __init__(self):

        self.path = os.getcwd()

        pass
    
    def get_api(self):

        api_path = self.path + '/keys.txt'

        with open(api_path) as f:
            out = f.readlines()[1:]
        
        


        return out
