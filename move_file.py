import os
import shutil
from pathlib import Path

source_folder = r"C:\temp\source\folder"
target_folder = r"C:\temp\target\folder"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for root, dirs, files in os.walk(source_folder):
    for name in files:
        if name.endswith("msp"):
            soure_file_path = root + os.sep + name

            target_file_name = name[:-4] + "_" + root[48:57] + ".msp"
            target_file_path = target_folder + os.sep + target_file_name

            print(soure_file_path)
            print(target_file_path)

            shutil.move(soure_file_path, target_file_path)
