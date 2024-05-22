# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:12:10 2024

@author: Starlight Damian
"""
import os
import logging

import pandas as pd
from exiftool import ExifToolHelper

from __init__ import path

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def set_tags(image_path_list, tags):
    """
    Modify camera parameters of photos
    """
    logging.info(f'Start modifying parameters: {image_path_list}')
    
    with ExifToolHelper() as et:
        logging.info(f'Modified parameters: {tags}')
        et.set_tags(
            image_path_list,
            tags=tags,
            params=["-P", "-overwrite_original"]
        )
        logging.info('Complete modifying parameters')
        
def get_tags(image_path_list):
    """
    Get the specified parameters of the photo
    """
    with ExifToolHelper() as et:
        for d in et.get_tags(image_path_list, tags=['make', 'model', 'uniquecameramodel']):
            for k, v in d.items():
                print(f"Dict: {k} = {v}")

def pipline(image_path, camera):
    """
    The overall process of modifying camera parameters
    """
    image_path_list = [f'{image_path}/{filename}' for filename in os.listdir(image_path)]
    
    camera_info_df = pd.read_csv(f'{path}/data/camera_info.csv', encoding='gb18030')
    camera = camera if camera in camera_info_df.UniqueCameraModel.values else 'Fujifilm GFX 100S'
    tags = camera_info_df[camera_info_df.UniqueCameraModel == camera].to_dict(orient='records')[0]
    
    set_tags(image_path_list, tags=tags)
    get_tags(image_path_list)