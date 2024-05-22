[中文介绍](./README.md)

# lr-camera-presets

No way! No way! It's 4202, and you still haven't mastered your camera? 🤡🤡 Official presets for Fujifilm, Canon, Sony, Leica at your fingertips 🤏🤏. Come and master your camera with me 🛹🛹.



## Main Features

* Official presets for various mainstream cameras

* One-click operation with a Python environment

* Fast batch processing

* Free!

  

## Comparison

- Sony PT Creative Look

  <img src="./resources/Sony ILCE-7RM5 - PT.jpg" alt="Sony ILCE-7RM5" style="width:55%;"/>

- Fujifilm GFX 100S Camera Classic Neg Film Simulation

  <img src="./resources/Fujifilm GFX 100S - Classic Neg.jpg" alt="Fujifilm GFX 100S" style="width:55%;"/>
  
  

## Installation

* Python
  * Anaconda or PyCharm

* Adobe Lightroom Classic
  * Official or other versions

* Installation

    * Linux Environment
      ```bash
      $ git clone https://github.com/fengzhisuiyi/lr-camera-presets.git
      ```

    * Windows Environment
      * Download and extract the files
      
        

## Quick Start

* Place multiple DNG photos you want to modify in the image folder

* Run the program

    * Linux Environment，you can setup from the source
      ```bash
      $ cd lr-camera-presets
      $ python main.py --camera Fujifilm GFX 100S
      ```

    * Windows Environment
      * Run main.py

* Import the photos from the image folder into Lightroom

    * Modify the photos - Basic - Profile to see the new presets
    
      

## Parameters

| Parameter |   Default Value   |                           Options                            |                            Notes                             |
| :-------: | :---------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  camera   | Fujifilm GFX 100S | ['Fujifilm GFX 100S', 'Sony ILCE-7', 'Sony ILCE-7RM5', 'Canon EOS R3', 'Canon EOS R5', 'Nikon Z 9', 'Leica SL2'] | The camera brand parameters you want to modify the photos for. In Linux, pass one of the options as the camera parameter. In Windows, modify the default value at line 20 of main.py. |
|   path    |      ./image      |                        Any valid path                        | The folder whose photos you want to modify. If not provided, defaults to all DNG files in the project's image folder. |



## Adding More Presets

* Modify /data/camera_info.csv. The specific model must match Lightroom's internal parameters, which can be found in **Reference** [3].

* If UniqueCameraModel does not match Lightroom's camera model, the imported photo will have no preset.

* If the Make column is incorrect, you will encounter ExifToolExecuteError: execute returned a non-zero exit status: 1.

  

## References

* [1] https://sylikc.github.io/pyexiftool/index.html
* [2] https://helpx.adobe.com/cn/lightroom-classic/kb/tethered-camera-support.html
* [3] https://helpx.adobe.com/cn/camera-raw/kb/camera-raw-plug-supported-cameras.html

```@article{lr-camera-presets,
  author = {Starlight Damian},
  title = {lr-camera-presets: Wonderful view of the world},
  year = {2024}
}
