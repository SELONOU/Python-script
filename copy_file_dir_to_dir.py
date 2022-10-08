import shutil
import pandas as pd
df = pd.read_csv("files_2.csv", delimiter=" ", header=None)
print(df)
filenames= df[0].to_list()
print(filenames)
for filename in filenames:
     shutil.copy2('/cta/users/myildiz/workspace/selonou/bases_kinases_proposed/log_files_opt_bases_kinaes/another/source_dir/%s.log'%filename, '/cta/users/myildiz/workspace/selonou/bases_kinases_proposed/log_files_opt_bases_kinaes/another/old_test/%s.log'%filename)
