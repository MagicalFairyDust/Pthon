import pandas as pd

df = pd.read_excel ('/Users/bombom/Downloads/data srplg17.xlsx',sheet_name='Sheet2')
dafdil = pd.read_excel('/Users/bombom/Downloads/datadildf.xlsx',sheet_name='Sheet1')
dafdil2 = pd.read_excel('/Users/bombom/Downloads/datadildf.xlsx',sheet_name='Sheet2')

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
    
is_int_array = df['idpelangga'].apply(is_int)

dff = df[is_int_array]
dff['idpelangga']=dff['idpelangga'].astype('int64')

merge_df = pd.merge(dff, dafdil, left_on = 'idpelangga',right_on='idpelanggan')
merge_df2 = pd.merge(dff, dafdil2, left_on = 'idpelangga',right_on='nokwh')

appen_df = pd.concat([merge_df,merge_df2],axis=0,ignore_index=True).sort_values(by=['Join_Count','idpelanggan'],ascending=[False,True]).drop_duplicates(subset='idpelanggan',keep='first')

print (appen_df.pivot_table(appen_df,index='UNITUP',columns='Joint_Count', values='idpelangga',aggfunc='count'))