[English Version](./README-EN.md)

# LR相机预设

不会吧！不会吧！4202年了不会还有人没有玩转相机吧 🤡🤡，富士、佳能、索尼、徕卡、宾得、奥林巴斯官方预设手到擒来 🤏🤏，快点和我一起玩转相机 🛹🛹。



## 主要特征

* 拥有多种主流相机的官方预设

* 有Python环境一键起飞

* 快速批量处理

* 免费！

  


## 效果对比

- 索尼 PT 创意外观

<img src="./resources/Sony ILCE-7RM5 - PT.jpg" alt="Sony ILCE-7RM5" style="width:55%;"/>


- 富士 GFX 100S 相机 Classic Neg 胶片模拟

<img src="./resources/Fujifilm GFX 100S - Classic Neg.jpg" alt="Fujifilm GFX 100S" style="width:55%;"/>



## 安装环境

* Python
  * Anaconda 或者 PyCharm 均可

* Adobe Lightroom Classic
  * 正版 或者 科技 均可

* 安装

    * Linux环境
      ```bash
      $ git clone https://github.com/fengzhisuiyi/lr-camera-presets.git
      $ git python -m pip install -U pyexiftool
      ```
      
    * Windows环境
      * 下载解压
      
      * 通过包管理器如Anaconda Prompt安装pyexiftool
      
        ```bash
        $ python -m pip install -U pyexiftool
        ```
        
          


## 快速开始

* 把要修改的多个DNG照片放入image文件夹中

* 运行程序

    * Linux环境
      ```bash
      $ cd lr-camera-presets
      $ python main.py --camera Fujifilm GFX 100S
      ```

    * Windows环境
      * 打开main.py运行

* LR导入image文件夹中的照片

    * 修改照片 - 基本 - 配置文件，可以看到新增的预设

    

## 参数

|  参数  |      默认值       |                            可选值                            |                             备注                             |
| :----: | :---------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| camera | Fujifilm GFX 100S | ['Fujifilm GFX 100S', 'Sony ILCE-7', 'Sony ILCE-7RM5', 'Canon EOS R3', 'Canon EOS R5', 'Nikon Z 9', 'Leica SL2', 'Pentax K-1', 'Olympus E-5'] | 希望把照片修改为什么品牌的相机参数。linux环境运行可以把可选值其中一项作为camera参数传入。windows环境运行修改main.py第20行default的值进行替换 |
|  path  |      ./image      |                        任何存在的路径                        | 希望把那一个文件夹的照片信息全部进行修改，传入一个地址即可。如果不传入值，默认为项目的image文件夹下所有DNG文件信息进行替换 |



## 新增更多预设

* 修改/data/camera_info.csv，具体机型需要符合LR内部的参数，可以从**参考**【3】中观察

* 如果UniqueCameraModel不符合LR的相机型号，则导入的照片无预设。

* 如果Make列错误，则会报错ExifToolExecuteError: execute returned a non-zero exit status: 1

  

## 参考

【1】https://sylikc.github.io/pyexiftool/index.html

【2】https://helpx.adobe.com/cn/lightroom-classic/kb/tethered-camera-support.html

【3】https://helpx.adobe.com/cn/camera-raw/kb/camera-raw-plug-supported-cameras.html


```
@article{lr-camera-presets,
  author = {Starlight Damian},
  title = {lr-camera-presets: Wonderful view of the world},
  year = {2024}
}
```

