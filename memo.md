docker-compose exec gs-app /bin/bash


ffmpeg -i "D:\Prj\gaussian-splatting\datasets\SolWallV3\mov\IMG_4337.MOV" img_%06d.png

python3 convert_png_to_8bit_multiprocess.py

python convert.py -s datasets/SolWallV3

```bash

root@5e36c48d8104:/gs_home# python3 convert.py -s datasets/SolWallV3
feat_extracton_cmd:colmap feature_extractor --database_path datasets/SolWallV3/distorted/database.db         --image_path datasets/SolWallV3/input         --ImageReader.single_camera 1         --ImageReader.camera_model OPENCV         --SiftExtraction.use_gpu 1

==============================================================================
Feature extraction
==============================================================================

...

Processed file [25/107]
  Name:            img_000601.png
  Dimensions:      1080 x 1920
  Camera:          #2 - OPENCV
  Focal Length:    2304.00px
  Features:        5495
Processed file [26/107]
  Name:            img_000626.png
  Dimensions:      1080 x 1920
  Camera:          #2 - OPENCV
  Focal Length:    2304.00px
  Features:        4306
Processed file [27/107]
  Name:            img_000651.png
  Dimensions:      1080 x 1920
  Camera:          #2 - OPENCV
  Focal Length:    2304.00px
  Features:        3575

...


```


```bash

==============================================================================
Exhaustive feature matching
==============================================================================

Matching block [1/14, 1/14] in 177.273s
Matching block [1/14, 2/14] in 199.824s
Matching block [1/14, 3/14] in 303.287s
Matching block [1/14, 4/14]
```



```bash


```



```bash


```