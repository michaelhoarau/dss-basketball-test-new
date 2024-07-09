# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
basketball_nScores = dataiku.Dataset("Basketball_nScores")
basketball_nScores_df = basketball_nScores.get_dataframe()

#copy df, increment year by 1 and join so past stats are available in row
basketball_nScores_df2=basketball_nScores_df.copy()
basketball_nScores_df2['Year']+=1
df1 = pd.merge(left=basketball_nScores_df,right=basketball_nScores_df2,how='left',left_on=['Player','Year'],right_on=['Player','Year'])

#take note if player switched teams
df1['Tm_Switch']=df1["Tm_x"]!=df1['Tm_y']

#create rows for next year of prediction
df2=df1[df1['Year']==2018].copy()
df2['Year']+=1
df2[[col for col in df2 if (col[-1] == 'x')]]='NaN'

#combine into one dataframe
df= pd.concat([df1, df2])

#check work
#df[df['Year']==2019]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
basketball_injuries_df = df # For this sample code, simply copy input to output


# Write recipe outputs
basketball_injuries = dataiku.Dataset("py_basketball_prepared")
basketball_injuries.write_with_schema(df)