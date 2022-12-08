import pandas as pd

df = pd.read_csv("all_results_smina_pubchem_last.csv")


df[['BindingDB','Pubchem_CID']] = df["BindingDB_Pubchem"].str.split("_",expand=True)

df.to_csv("perş.csv")



## groupby 

import pandas as pd
df =pd.read_csv("all_tanimoto_results_more_7.csv")
df2 = df.groupby("CID_PubChem").agg(list).to_csv("output_per.csv", sep =",")
#df2 = df.groupby("CID_PubChem").agg(list)
