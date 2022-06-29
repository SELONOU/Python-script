import os
for filename in os.listdir('/home/skankinou/Desktop/5e16_new/my_scr/renam_py/'):
        os.rename(filename, filename.replace('_', ''))
