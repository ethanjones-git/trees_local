import os 
import csv

class XmlAdder:
    '''
    When annotating, xml files were not created for files that didn't get annotations.

    These will all be fed into the machine. It's importatnt to create empty files when
    something wasn't annotated.

    '''

    def __init__(self,path):

        # directory these will be applied to
        self.path = path

    def index_current_xml(self):

        # instantiate file name list
        lst = []

        # give list of images
        xml_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.xml')]
        
        if xml_files:
            print("Found XML files:")
            for file in xml_files:
                lst.append(file)
        else:
            print("No XML files found in the folder.")

        # save csv

        # location of csv
        meta_data = '/Users/ethanjones/projects/trees_local/data/meta_data/xml_index.csv'

        # write csv
        with open(meta_data, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Filename"])  # Optional header
            for item in lst:
                writer.writerow([item])
        
    
    def index_return(self):
        pass

        # pulls index
    
# note all xml files that exist
# if it's missing create an xml file
# create a condition to remove all empty xml files.
# need to create xml files for all data that's missing
