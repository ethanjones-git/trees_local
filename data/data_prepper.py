import os 
import csv
import pandas as pd
import datetime
import xml.etree.ElementTree as ET


class XmlAdder:
    '''
    When annotating, xml files were not created for files that didn't get annotations.

    These will all be fed into the machine. It's importatnt to create empty files when
    something wasn't annotated.

    '''

    def __init__(self,file):

        self.image_folder_path = os.getcwd() + f'/data/{file}'
        
        pass 

    def index_current_xml(self,meta_data_title):

        
        # instantiate file name list
        lst = []

        # give list of images
        xml_files = [f for f in os.listdir(self.image_folder_path) if f.lower().endswith('.xml')]
        
        if xml_files:
            print("Found XML files:")
            for file in xml_files:
                lst.append(file)
        else:
            print("No XML files found in the folder.")

        # save csv

        # location of csv
        meta_data = f'/Users/ethanjones/projects/trees_local/data/meta_data/{meta_data_title}'

        # write csv
        with open(meta_data, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Filename"])  # Optional header
            for item in lst:
                writer.writerow([item])
        
    
    def index_return(self):
        folder_path = os.getcwd() + '/data/meta_data/xml_index.csv'
        
        df = pd.read_csv(folder_path)
        
        return df
    
    def create_empty_xml(self, image_path, xml_path):
        """
        Creates an empty XML file with a structured annotation template.
        :param image_path: Path to the image file.
        :param xml_path: Path where the XML file will be created.
        """

        image_name = os.path.basename(image_path)
        
        annotation = ET.Element("annotation")

        folder = ET.SubElement(annotation, "folder")
        folder.text = os.path.dirname(image_path)

        filename = ET.SubElement(annotation, "filename")
        filename.text = image_name

        path = ET.SubElement(annotation, "path")
        path.text = image_path

        source = ET.SubElement(annotation, "source")
        database = ET.SubElement(source, "database")
        database.text = "Unknown"

        size = ET.SubElement(annotation, "size")
        width = ET.SubElement(size, "width")
        width.text = "0"
        height = ET.SubElement(size, "height")
        height.text = "0"
        depth = ET.SubElement(size, "depth")
        depth.text = "0"

        segmented = ET.SubElement(annotation, "segmented")
        segmented.text = "0"

        # Write XML to file
        tree = ET.ElementTree(annotation)
        with open(xml_path, "wb") as xml_file:
            tree.write(xml_file, encoding="utf-8", xml_declaration=False)

        print(f"Created empty XML file: {xml_path}")
    
    def creater(self):
        """
        Goes through a folder, ensures each .png file has a corresponding .xml file.
        If an XML file is missing, it creates a structured empty XML.
        
        :param folder_path: Path to the folder containing .png files.
        """
        folder_path = self.image_folder_path 

        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            return

        for file in os.listdir(folder_path):
            if file.endswith(".png"):
                image_path = os.path.join(folder_path, file)
                xml_filename = os.path.splitext(file)[0] + ".xml"
                xml_path = os.path.join(folder_path, xml_filename)

                if not os.path.exists(xml_path):
                    self.create_empty_xml(image_path, xml_path)
    
    def purger(self):

        """
        Goes through a folder, checks all XML files, and removes any XML file not in the allowed list.
        
        :param folder_path: Path to the folder containing XML files.
        :param allowed_files: List of XML filenames (without path) that should NOT be deleted.
        """
        
        folder_path = self.image_folder_path

        df = self.index_return()
        allowed_files = df['Filename'].to_list()

        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            return

        for file in os.listdir(folder_path):
            if file.endswith(".xml") and file not in allowed_files:
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Deleted: {file}")

        # pulls index
    
# note all xml files that exist
# if it's missing create an xml file
# create a condition to remove all empty xml files.
# need to create xml files for all data that's missing
