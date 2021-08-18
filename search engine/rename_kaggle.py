import glob
import os
import numpy as np

# Path for train and test (if exist)
train_path = "train\\"
test_path = "test\\"

train_dir_path = glob.glob(train_path + "*")
test_dir_path = glob.glob(test_path + "*")

# Combine all
for string in test_dir_path:
    train_dir_path.append(string)

# Get all filenames inside each dir
image_path = []
for idx, string in enumerate(train_dir_path):
    image_path.append(np.asarray(glob.glob(string + "\*")))

# Combine all image in one array
main_image_array = []
for subarray in image_path:
    for path in subarray:
        main_image_array.append(path)

# Saving path
# Data will be lost after replacing make sure have backup
save_dir = "labelimg\\train"

# Rename file
for old_path in main_image_array:
    new_name = old_path.split("\\")[0] + "_" + old_path.split("\\")[1] + "_" + old_path.split("\\")[2]
    new_path = os.path.join(save_dir, new_name)
    os.rename(old_path, new_path)