# todo: * - NOT POSSIBLE TO RUN

import os
import requests
import subprocess

import Telegram_Backup
import shutil

linwin_sep = os.sep



#1. Make folder structure
try:
    print("Creating Directories")
    os.mkdir(f'{self.thisdir}{linwin_sep}{self.root}')
    os.mkdir(f'{self.thisdir}{linwin_sep}{self.root}{linwin_sep}{self.channel}')
except FileExistsError:
    print("We got file exist error. Continuing..")

#2. Run a blocking system command - assume when this is done we will have a downloaded torrernt file
#3. user should be sure that the torrent does not go inside a zip/rar / archive
#4. when download is done...delete all files except the largest mp4 file - also user should make sure its mp4


#5. send to channel Upload process
try:
    # ensure that only 1 file is present - just a copy paste from youtube - needs to bedefined
    if len(os.listdir(output_dir)) == 1:
        print("Backup is starting only 1 file is present")
        self.channel_id = self.backup_obj.back_all(silent=True, channel_id=self.channel_id)
        print(self.channel_id)
    else:
        print("More than one file found. Breaking script")
        break
except ValueError:
    print("We are getting channel not found error")
    break


subprocess.run('ping')
