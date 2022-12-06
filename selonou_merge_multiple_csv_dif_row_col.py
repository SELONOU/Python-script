import pandas as pd
import os

files = [i for i in os.listdir(".") if i.endswith(".csv")] # load all csv files with extension csv
combine_csv = pd.concat([pd.read_csv(f) for f in files]).to_csv("all_tanimoto_results_more_7.csv", index= False)


## another 
# load csv files located into same directory (path)
import pandas as pd
import glob 
import os
os.chdir("/cta/users/myildiz/workspace/selonou/tanimoto_similarity_separated/job_tanimoto/all_tanimoto_resulst_files/tanimoto_more_07_score/combine_sinle/test_com/")
extension="csv"
filenames = [i for i in glob.glob('*.{}'.format(extension))]
results_combibnation = pd.concat([pd.read_csv(f) for f in filenames]).to_csv("merge_git_salı2.csv", sep = ",", index= False)



## add files names after merging multiple csv files (concat)
import pandas as pd
import glob, os
path = '/cta/users/myildiz/workspace/selonou/tanimoto_similarity_separated/job_tanimoto/all_tanimoto_resulst_files/tanimoto_more_07_score/combine_sinle/test_com/'
filenames = glob.glob(os.path.join(path, "*.csv"))
pd.concat([pd.read_csv(f, sep='\s+').assign(file=os.path.basename(f)) for f in filenames]).to_csv('results_merged.csv', index=False)
