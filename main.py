"""
Date: 08/03/2021
author: MariPS
"""

import os
import shutil
from tkinter import filedialog

# get path to spotlight images
local_app_data = os.environ['LOCALAPPDATA']
path_to_images = local_app_data + '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

# get directory where the images have to be saved
path_to_save_imgs = filedialog.askdirectory()

# for each image in the directory
with os.scandir(path_to_images) as dir_contents:
    tmpfiles = []
    for entry in dir_contents:
        if entry.stat().st_size/1024 >= 400:
            tmpfiles.append(os.path.join(path_to_save_imgs, entry.name + ".jpg"))
            shutil.copy2(entry, tmpfiles[-1])
