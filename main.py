# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:17:41 2024

@author: Starlight Damian

python -m pip install -U pyexiftool
file_types in ["a.jpg", "b.png", "c.tif", "d.dng"]
camera in ['Fujifilm GFX 100S', 'Sony ILCE-7', 'Sony ILCE-7RM5', 'Canon EOS R3', 'Canon EOS R5', 'Nikon Z 9', 'Leica SL2']
"""
import argparse

from __init__ import path
import utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--camera', type=str, default='Fujifilm GFX 100S', help='Camera uniquecameramodel')
    parser.add_argument('--path', type=str, default=f'{path}/image', help='The path to the folder where the photos are located')
    args = parser.parse_args()
    
    utils.pipline(args.path, args.camera)
    
    
    
