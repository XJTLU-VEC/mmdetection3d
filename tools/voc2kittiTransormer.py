import os

base_dir = "/mnt/mmdection3D/data/radar"


def changeVelodyne(based_path, path_stage_2, path_stage_3, prefix):
    files = os.listdir(os.path.join(based_path, path_stage_2, path_stage_3))
    os.chdir(os.path.join(based_path, path_stage_2, path_stage_3))
    for file in files:
        idx = ('{:06d}'.format(int(str(file).split(".")[0])))
        os.rename(file, (str(idx) + '.' + prefix))
    return 0


if __name__ == '__main__':
    changeVelodyne(base_dir, "training", "image_2", "png")
    changeVelodyne(base_dir, "testing", "image_2", "png")
    changeVelodyne(base_dir, "training", "velodyne", "bin")
    changeVelodyne(base_dir, "testing", "velodyne", "bin")
    changeVelodyne(base_dir, "training", "label_2", "txt")
    changeVelodyne(base_dir, "training", "calib", "txt")
    changeVelodyne(base_dir, "testing", "calib", "txt")

