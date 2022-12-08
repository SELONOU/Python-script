import pandas as pd

df = pd.read_csv("all_results_smina_pubchem_last.csv")


df[['BindingDB','Pubchem_CID']] = df["BindingDB_Pubchem"].str.split("_",expand=True)

df.to_csv("perş.csv")
