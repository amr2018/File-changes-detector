
import time
import os

old_files = os.listdir(os.curdir)
print(old_files)

while True:
    new_files = os.listdir(os.curdir)
    if old_files != new_files:
        print('New Changes Detected : ', new_files)
        old_files = new_files
        
    time.sleep(2)
