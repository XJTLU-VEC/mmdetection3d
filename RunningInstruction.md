
## Run PointPillars on VoD Dataset

### Step 1
Modify **base_dir** to the path of the data.

Then, run
```shell script
python tools/voc2kittiTransormer.py
```

### Step 2
Run 
```shell
python tools/create_data.py kitti --root-path /mnt/mmdection3D/data/radar --out-dir /mnt/mmdection3D/data/radar  --extra-tag kitti
```
root-path are the path of the data

### Step 3
Modify the **root-path** in `configs/_base_/datasets/kitti-3d-3class.py`

Then, run 
```shell script
python tools/train.py configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py
```

