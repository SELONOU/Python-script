#====================================================================================================================================
#
#          FILE: rename1.sh
# 
# REQUIREMENTS: Put this script in the same directory with all files you want to rename 
# CREATED: 25-04-2022 
#====================================================================================================================================
#import os
#for filename in os.listdir('path'):
#        os.rename(filename, filename.replace('_', ''))


#Example to rename three csv files (i want in this case remove _ in all files in the same directory)                                                            
import os
for filename in os.listdir('/home/skankinou/Desktop/5e16_new/my_scr/renam_py/send_renam/red/rename_file/'):
        os.rename(filename, filename.replace('_', ''))
