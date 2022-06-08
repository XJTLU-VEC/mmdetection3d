
### run pointpillar in vod dataset

### step 1
Run
```shell script
tools/voc2kittiTransormer.py
```
Remember change base_dir to the path of the data

#### Step 2
Run 
```shell
tools/create_data.py 
```
by 
```shell
kitti --root-path /mnt/mmdection3D/data/radar --out-dir /mnt/mmdection3D/data/radar  --extra-tag kitti
root-path are the path of the data
```

#### step 3
change 
```shell
configs/_base_/datasets/kitti-3d-3class.py
data_root 
```
to the root-path are the path of the data 


Run 
```shell script
tools/train.py
```
by 
```shell script
/configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py
```
