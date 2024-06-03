[中文介绍](./README.md)

# LR Camera Presets

No way! No way! It's already the year 4202 and some people still haven't mastered their cameras 🤡🤡? Official presets for Fujifilm, Canon, Sony, Leica, Pentax, Olympus are at your fingertips 🤏🤏. Join me in mastering your camera 🛹🛹.

By modifying the camera information in DNG files, you can use the camera's LR presets after importing the photos into Lightroom.

## Main Features

* Official presets for various mainstream cameras
* One-click setup with Python environment
* Fast batch processing
* Free!

## Comparison of Effects

- Sony PT Creative Look

<img src="./resources/Sony ILCE-7RM5 - PT.jpg" alt="Sony ILCE-7RM5" style="width:55%;"/>

- Fujifilm GFX 100S Camera Classic Neg Film Simulation

<img src="./resources/Fujifilm GFX 100S - Classic Neg.jpg" alt="Fujifilm GFX 100S" style="width:55%;"/>

## Installation Environment

* Python
  * Either Anaconda or PyCharm is fine

* Adobe Lightroom Classic
  * Genuine or otherwise

* Installation

    * Linux environment
      ```bash
      $ git clone https://github.com/StarlightDamian/lr-camera-presets.git
      $ git python -m pip install -U pyexiftool
      ```

    * Windows environment
      * Download and extract
      
      * Install pyexiftool via a package manager like Anaconda Prompt
      
        ```bash
        $ python -m pip install -U pyexiftool
        ```

## Quick Start

* Place the DNG photos you want to modify in the image folder

* Run the program

    * Linux environment
      ```bash
      $ cd lr-camera-presets
      $ python main.py --camera Fujifilm GFX 100S
      ```

    * Windows environment
      * Open and run main.py

* Import photos from the image folder into LR

    * Modify photos - Basic - Profile, you can see the new presets
      <img src="./resources/LR-basic-configuration file.png" alt="configuration file" style="width:45%;"/>
      <img src="./resources/LR-basic-configuration file-creative look.png" alt="creative look" style="width:45%;"/>

## Parameters

|  Parameter  |    Default Value    |                           Optional Values                            |                             Notes                             |
| :---------: | :-----------------: | :------------------------------------------------------------------: | :------------------------------------------------------------: |
|   camera    | Fujifilm GFX 100S   | ['Fujifilm GFX 100S', 'Sony ILCE-7', 'Sony ILCE-7RM5', 'Canon EOS R3', 'Canon EOS R5', 'Nikon Z 9', 'Leica SL2', 'Pentax K-1', 'Olympus E-5'] | Specifies the camera parameters you want to modify the photos to. When running in a Linux environment, pass one of the optional values as the camera parameter. In a Windows environment, modify the default value on line 20 of main.py. |
|    path     |      ./image        |                          Any existing path                          | Specifies the folder containing the photos whose information you want to modify. If no value is passed, the information of all DNG files in the project's image folder will be modified. Does not handle .NEF, .CR2, .CR3, .RAF, .ARW, or other RAW formats. |

## Adding More Presets

* Modify /data/camera_info.csv; specific models must match LR's internal parameters, which can be observed from **Reference** [3].

* If UniqueCameraModel does not match LR's camera model, the imported photos will have no presets.

* If the Make column is incorrect, it will result in an error: ExifToolExecuteError: execute returned a non-zero exit status: 1.

## References

[1] https://sylikc.github.io/pyexiftool/index.html

[2] https://helpx.adobe.com/lightroom-classic/kb/tethered-camera-support.html

[3] https://helpx.adobe.com/camera-raw/kb/camera-raw-plug-supported-cameras.html

```
@article{lr-camera-presets,
  author = {Starlight Damian},
  title = {lr-camera-presets: Wonderful view of the world},
  year = {2024}
}
```